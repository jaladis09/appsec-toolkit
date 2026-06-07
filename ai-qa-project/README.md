
# AI-Powered QA Pipeline

> Original concept and implementation by Sandeepa Jaladi
> QA Automation Engineer (14 years) | CISSP | CC
> [LinkedIn](https://www.linkedin.com/in/sandeepa-jaladi-b4250966/)

---

## The Problem

Two recurring pain points after 14 years in QA:

**1. Regression blind spot**
When a developer changes code, QA has no visibility into which files and
modules were actually touched. Regression testing becomes guesswork —
you test what you think was affected, not what was actually affected.

**2. Wasted QA cycles**
If a code change is completely irrelevant to the Acceptance Criteria in Jira,
nobody catches it until QA runs tests, hits failures, raises bugs, and sends
it back to dev. A full wasted cycle — every single sprint.

---

## The Solution — Left Shift at PR Level

Validate alignment between business intent and technical implementation
at the PR stage — before a single QA hour is spent.