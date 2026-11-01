#!/usr/bin/env python3
"""
GitHub Operations Helper for ALO Doctor Platform
Provides seamless issue creation, comment posting, and status updates
without shell escaping issues.
"""

import urllib.request
import urllib.error
import json
import os
import sys
import argparse

REPO = os.getenv("GITHUB_REPO", "kathirvelmurugan/second-consult")
TOKEN = os.getenv("GITHUB_TOKEN")

def get_headers():
    if not TOKEN:
        print("Error: GITHUB_TOKEN environment variable not set.")
        sys.exit(1)
    return {
        "Authorization": f"token {TOKEN}",
        "User-Agent": "ALO-Doctor-Helper",
        "Content-Type": "application/json",
        "Accept": "application/vnd.github.v3+json"
    }

def create_issue(title, body, labels=None):
    url = f"https://api.github.com/repos/{REPO}/issues"
    payload = {
        "title": title,
        "body": body,
        "labels": labels or []
    }
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=get_headers())
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"Created Issue #{data['number']}: {data['title']}")
            return data
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.read().decode()}")
        return None

def add_comment(issue_number, comment):
    url = f"https://api.github.com/repos/{REPO}/issues/{issue_number}/comments"
    payload = {"body": comment}
    req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=get_headers())
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"Comment added to Issue #{issue_number}")
            return data
    except urllib.error.HTTPError as e:
        print(f"HTTP Error {e.code}: {e.read().decode()}")
        return None

def main():
    parser = argparse.ArgumentParser(description="GitHub Helper Tool")
    subparsers = parser.add_subparsers(dest="action")

    # Issue creation
    p_issue = subparsers.add_parser("create-issue")
    p_issue.add_argument("--title", required=True)
    p_issue.add_argument("--body", required=True)
    p_issue.add_argument("--labels", nargs="*", default=[])

    # Comment creation
    p_comment = subparsers.add_parser("comment")
    p_comment.add_argument("--issue", type=int, required=True)
    p_comment.add_argument("--body", required=True)

    args = parser.parse_args()
    if args.action == "create-issue":
        create_issue(args.title, args.body, args.labels)
    elif args.action == "comment":
        add_comment(args.issue, args.body)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
