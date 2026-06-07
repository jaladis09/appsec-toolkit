# AI-Powered QA Pipeline

> Built by Sandeepa Jaladi
> QA Automation Engineer (14 years) | CISSP | CC
> [LinkedIn](https://www.linkedin.com/in/sandeepa-jaladi-b4250966/)

---

## The Problem

Two recurring pain points after 14 years in QA:

**1. Regression blind spot**
When a developer changes code, QA has no visibility into which files and modules were actually touched. Regression testing becomes guesswork — you test what you think was affected, not what was actually affected.

**2. Wasted QA cycles**
If a code change is completely irrelevant to the Acceptance Criteria in Jira, nobody catches it until QA runs tests, hits failures, raises bugs, and sends it back to dev. A full wasted cycle — every single sprint.

---

## The Solution — Left Shift at PR Level

Validate alignment between business intent and technical implementation at the PR stage — before a single QA hour is spent.

---

## How It Works

```
Step 1 — PR Raised in Azure DevOps
        ↓
Pipeline fetches the diff — every file changed, every line modified
Regression question answered immediately: exactly what was touched
        ↓
Step 2 — AI Generates Test Cases from Code
        ↓
PR diff sent to Claude AI
Analyzes actual code changes → generates test cases based on what
technically changed, not what was assumed to change
        ↓
Step 3 — Fetch AC Test Cases from Jira
        ↓
Pipeline pulls Rovo-generated test cases from the linked Jira story
Test cases written from Acceptance Criteria — representing business intent
        ↓
Step 4 — AI Compares Both Sets
        ↓
Claude compares the two sets and identifies:
   → Code changes not covered by any AC test case
   → AC test cases with no corresponding code change
   → Potential regression impact based on files touched
        ↓
Step 5 — Report Before QA
        ↓
Consolidated gap report surfaced before code reaches QA
Teams fix misalignment at the source — zero wasted QA cycles
```

---

## Current Status

| Component | Status |
|-----------|--------|
| Claude API connection | ✅ Complete |
| Secure environment setup | ✅ Complete |
| Jira REST API integration | 🔄 In Progress |
| Azure DevOps REST API | 🔄 In Progress |
| Test case comparison engine | ⬜ Upcoming |
| Report generation | ⬜ Upcoming |

> Jira and Azure DevOps integrations are being developed against business systems and maintained in a private repository.

---

## Stack

| Tool | Purpose |
|------|---------|
| Python 3.12 | Pipeline development |
| Claude API | AI test case generation and comparison |
| Jira REST API | Fetch Rovo test cases from AC |
| Azure DevOps REST API | Fetch PR diffs and impacted files |
| python-dotenv | Secure API key management |

---

## Background
- 14 years QA Automation Engineering
- CISSP | CC — both self-study
- Masters in Information Systems, NJIT (4.0 GPA)
- Transitioning into AI Engineering

[LinkedIn — Sandeepa Jaladi](https://www.linkedin.com/in/sandeepa-jaladi-b4250966/)
