#!/usr/bin/env python3
"""
Seed 5 Concurrent Worker GitHub Issues for ALO Doctor Platform
Repository: kathirvelmurugan/second-consult
"""

import urllib.request
import json
import os
import sys

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
if not GITHUB_TOKEN:
    print("Error: Please set GITHUB_TOKEN environment variable.")
    sys.exit(1)
REPO = "kathirvelmurugan/second-consult"

ISSUES = [
    {
        "title": "[STREAM 1 / WORKER 1] Patient Intake Engine & Payment Gateway (Stages 1 & 4)",
        "labels": ["stream-1", "intake", "payment", "worker-1"],
        "body": """### 🚀 STREAM 1: Patient Intake, SMS OTP & Payment Gateway
**Target Stages**: 
- `STAGE_1: INTAKE_RECEIVED` (P01–P14)
- `STAGE_4: AWAITING_PAYMENT` (P19–P21, C04)

#### **Roles Handled**:
- `P`: Patient (Consumer / Care Receiver via WhatsApp & Mobile App)
- `C`: ALO Coordinator (Invoice Generation)

#### **Functional Checklist Gates to Deliver**:
- [ ] **Saudi ID / Iqama Verification**: 4-digit SMS OTP integration (`P02`-`P03`).
- [ ] **Intake Form & File Drops**: Medical reports, DICOM CT/MRI scans, echocardiograms (`P04`, `P06`).
- [ ] **WhatsApp Webhook Listener**: Meta Cloud API listener for conversational intake (`W01`, `W02`).
- [ ] **Invoice & VAT Engine**: 15% Saudi ZATCA compliant invoice calculation (`C04`).
- [ ] **Mada / Apple Pay Integration**: Payment sheet `/p/{token}/pay` with webhook callback (`P19`-`P20`).
- [ ] **Receipt Generation**: Stamped VAT receipt dispatched via WhatsApp `W06`.
- [ ] **Exception Handlers**:
  - `X01`: Card declined (auto-retry link dispatched).
  - `X02`: Payment expired after 48 hours (auto-cancel and slot release).

#### **Key API Endpoints**:
- `POST /api/v1/intake/submit`
- `POST /api/v1/intake/verify-otp`
- `POST /api/v1/payments/create-intent`
- `POST /api/v1/webhooks/payment`
- `POST /api/v1/webhooks/whatsapp`
"""
    },
    {
        "title": "[STREAM 2 / WORKER 2] Clinical Nurse Triage & Saudi Treating Doctor Desk (Stages 2 & 3)",
        "labels": ["stream-2", "triage", "saudi-doctor", "worker-2"],
        "body": """### 🚀 STREAM 2: Clinical Triage & Saudi Doctor Desk
**Target Stages**:
- `STAGE_2: NURSE_CHECK` (N01–N07)
- `STAGE_3: DOCTOR_REVIEW` (D01–D10)

#### **Roles Handled**:
- `N`: ALO Nurse (Triage & Translator)
- `D`: Saudi Treating Doctor (Licensed KSA Physician)

#### **Functional Checklist Gates to Deliver**:
- [ ] **Nurse Triage Inbox**: File completeness inspection (detect corrupted scans/DICOM) (`N02`).
- [ ] **Missing File Re-upload Trigger**: WhatsApp template `W03` triggered directly to patient.
- [ ] **Bilingual Clinical Summary**: Structured Arabic/English case summary authoring (`N04`).
- [ ] **Doctor Review Interface**: Case approval and medical rationale validation (`D02`).
- [ ] **Consultant Picker**: Directory of affiliated Indian super-specialists (KIMS, Aster, HCG) (`D04`).
- [ ] **Clinical Question Authoring**: Strict requirement of 2 focus questions (`D03`).
- [ ] **Exception Handlers**:
  - `X05`: Missing scan -> auto-request to patient.
  - `X09`: Saudi doctor review overdue (>24h) -> escalate to Hospital Admin `HA`.

#### **Key API Endpoints**:
- `GET /api/v1/nurse/triage/queue`
- `POST /api/v1/nurse/triage/:caseId/validate`
- `POST /api/v1/nurse/triage/:caseId/request-missing`
- `GET /api/v1/doctor/cases/pending`
- `POST /api/v1/doctor/cases/:caseId/approve-consultant`
"""
    },
    {
        "title": "[STREAM 3 / WORKER 3] Global Consultant Workspace & Privacy De-identification Firewall (Stages 5 & 6)",
        "labels": ["stream-3", "consultant", "privacy-firewall", "worker-3"],
        "body": """### 🚀 STREAM 3: Global Consultant Portal & Privacy Firewall
**Target Stages**:
- `STAGE_5: WITH_CONSULTANT` (K01–K07)
- `STAGE_6: OPINION_READY` (K08, P23–P25, C08)

#### **Roles Handled**:
- `K`: Indian Consultant (Global Super-Specialist)
- `C`: ALO Coordinator (Bilingual Translation Auditor)

#### **Functional Checklist Gates to Deliver**:
- [ ] **Privacy Firewall**: Automated de-identification pipeline stripping Patient National IDs, names, and phone numbers before consultant sees files.
- [ ] **Consultant Mobile/Web Workspace**: Clean English-only interface displaying questions, clinical summary, and de-identified DICOM scans.
- [ ] **SLA Acceptance Timer**: 48-hour acceptance/decline SLA countdown (`X10`).
- [ ] **3-Party WebRTC Video Room**: Secure, browser-based video room connecting Consultant, Saudi Dr, Patient, and ALO Nurse translator (`P23`).
- [ ] **Written Opinion Authoring**: Structured second opinion drafting tool (`K08`).
- [ ] **Bilingual Certified Stamped PDF**: PDF generator combining English specialist report and certified Arabic translation (`P25`).
- [ ] **Exception Handlers**:
  - `X10`: Consultant overdue (>48h) -> Auto-route to backup consultant.
  - `X12`: Consultant declines -> Coordinator reassigns or initiates refund.
  - `X16`: Video call drops -> fallback to audio bridge.

#### **Key API Endpoints**:
- `GET /api/v1/consultant/cases/:caseId/deidentified`
- `POST /api/v1/consultant/cases/:caseId/accept`
- `POST /api/v1/consultant/cases/:caseId/submit-opinion`
- `POST /api/v1/video/room/create`
- `POST /api/v1/reports/generate-pdf`
"""
    },
    {
        "title": "[STREAM 4 / WORKER 4] Saudi Partner Care Ecosystem (Lab, Pharmacy, Nursing, Physio) (Stages 7 & 8)",
        "labels": ["stream-4", "partners", "lab", "pharmacy", "worker-4"],
        "body": """### 🚀 STREAM 4: Saudi Partner Care Ecosystem & 21-Day Follow-Up
**Target Stages**:
- `STAGE_7: PARTNER_SERVICES` (L01, H01, T01, V01, D09-D10)
- `STAGE_8: FOLLOW_UP_21_DAYS` (P27–P29, W17–W19)

#### **Roles Handled**:
- `L`: Pathology Lab Technician
- `H`: Community Pharmacist
- `T`: Physiotherapist
- `V`: Home Nursing Tech
- `P`: Patient

#### **Functional Checklist Gates to Deliver**:
- [ ] **Lab Order Routing**: Phlebotomy dispatch tracking & diagnostic report upload (`L01`, `W13`).
- [ ] **Pharmacy E-Prescription**: Cash vs Insurance pricing, stock check, delivery/pickup (`H01`, `W14`).
- [ ] **Generic Substitution Engine**: Exception `X20` workflow for out-of-stock brand medications.
- [ ] **Home Nursing Dispatch**: Map dispatch interface for nurse home visits (vitals, injections) (`V01`, `W16`).
- [ ] **Physiotherapy Booking**: In-clinic or home rehab schedule management (`T01`, `W15`).
- [ ] **21-Day Follow-Up Chat**: Secure messaging channel between Patient, Nurse, and Saudi Doctor (`P27`).

#### **Key API Endpoints**:
- `POST /api/v1/partner/lab/order`
- `POST /api/v1/partner/pharmacy/prescribe`
- `POST /api/v1/partner/nursing/dispatch`
- `POST /api/v1/partner/physio/book`
- `GET/POST /api/v1/followup/:caseId/chat`
"""
    },
    {
        "title": "[STREAM 5 / WORKER 5] Master State Machine, Single-Page Cockpit & Audit Engine (Stage 9 & Architecture)",
        "labels": ["stream-5", "orchestrator", "super-admin", "worker-5"],
        "body": """### 🚀 STREAM 5: Master State Machine, Single-Page Cockpit & Audit Engine
**Target Stages**:
- `STAGE_9: CLOSED` (W20)
- Administrative Settings & 11-Role RBAC Model
- Single-Page Cockpit & Audit Trail Ledger

#### **Roles Handled**:
- `AD`: ALO Super Admin
- `HA`: Hospital Partner Admin
- Universal Role Switcher (`P`, `D`, `N`, `C`, `K`, `L`, `H`, `T`, `V`, `HA`, `AD`)

#### **Functional Checklist Gates to Deliver**:
- [ ] **Single-Page Master Flow Cockpit**: Dynamic 9-stage view with condition checklists, role picker, and live SLA countdowns.
- [ ] **Finite State Machine (FSM)**: Strict condition validation preventing stage advancement until all mandatory criteria are checked.
- [ ] **Audit Trail Ledger**: Immutable event logger capturing Actor, Role, Timestamp, and Action taken.
- [ ] **Multi-Tier Admin Settings**: Hospital management, dynamic test catalog, formulary pricing, and slot templates.
- [ ] **Case Closure & CSAT Engine**: 21-day auto-expiry, archive lock, and WhatsApp `W20` 5-star survey trigger.
- [ ] **In-Kingdom Data Sovereignty Verification**: Verify all scans and PII reside on local KSA volumes.

#### **Key API Endpoints**:
- `GET /api/v1/cases/:caseId/state`
- `POST /api/v1/cases/:caseId/transition`
- `GET /api/v1/cases/:caseId/timeline`
- `POST /api/v1/admin/hospitals`
- `POST /api/v1/admin/catalogs`
"""
    }
]

def create_issue(issue_data):
    url = f"https://api.github.com/repos/{REPO}/issues"
    req = urllib.request.Request(
        url,
        data=json.dumps(issue_data).encode("utf-8"),
        headers={
            "Authorization": f"token {GITHUB_TOKEN}",
            "User-Agent": "ALO-Doctor-Seeder",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github.v3+json"
        }
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            print(f"Created Issue #{data['number']}: {data['title']}")
            return data
    except Exception as e:
        print(f"Error creating issue '{issue_data['title']}': {e}")
        return None

def main():
    print(f"Seeding 5 Concurrent Process Issues into {REPO}...")
    for item in ISSUES:
        create_issue(item)
    print("Done seeding issues!")

if __name__ == "__main__":
    main()
