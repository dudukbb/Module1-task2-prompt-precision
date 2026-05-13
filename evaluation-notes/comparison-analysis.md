# Comparison Analysis

## EPAM A!Tech Bootcamp — Module 1, Task 2: Prompt Precision Lab

---

## Overview

This document compares the three prompt rounds used in the Precision Prompting Lab. The same feature (user authentication system) was prompted at three precision levels to demonstrate the measurable difference in output quality.

---

## Round-by-Round Comparison

### Round 1: Vague Prompt

**Prompt style:** Minimal instruction with no constraints or context.

**AI assumptions introduced:**

* Tech stack selected arbitrarily (Node.js or Firebase assumed)
* Authentication method chosen without instruction (sessions or tokens)
* Password rules applied inconsistently or skipped
* No database schema defined
* No error handling contract
* No API structure

**Ambiguity level:** High

**Security coverage:** Absent

**Confidence for implementation:** 3/10

---

### Round 2: Improved Prompt

**Prompt style:** Clear scope and explicit stack with basic constraints.

**Improvements over Round 1:**

* Tech stack fully declared (React + TypeScript, Node.js + Express, PostgreSQL)
* Email-based login specified
* bcrypt hashing and JWT explicitly required
* Basic validation rules present
* Error handling scenarios listed
* Measurable success criteria introduced

**Remaining ambiguity:**

* No exact runtime versions
* No rate limiting or lock policy
* No response envelope contract
* No database schema constraints
* No performance thresholds

**Ambiguity level:** Low-Medium

**Security coverage:** Baseline

**Confidence for implementation:** 8/10

---

### Round 3: Precise Prompt (Production-Ready)

**Prompt style:** Full technical specification with contracts, constraints, and acceptance criteria.

**Improvements over Round 2:**

* Exact runtime versions specified (React 18, Node.js 20)
* bcrypt cost factor defined (12)
* JWT expiry explicitly set (24 hours)
* Rate limiting and lockout policy defined (5 attempts/hour)
* Standardized JSON response/error envelope required
* Stable error codes defined for frontend branching
* PostgreSQL schema specified with constraints
* Performance threshold set (under 2 seconds)
* Anti-enumeration requirement included
* Testable success criteria covering all flows

**Ambiguity level:** Very Low

**Security coverage:** Detailed

**Confidence for implementation:** 9.5/10

---

## Summary Table

| Dimension | Round 1 | Round 2 | Round 3 |
|---|---|---|---|
| Prompt clarity | Low | Medium-High | Very High |
| Tech stack | None | Defined | Defined with versions |
| Security controls | None | Baseline | Detailed |
| API contract | None | Partial | Full |
| Validation rules | None | Basic | Explicit (client + server) |
| Error handling | None | Basic cases | Full taxonomy |
| Database schema | None | Implied | Explicit constraints |
| Performance targets | None | None | Explicit (under 2s) |
| Success criteria | None | Defined | Comprehensive |
| Confidence score | 3/10 | 8/10 | 9.5/10 |

---

## How Precision Improved Output Quality

* Explicit constraints removed guesswork and reduced interpretation variance.
* Security requirements specified upfront prevented insecure defaults.
* Response and error contracts created consistent frontend-backend alignment.
* Measurable success criteria made output verifiable and testable.
* The progression from Round 1 to Round 3 shows that specificity is the primary driver of implementation reliability.
- Missing security and API details
- Low confidence level

## Round 2
- Added clear requirements
- Added tech stack and JWT authentication
- Reduced ambiguity
- Improved validation and structure

## Round 3
- Production-oriented structure
- Added security constraints
- Defined API schemas and endpoints
- Included consistent error handling
- Much higher implementation confidence

---

## Overall Observation

Prompt precision directly improved:
- output quality
- implementation completeness
- security awareness
- confidence level
- reduction of AI assumptions

The lab demonstrated that precise prompts reduce rework and produce more production-ready outputs.