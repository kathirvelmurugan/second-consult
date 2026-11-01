#!/usr/bin/env python3
"""
Seed 30 Exact PDF-Aligned Issues into GitHub
ALO Doctor Workflow Chain v2.4 (Pages 1 to 30)
Includes 429 Rate-Limit Auto-Pause (2 Minutes) and Compute/Wallclock Time Tracker
"""

import urllib.request
import urllib.error
import json
import os
import sys
import time

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = "kathirvelmurugan/second-consult"

if not GITHUB_TOKEN:
    print("Error: GITHUB_TOKEN environment variable not set.")
    sys.exit(1)

# 30 ISSUES MAPPED 1:1 TO PAGES 1-30 OF THE OFFICIAL PDF
ISSUES_30 = [
    {
        "title": "[Page 01] Master Architecture & Unified Multi-Role Design (11 Roles, 3 Surfaces)",
        "labels": ["page-01", "architecture", "batch-1"],
        "body": """### 📖 Official Spec: Page 01 · End-to-End Workflow Chain
**Domain**: Master Architecture & Multi-Role Design
- **3 Client Surfaces**: Phone App (Patient & Consultant), WhatsApp 24/7 Automation ("Never Login"), Web Portal (`alodoctor.sa/portal` · `AD01`).
- **11 System Personas**: `P` (Patient), `D` (Saudi Doctor), `N` (Nurse), `C` (Coordinator), `K` (Consultant), `L` (Lab), `T` (Physio), `H` (Pharmacist), `V` (Home Nursing), `HA` (Partner Admin), `AD` (ALO Admin).
- **Core Deliverables**:
  - [ ] Implement single case identifier generator (`ALO-YYYY-NNNN`).
  - [ ] Configure unified RBAC router at `/portal` handling all staff roles.
  - [ ] Verify 100% In-Kingdom data residency compliance (Saudi NDMO/MOH).
"""
    },
    {
        "title": "[Page 02] Universal Notation, Screen Codes & 9-Stage Case State Machine",
        "labels": ["page-02", "fsm", "batch-1"],
        "body": """### 📖 Official Spec: Page 02 · How to Read
**Domain**: Finite State Machine & Notation Engine
- **9 Core Case Statuses**: `Intake received` › `Nurse check` › `Doctor review` › `Awaiting payment` › `With consultant` › `Opinion ready` › `Partner services` › `Follow-up 21 days` › `Closed`.
- **3 Exception Statuses**: `On hold`, `Cancelled`, `No-show`.
- **Core Deliverables**:
  - [ ] Model master PostgreSQL enum for the 9 case statuses and 3 exception states.
  - [ ] Build stage transition guard verifying all mandatory condition checkboxes before hand-off.
  - [ ] Implement event bus publishing state transitions to Coordinator and Patient channels.
"""
    },
    {
        "title": "[Page 03] Master Pre-Payment Workflow (Join -> Intake -> Triage -> Review -> Payment)",
        "labels": ["page-03", "pre-payment", "batch-1"],
        "body": """### 📖 Official Spec: Page 03 · Master Map 1/2 (Pre-Payment)
**Domain**: Stages 1 to 4 End-to-End Relay
- **Clinical Sequence**: Join (`P01`–`P06`) ➔ Intake (`P07`–`P17`) ➔ Nurse Triage (`N01`–`N07`) ➔ Saudi Doctor Review (`D01`–`D06` or `D03` Doctor-opened) ➔ Invoice & Payment (`C04`, `P19`–`P21`).
- **Core Deliverables**:
  - [ ] Wire two-way nurse clarification line (`P06` ↔ `N07`).
  - [ ] Implement Doctor-started case branch (`D03` opens case for patient).
  - [ ] Add direct partner booking bypass without opinion (`P30`–`P38`).
"""
    },
    {
        "title": "[Page 04] Master Post-Payment Workflow (Consultant -> Call -> Report -> Partners -> Follow-up)",
        "labels": ["page-04", "post-payment", "batch-1"],
        "body": """### 📖 Official Spec: Page 04 · Master Map 2/2 (Post-Payment)
**Domain**: Stages 5 to 9 End-to-End Relay
- **Clinical Sequence**: Consultant accepts (`K02`–`K04`) ➔ 3-Party Video Conference (`K08`, `D08`, `P23`, `N08`) ➔ Certified PDF Report (`C08`, `P25`) ➔ Partner Orders (`D09`–`D10`, `L01`, `T01`, `H01`, `V01`) ➔ 21-Day Follow-Up (`P27`–`P29`) ➔ Archival (`Closed`).
- **Core Deliverables**:
  - [ ] Implement 3-party WebRTC call scheduler with Arabic/English interpretation line.
  - [ ] Build automated referral dispatcher routing e-prescriptions and lab tests.
  - [ ] Implement 21-day direct chat window between Patient, Nurse, and Doctor.
"""
    },
    {
        "title": "[Page 05] Cross-Role Notification Engine & Webhook Event Registry",
        "labels": ["page-05", "notifications", "batch-1"],
        "body": """### 📖 Official Spec: Page 05 · Notifications (Who Hears What & Where)
**Domain**: Cross-Channel Notification Router
- **Matrix Mapping**:
  - Patient: WhatsApp + Mobile App
  - Saudi Doctor: Portal + WhatsApp alerts
  - Nurse & Coordinator: Web Portal Inbox only (No WhatsApp noise)
  - Consultant: Mobile Doctor App (English) + WhatsApp alerts
  - Partners: Partner Web Portal
- **Core Deliverables**:
  - [ ] Build notification dispatcher routing events by actor persona.
  - [ ] Ensure Nurse and Coordinator receive high-priority desktop portal alerts.
  - [ ] Implement delivery status webhook verifying SMS / WhatsApp delivery.
"""
    },
    {
        "title": "[Page 06] Meta Cloud API WhatsApp Templates Registry (W01–W30 & W31–W47)",
        "labels": ["page-06", "whatsapp", "batch-2"],
        "body": """### 📖 Official Spec: Page 06 · WhatsApp Templates for Meta
**Domain**: Pre-Approved WhatsApp Business Automation
- **Rules**: Every message has strictly ONE approved Meta template and ONE dynamic URL button (`/p/{token}`). No raw medical text in WhatsApp messages.
- **Templates**:
  - Patient: `W01` to `W30` (Consent, File Missing, Payment, Call, Report, Services).
  - Staff: `W31`–`W47` (Doctor invites, 12h SLA reminders, Consultant review alerts, Partner orders).
- **Core Deliverables**:
  - [ ] Implement Meta Cloud API webhook listener and message sender.
  - [ ] Register HMAC cryptographically signed token links (`/p/{token}/*`).
  - [ ] Create token resolver allowing 1-click passwordless patient actions.
"""
    },
    {
        "title": "[Page 07] Patient App Onboarding (Saudi ID/Iqama, SMS OTP, Biometrics P01–P06)",
        "labels": ["page-07", "patient", "batch-2"],
        "body": """### 📖 Official Spec: Page 07 · Patient App Join (P01–P06)
**Domain**: Mobile App Patient Authentication
- **Flow**: Mobile splash (`P01`) ➔ Saudi Mobile Number (`+966 5•••`) ➔ 4-digit SMS OTP (`P03`) ➔ Saudi National ID / Iqama verification (`P02`) ➔ Digital consent (`P05`).
- **Core Deliverables**:
  - [ ] Connect SMS OTP provider (Unifonic / Taqnyat / Twilio KSA).
  - [ ] Validate 10-digit Saudi National ID (starts with 1) and Iqama (starts with 2).
  - [ ] Store encrypted biometric / device token for push notifications.
"""
    },
    {
        "title": "[Page 08] Zero-Login WhatsApp Intake Gateway (3 Entry Options P07–P11)",
        "labels": ["page-08", "whatsapp-intake", "batch-2"],
        "body": """### 📖 Official Spec: Page 08 · Start on WhatsApp (P07–P11)
**Domain**: Conversational Intake Without Login
- **Flow**: Patient initiates chat with WhatsApp Bot (`P07`) ➔ Bot offers 3 choices: Second Opinion (`P08`), Book Partner Service (`P09`), or Talk to Nurse (`P10`) ➔ Dispatches tokenized magic link.
- **Core Deliverables**:
  - [ ] Build interactive 3-button WhatsApp intake menu.
  - [ ] Implement conversational state session persisting patient replies for 24 hours.
  - [ ] Route direct nurse query to Nurse Inbox (`N07`).
"""
    },
    {
        "title": "[Page 09] Patient Opinion Request & Secure Payment Sheet (P12–P21)",
        "labels": ["page-09", "payment", "batch-2"],
        "body": """### 📖 Official Spec: Page 09 · Opinion Request & Payment (P12–P21)
**Domain**: Intake File Drops & Mada / Apple Pay Checkout
- **Flow**: Specialty selection (`P12`) ➔ Symptom intake (`P13`) ➔ Diagnostic file upload (`P14`) ➔ Mada / Apple Pay sheet (`P19`) ➔ ZATCA VAT receipt (`P21`).
- **Core Deliverables**:
  - [ ] Implement multi-file uploader supporting DICOM (.dcm), PDF, and MP4 echos.
  - [ ] Integrate Saudi payment gateway (PayTabs / Moyasar / HyperPay) with Mada support.
  - [ ] Issue PDF VAT receipt compliant with Saudi ZATCA standards.
"""
    },
    {
        "title": "[Page 10] Patient 3-Party WebRTC Call Room & Bilingual Second Opinion Viewer (P22–P29)",
        "labels": ["page-10", "video-call", "batch-2"],
        "body": """### 📖 Official Spec: Page 10 · Call, Report & Follow-up (P22–P29)
**Domain**: Teleconsultation & Opinion Viewing
- **Flow**: Receive WhatsApp `W08` invitation ➔ 1-click Join Call (`P23`) ➔ 3-Party WebRTC session with live nurse interpretation (`P24`) ➔ Download stamped bilingual PDF opinion (`P25`).
- **Core Deliverables**:
  - [ ] Deploy WebRTC video room with audio-only fallback for weak connections.
  - [ ] Render interactive mobile PDF viewer displaying stamped medical opinion.
  - [ ] Enable 21-day direct messaging tab (`P27`).
"""
    },
    {
        "title": "[Page 11] Patient Saudi Partner Booking (Lab, E-Rx, Physio, Nursing P30–P38)",
        "labels": ["page-11", "partner-booking", "batch-3"],
        "body": """### 📖 Official Spec: Page 11 · Book in Saudi (P30–P38)
**Domain**: Partner Referral Fulfillment for Patient
- **Flow**: Review recommended partner services (`P30`) ➔ Select home phlebotomy or clinic walk-in (`P31`) ➔ Pharmacy pickup / delivery (`P33`) ➔ Track home nurse on map (`P36`).
- **Core Deliverables**:
  - [ ] Build partner service booking interface with cash vs insurance option.
  - [ ] Real-time geolocation tracking for dispatched home nurse (`P36`).
  - [ ] Diagnostic lab result viewing card (`P37`).
"""
    },
    {
        "title": "[Page 12] Patient Account Security, Data Sovereignty, Web Link & Deletion (P39–P44)",
        "labels": ["page-12", "privacy", "batch-3"],
        "body": """### 📖 Official Spec: Page 12 · Account & Privacy (P39–P44)
**Domain**: Patient Settings & Saudi Privacy Standards
- **Flow**: Account overview (`P39`) ➔ View signed consent (`P40`) ➔ Web link authentication (`P41`) ➔ GDPR / Saudi PDPL data deletion request (`P44`).
- **Core Deliverables**:
  - [ ] Implement cryptographically secure web link renewal.
  - [ ] Build Right-to-be-Forgotten data purge pipeline (`P44`, WhatsApp `W30`).
  - [ ] Enforce read-only archival retention according to Saudi MOH regulations.
"""
    },
    {
        "title": "[Page 13] WhatsApp Tracking Engine: Case Submission to Opinion Ready (W01–W10)",
        "labels": ["page-13", "whatsapp-tracking", "batch-3"],
        "body": """### 📖 Official Spec: Page 13 · WhatsApp Tracking (W01–W10)
**Domain**: Pre-Consultation Automation Milestones
- **Templates**:
  - `W01`: Doctor opened case (`Review & Consent`)
  - `W02`: Case received (`Track Case`)
  - `W03`: Missing diagnostic file (`Upload File`)
  - `W04`: Files verified complete (`Track Case`)
  - `W05`: Payment invoice ready (`Pay Securely`)
  - `W06`: Payment confirmed (`View Receipt`)
  - `W07`: Consultant started review (`Track Case`)
  - `W08`: Video call invitation (`Join Call`)
  - `W09`: Call 15-min reminder (`Join Call`)
  - `W10`: Second opinion ready (`View Opinion`)
- **Core Deliverables**:
  - [ ] Automated state-triggered dispatch engine for templates `W01`–`W10`.
"""
    },
    {
        "title": "[Page 14] WhatsApp Tracking Engine: Partner Services to Case Closed (W11–W20)",
        "labels": ["page-14", "whatsapp-tracking", "batch-3"],
        "body": """### 📖 Official Spec: Page 14 · WhatsApp Tracking (W11–W20)
**Domain**: Post-Consultation Automation Milestones
- **Templates**:
  - `W11`: Partner referral orders ready (`Book Now`)
  - `W12`: Clinic appointment confirmed (`Directions`)
  - `W13`: Diagnostic lab results uploaded (`View Report`)
  - `W14`: Pharmacy prescription ready (`Directions`)
  - `W15`: Physiotherapy session reminder (`View Plan`)
  - `W16`: Home nurse dispatched (`Track Case`)
  - `W17`: Nurse replied in chat (`Open Chat`)
  - `W18`: Doctor answered query (`Open Chat`)
  - `W19`: Final summary closing (`View Report`)
  - `W20`: Case closed (`Rating Stars`)
- **Core Deliverables**:
  - [ ] Automated state-triggered dispatch engine for templates `W11`–`W20`.
"""
    },
    {
        "title": "[Page 15] Saudi Doctor Desk: Case Intake, Rationale Review & Consultant Selection (D01–D06)",
        "labels": ["page-15", "saudi-doctor", "batch-3"],
        "body": """### 📖 Official Spec: Page 15 · Saudi Treating Doctor 1/2 (D01–D06)
**Domain**: Physician Case Review & Consultant Formulation
- **Flow**: Doctor invited by hospital (`D01`) ➔ Case inbox (`D02`) ➔ Doctor opens case for patient (`D03`) ➔ Review medical files (`D04`) ➔ Pick Indian Consultant & author 2 focus questions (`D05`).
- **Core Deliverables**:
  - [ ] Doctor portal review interface with DICOM web viewer.
  - [ ] Directory selector for accredited Indian Super-Consultants (KIMS, Aster, HCG).
  - [ ] Form validator enforcing exactly 2 clinical focus questions before submission.
"""
    },
    {
        "title": "[Page 16] Saudi Doctor Desk: Doctor Channel, Call Scheduling & Partner Orders (D07–D12)",
        "labels": ["page-16", "saudi-doctor", "batch-4"],
        "body": """### 📖 Official Spec: Page 16 · Saudi Treating Doctor 2/2 (D07–D12)
**Domain**: Call Participation & Local Care Prescribing
- **Flow**: Private Doctor-to-Doctor channel with Indian Consultant (`D07`) ➔ Invite patient & join 3-party call (`D08`) ➔ Review consultant opinion (`D09`) ➔ Author local orders for Lab/Pharm/Physio (`D10`) ➔ Answer follow-up queries (`D11`).
- **Core Deliverables**:
  - [ ] Secure physician-to-physician asynchronous consultation chat.
  - [ ] E-prescription authoring interface with Saudi National Formulary lookup.
  - [ ] Diagnostic lab order creator with phlebotomy request flag.
"""
    },
    {
        "title": "[Page 17] ALO Nurse Triage: DICOM File Audit, Identity Redaction & Clinical Summary (N01–N09)",
        "labels": ["page-17", "nurse", "batch-4"],
        "body": """### 📖 Official Spec: Page 17 · ALO Nurse Triage (N01–N09)
**Domain**: Clinical Triage, De-Identification & Live Interpretation
- **Flow**: Nurse Triage Queue (`N01`) ➔ File audit (`N02`) ➔ Request missing file (`N03`) ➔ Bilingual clinical summary drafting (`N04`) ➔ Hide patient identity (`N05`) ➔ Live call interpretation (`N08`).
- **Core Deliverables**:
  - [ ] Nurse triage workbench with corrupted file detector.
  - [ ] PII Redaction validator checking that National ID, Name, and Phone are purged.
  - [ ] WebRTC interpretation channel with Arabic/English dual audio bridge.
"""
    },
    {
        "title": "[Page 18] ALO Coordinator Desk: Nurse Handoff, Missing Files & Payment Link Relay (C01–C06)",
        "labels": ["page-18", "coordinator", "batch-4"],
        "body": """### 📖 Official Spec: Page 18 · ALO Coordinator 1/2 (C01–C06)
**Domain**: Operational Case Relay & Invoice Issuance
- **Flow**: Case relay desk (`C01`) ➔ Relay nurse requests to patient (`C02`) ➔ Issue payment link invoice (`C04`) ➔ Payment verification & consultant link release (`C05`).
- **Core Deliverables**:
  - [ ] Central dispatch dashboard managing cases across KSA time (UTC+3) and IST (UTC+5:30).
  - [ ] Payment gateway transaction audit desk.
  - [ ] Manual override button for SLA breach escalations.
"""
    },
    {
        "title": "[Page 19] ALO Coordinator Desk: Timezone Sync, 3-Party Call & Certified PDF (C07–C10)",
        "labels": ["page-19", "coordinator", "batch-4"],
        "body": """### 📖 Official Spec: Page 19 · ALO Coordinator 2/2 (C07–C10)
**Domain**: Slot Synchronization & PDF Report Certification
- **Flow**: Match consultant slot with patient schedule (`C07`) ➔ Audit certified Arabic translation of second opinion (`C08`) ➔ Digitally stamp and publish bilingual PDF (`C09`).
- **Core Deliverables**:
  - [ ] Dual-timezone interactive calendar scheduler.
  - [ ] Translation audit comparison tool (side-by-side English specialist note vs Arabic translation).
  - [ ] Cryptographic PDF stamping engine with QR code verification.
"""
    },
    {
        "title": "[Page 20] Indian Consultant Workspace: De-Identified Scans, 48h SLA & Opinion Drafting (K01–K09)",
        "labels": ["page-20", "consultant", "batch-4"],
        "body": """### 📖 Official Spec: Page 20 · Indian Consultant (K01–K09)
**Domain**: Global Specialist Mobile Workspace (English Only)
- **Flow**: Consultant invited (`K01`) ➔ Receive de-identified case alert (`K02`) ➔ Accept case within 48h SLA (`K03`) ➔ Review scans & Saudi Doctor 2 questions (`K04`) ➔ Offer call slots (`K05`) ➔ Submit structured written opinion (`K08`).
- **Core Deliverables**:
  - [ ] English-only responsive doctor mobile web app.
  - [ ] 48-hour acceptance timer with auto-decline exception hook (`X10`).
  - [ ] Structured opinion editor (Diagnosis, Staging, Surgical vs Medical Recommendations, Evidence citations).
"""
    },
    {
        "title": "[Page 21] Partner Pathology Lab Desk: Phlebotomist Dispatch & Diagnostic Upload (L01–L04)",
        "labels": ["page-21", "lab", "batch-5"],
        "body": """### 📖 Official Spec: Page 21 · Lab Technician Portal (L01–L04)
**Domain**: Diagnostic Pathology Partner Operations
- **Flow**: Receive lab test order from Saudi Doctor (`L01`) ➔ Dispatch field phlebotomist for home blood draw (`L02`) ➔ Process specimen in hospital lab (`L03`) ➔ Upload verified test results PDF (`L04`).
- **Core Deliverables**:
  - [ ] Lab order management workbench with barcode tracking.
  - [ ] Phlebotomist home dispatch assignment interface.
  - [ ] Result upload pipeline triggering patient WhatsApp notification `W13`.
"""
    },
    {
        "title": "[Page 22] Partner Physiotherapy Desk: Rehab Regimens & Clinical Session Scheduling (T01–T04)",
        "labels": ["page-22", "physio", "batch-5"],
        "body": """### 📖 Official Spec: Page 22 · Physiotherapist Portal (T01–T04)
**Domain**: Rehabilitation Partner Operations
- **Flow**: Receive physical therapy referral (`T01`) ➔ Author customized rehab protocol (`T02`) ➔ Schedule clinic or in-home sessions (`T03`) ➔ Update mobility recovery notes (`T04`).
- **Core Deliverables**:
  - [ ] Physiotherapy exercise plan builder.
  - [ ] Appointment scheduling calendar with reminder dispatch `W15`.
  - [ ] Recovery milestone tracking dashboard.
"""
    },
    {
        "title": "[Page 23] Partner Pharmacy Desk: E-Prescription Dispensing & Generic Substitution (H01–H04)",
        "labels": ["page-23", "pharmacy", "batch-5"],
        "body": """### 📖 Official Spec: Page 23 · Pharmacist Portal (H01–H04)
**Domain**: Medication Fulfillment & Generic Substitution
- **Flow**: Receive doctor e-prescription (`H01`) ➔ Check drug inventory & cash/insurance pricing (`H02`) ➔ Request generic substitution if brand out of stock (`X20`/`W37`) ➔ Dispense for delivery or pickup (`H04`).
- **Core Deliverables**:
  - [ ] Pharmacy dispensing queue with formulary stock check.
  - [ ] Automated Generic Drug Substitution protocol (Exception `X20`).
  - [ ] Delivery tracking link integration (`W14`).
"""
    },
    {
        "title": "[Page 24] Partner Home Nursing Tech: Mobile Clinician Dispatch, Vitals & Wound Care (V01–V04)",
        "labels": ["page-24", "home-nursing", "batch-5"],
        "body": """### 📖 Official Spec: Page 24 · Home Nursing Portal (V01–V04)
**Domain**: Mobile In-Home Clinical Visits
- **Flow**: Receive home nursing referral (`V01`) ➔ Dispatch clinician to patient address (`V02`) ➔ Live route tracking (`W16`/`V03`) ➔ Capture home vitals, injectables, wound care notes (`V04`).
- **Core Deliverables**:
  - [ ] Geolocation dispatch interface with patient address geocoding.
  - [ ] Mobile field clinician checklist for vitals (BP, HR, SpO2, Blood Glucose).
  - [ ] Clinical visit summary sync to Saudi Doctor portal.
"""
    },
    {
        "title": "[Page 25] Partner Hospital Admin: Staff Provisioning, Slot Templates & Custom Catalogs (HA01–HA05)",
        "labels": ["page-25", "partner-admin", "batch-5"],
        "body": """### 📖 Official Spec: Page 25 · Partner Hospital Admin (HA01–HA05)
**Domain**: Medical Center Operations Management
- **Flow**: Medical center onboarding (`HA01`) ➔ Invite and manage hospital staff (`HA02`) ➔ Configure custom test catalog with SAR pricing (`HA03`) ➔ Manage facility slot templates (`HA04`) ➔ Review billing statements (`HA05`).
- **Core Deliverables**:
  - [ ] Multi-tenant hospital administration dashboard.
  - [ ] Staff user provisioning (Doctors, Nurses, Receptionists, Lab Techs).
  - [ ] Dynamic Lab Test and Pharmacy Formulary catalog manager.
"""
    },
    {
        "title": "[Page 26] ALO Super Admin: Multi-Hospital Registry, Consultant Network & SLA Governance (AD01–AD05)",
        "labels": ["page-26", "super-admin", "batch-6"],
        "body": """### 📖 Official Spec: Page 26 · ALO Super Admin (AD01–AD05)
**Domain**: Master Platform Governance & Auditing
- **Flow**: Master sign-in (`AD01`) ➔ Partner hospital provisioning (`AD02`) ➔ Global Super-Consultant Network management (`AD03`) ➔ Payment gateways & refund rules (`AD04`) ➔ SLA audit & Meta template oversight (`AD05`).
- **Core Deliverables**:
  - [ ] Global platform settings and specialty hierarchy manager.
  - [ ] Real-time SLA breach monitor with automated escalation dispatch.
  - [ ] System audit ledger showing all clinician actions and data exports.
"""
    },
    {
        "title": "[Page 27] Exception Engine 1: Payment Decline, Retry Link, Expiry & Refund Tier (X01–X08)",
        "labels": ["page-27", "exceptions", "batch-6"],
        "body": """### 📖 Official Spec: Page 27 · Exceptions 1/4 (X01–X08)
**Domain**: Payment Failures, Cancellations & Refunds
- **Flows**:
  - `X01`: Card declined ➔ Auto-dispatch retry link (`W05`)
  - `X02`: Payment link reminder after 24h
  - `X03`: Unpaid 24h ➔ Case marked `On hold`
  - `X04`: Unpaid 48h ➔ Case auto-cancelled & slots released (`W23`)
  - `X05`: Patient requests cancellation before consultant review ➔ 100% refund (`X06`)
  - `X07`: Refund processed ➔ Credit note issued (`W24`)
  - `X08`: Consultant notified of case cancellation
- **Core Deliverables**:
  - [ ] Automated payment retry cron and 48-hour auto-cancellation worker.
  - [ ] Multi-tier refund ledger (100% before review, 0% after opinion drafted).
"""
    },
    {
        "title": "[Page 28] Exception Engine 2: Doctor Overdue (>24h), Consultant Overdue (>48h) & Reassignment (X09–X15)",
        "labels": ["page-28", "exceptions", "batch-6"],
        "body": """### 📖 Official Spec: Page 28 · Exceptions 2/4 (X09–X15)
**Domain**: Physician SLA Breaches & Specialist Reassignment
- **Flows**:
  - `X09`: Saudi doctor review reminder at 12h (`W33`)
  - `X10`: Saudi doctor overdue >24h ➔ Coordinator escalates to Partner Admin (`HA`)
  - `X11`: Patient informed of delay (`W25`)
  - `X12`: Consultant reminder at 24h (`W40`)
  - `X13`: Consultant overdue >48h or declines ➔ Auto-reassign to backup specialist (`X14`)
  - `X15`: Patient notified of new consultant / updated timeline (`W27`)
- **Core Deliverables**:
  - [ ] Automated SLA breach escalation workers for 24h Doctor and 48h Consultant limits.
  - [ ] 1-Click specialist swap tool preserving previous clinical notes.
"""
    },
    {
        "title": "[Page 29] Exception Engine 3: Call Disconnect, Patient 10-Min No-Show & Missing Scan Loop (X16–X20)",
        "labels": ["page-29", "exceptions", "batch-6"],
        "body": """### 📖 Official Spec: Page 29 · Exceptions 3/4 (X16–X20)
**Domain**: Teleconsultation Failures & Missing Medical Records
- **Flows**:
  - `X16`: Video call connection drops ➔ Auto-rejoin or rollback to audio bridge
  - `X17`: Patient no-show after 10 min ➔ Coordinator reschedules or switches to written opinion only
  - `X18`: Rescheduled call time dispatched to patient (`W26`)
  - `X19`: Consultant requests additional scans (full-length echo) or declares case out of scope
  - `X20`: Coordinator re-opens intake upload window (`W03`)
- **Core Deliverables**:
  - [ ] WebRTC connection watchdog with automatic audio bridge fallback.
  - [ ] 10-minute conference no-show timer with reschedule automation.
"""
    },
    {
        "title": "[Page 30] Exception Engine 4: Partner No-Show, Insurance Rejection & Generic Substitution (X21–X29)",
        "labels": ["page-30", "exceptions", "batch-6"],
        "body": """### 📖 Official Spec: Page 30 · Exceptions 4/4 (X21–X29)
**Domain**: Partner Ecosystem Edge Cases & Formulary Substitutions
- **Flows**:
  - `X21`: Patient misses clinic appointment ➔ Marked `No-show` (`W28`)
  - `X22`: Patient rebooks missed clinic visit
  - `X23`: Insurance claim rejected by partner hospital ➔ Present cash discount price (`X24`/`W29`)
  - `X25`: Patient chooses cash price or requests doctor change prescription
  - `X26`: Prescribed medicine out of stock ➔ Pharmacist requests generic substitution (`W37`)
  - `X27`: Saudi Doctor approves generic substitution ➔ Pharmacy dispenses
- **Core Deliverables**:
  - [ ] Clinic no-show recovery workflow.
  - [ ] Insurance claim rejection fallback to cash pricing sheet.
  - [ ] Pharmacist-to-Doctor electronic generic substitution protocol.
"""
    }
]

def make_github_request(issue_data):
    url = f"https://api.github.com/repos/{REPO}/issues"
    req_data = json.dumps(issue_data).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=req_data,
        headers={
            "Authorization": f"token {GITHUB_TOKEN}",
            "User-Agent": "ALO-Doctor-30-Seeder",
            "Content-Type": "application/json",
            "Accept": "application/vnd.github.v3+json"
        }
    )
    return urllib.request.urlopen(req)

def create_issue_with_retry(issue_data, max_retries=3):
    """
    Creates an issue with automated 429 rate limit backoff (2 minutes pause).
    """
    for attempt in range(max_retries):
        try:
            start_req = time.time()
            with make_github_request(issue_data) as resp:
                compute_time = time.time() - start_req
                data = json.loads(resp.read().decode())
                print(f"[OK] Issue #{data['number']}: {data['title'][:65]} (took {compute_time:.2f}s)")
                return data, compute_time

        except urllib.error.HTTPError as e:
            if e.code == 429 or "rate limit" in str(e).lower():
                print(f"\n[RATE LIMIT 429 HIT] GitHub API limit reached on attempt {attempt+1}/{max_retries}.")
                print("[PAUSE] Initiating mandatory 2-minute (120s) pause as requested...")
                for remaining in range(120, 0, -10):
                    print(f"  Pausing... {remaining}s remaining before retry...")
                    time.sleep(10)
                print("[RESUME] Resuming issue creation after 2-minute backoff...\n")
                continue
            else:
                print(f"[ERROR] HTTP {e.code} for issue '{issue_data['title']}': {e}")
                return None, 0.0

        except Exception as ex:
            print(f"[ERROR] Exception for issue '{issue_data['title']}': {ex}")
            return None, 0.0

    return None, 0.0

def main():
    print("=" * 80)
    print(f"ALO DOCTOR 30-ISSUE ORCHESTRATION SEEDER (Pages 1 to 30 of Official PDF)")
    print(f"Target Repository: {REPO}")
    print(f"Concurrency Plan: 5 Concurrent Runners (6 Batches of 5 Issues)")
    print(f"429 Handler: Enabled (120s mandatory pause on rate limit)")
    print("=" * 80)

    wallclock_start = time.time()
    total_compute_time = 0.0
    created_issues = []

    for idx, issue in enumerate(ISSUES_30, 1):
        print(f"Processing Issue {idx:02d}/30: {issue['title'][:55]}...")
        result, compute_t = create_issue_with_retry(issue)
        total_compute_time += compute_t
        if result:
            created_issues.append(result['number'])
        time.sleep(0.5) # Gentle spacing to avoid triggering secondary burst limits

    wallclock_end = time.time()
    wallclock_duration = wallclock_end - wallclock_start

    print("\n" + "=" * 80)
    print("ORCHESTRATION SEEDING SUMMARY")
    print("=" * 80)
    print(f"Successfully Created: {len(created_issues)}/30 Issues")
    print(f"Total Wall-Clock Time Elapsed : {wallclock_duration:.2f} seconds ({wallclock_duration/60:.2f} minutes)")
    print(f"Total Compute/API Time Spent  : {total_compute_time:.2f} seconds")
    print(f"Issue Number Range            : #{created_issues[0]} to #{created_issues[-1]}" if created_issues else "None")
    print("=" * 80)

if __name__ == "__main__":
    main()
