## Round 3: Precision Prompt (Production-Ready)

---

## Prompt

Build a production-ready user authentication system for a web application with these core capabilities:

* User registration
* User login
* Password management (including reset via email)

Use the following exact technology stack:

* Frontend: React 18 + TypeScript
* Backend: Node.js 20 + Express
* Database: PostgreSQL

### 1. System Context and Architecture Requirements

Implement a full-stack authentication module that can be integrated into a SaaS-style product.

* Frontend responsibility:
	* Collect and validate user input before API submission.
	* Display loading, success, and error states for all auth flows.
	* Persist JWT securely in memory or secure storage strategy appropriate for SPA threat model.
* Backend responsibility:
	* Own all security-critical validation and authentication logic.
	* Issue JWT tokens with clear expiration metadata.
	* Enforce login attempt controls and account lock behavior.
* Database responsibility:
	* Store user identity and credential hashes securely.
	* Enforce uniqueness and integrity constraints.

### 2. Authentication and Security Requirements

Use these exact rules:

* Email-based authentication only.
* JWT authentication for session management.
* JWT session expiration: 24 hours (86400 seconds).
* Password hashing: bcrypt with cost factor 12.
* Rate limiting and lockout:
	* Maximum 5 failed login attempts per hour per account.
	* Return locked-account error when threshold is reached.
* Password reset must be supported via email flow.

Security controls to implement:

* Never store plaintext passwords.
* Do not leak whether email exists during reset-password request.
* Return generic auth failure messages where appropriate to reduce user enumeration risk.
* Validate and sanitize all inputs on backend even if frontend validation passes.
* Use HTTPS-only assumptions for all token and credential transport.

### 3. Validation Rules (Frontend and Backend)

Apply these validation constraints consistently on client and server:

* Email must follow RFC 5322 format.
* Password must include:
	* Minimum 8 characters
	* At least 1 uppercase letter
	* At least 1 number
	* At least 1 special character

Validation behavior expectations:

* Frontend: immediate field-level feedback before submit.
* Backend: authoritative validation with structured error responses.
* Validation errors must be deterministic and machine-readable.

### 4. API Structure and Endpoint Contract

Implement these endpoints exactly:

* `POST /api/auth/register`
* `POST /api/auth/login`
* `POST /api/auth/reset-password`

#### 4.1 `POST /api/auth/register`

Request body:

```json
{
	"email": "user@example.com",
	"password": "StrongPass1!"
}
```

Success behavior:

* Creates user account with unique email.
* Stores bcrypt hash only.
* Returns success response envelope.

Error scenarios:

* Duplicate email
* Invalid validation input
* Internal server error

#### 4.2 `POST /api/auth/login`

Request body:

```json
{
	"email": "user@example.com",
	"password": "StrongPass1!"
}
```

Success behavior:

* Validates credentials.
* Enforces failed-attempt lock policy.
* Returns JWT token and expiry metadata.

Error scenarios:

* Invalid credentials
* Account locked
* Internal server error

#### 4.3 `POST /api/auth/reset-password`

Request body:

```json
{
	"email": "user@example.com"
}
```

Success behavior:

* Triggers password reset email workflow.
* Returns generic success response regardless of account existence.

Error scenarios:

* Invalid email format
* Network timeout (downstream email service)
* Internal server error

### 5. Standardized Response Format

Use a consistent response envelope for all endpoints.

Success example:

```json
{
	"success": true,
	"data": {
		"token": "jwt-token",
		"expiresIn": 86400
	}
}
```

Error example:

```json
{
	"success": false,
	"error": {
		"code": "INVALID_CREDENTIALS",
		"message": "Invalid email or password"
	}
}
```

Response requirements:

* `success` is always present.
* `data` exists only on success.
* `error` exists only on failure.
* `error.code` must be stable and suitable for frontend branching.

### 6. Error Handling Requirements

Implement explicit handling for:

* Invalid credentials
* Account locked
* Duplicate email
* Network timeout
* Internal server error

Operational expectations:

* Map internal exceptions to safe public error messages.
* Log full technical error details server-side without exposing sensitive traces to clients.
* Return appropriate HTTP status codes aligned with error categories.

### 7. Database Schema Requirements

Use PostgreSQL with a `users` table containing:

* `id` (UUID, primary key)
* `email` (unique, indexed, not null)
* `password_hash` (not null)
* `created_at` (timestamp with timezone, not null)
* `updated_at` (timestamp with timezone, not null)

Schema expectations:

* Enforce unique constraint on `email`.
* Store all timestamps in UTC.
* Ensure `updated_at` is updated on credential changes.

### 8. Frontend Requirements

Build React 18 + TypeScript auth flows for:

* Registration form
* Login form
* Password reset request form

UI behavior requirements:

* Client-side validation mirroring backend rules.
* Disabled submit during pending API request.
* Inline field errors and top-level API error display.
* Clear post-success state transitions (for example, redirect after login).

### 9. Backend Requirements

Build Node.js 20 + Express services with:

* Auth routes and controller separation.
* Validation middleware.
* Service layer for auth logic.
* Data access layer for PostgreSQL operations.
* Centralized error middleware.

Implementation quality requirements:

* Keep functions focused and testable.
* Separate transport DTOs from domain logic.
* Use environment-based configuration for JWT secret and runtime settings.

### 10. Performance Constraints

Meet these constraints:

* Authentication API response time under 2 seconds under normal load.
* Secure password storage with bcrypt cost 12.
* Input validation on both frontend and backend.

Performance expectations:

* Avoid blocking operations in request path beyond required bcrypt work.
* Index email lookups for login performance.
* Use efficient error paths to avoid unnecessary DB queries.

### 11. Success Criteria

The implementation is successful only if all conditions below are met:

* User can register with valid email/password and data is persisted correctly.
* Duplicate registration attempts return deterministic duplicate-email error.
* User can login and receive JWT token with 24-hour expiry.
* Failed login attempts are tracked and account lock is enforced after 5 failures per hour.
* Password reset request endpoint is functional and does not reveal account existence.
* Validation rules are enforced consistently on frontend and backend.
* Error responses follow standardized envelope and stable error codes.
* Core authentication flows return within 2 seconds under expected baseline load.

---

## Detailed Evaluation

### Comparison with Round 1

Round 1 was broad and ambiguous. It lacked implementation boundaries, security constraints, API contracts, and measurable outcomes.

Key upgrades in Round 3 versus Round 1:

* From generic request to concrete, enforceable engineering specification.
* From implicit assumptions to explicit stack and architecture definitions.
* From undefined behavior to defined validation, error, and response contracts.
* From no success metric to clear pass/fail acceptance criteria.

### Comparison with Round 2

Round 2 introduced useful specificity but remained mid-level. Round 3 adds production precision by defining non-negotiable technical parameters and operational expectations.

Key upgrades in Round 3 versus Round 2:

* Adds exact runtime versions (React 18, Node.js 20).
* Adds strict crypto requirement (bcrypt cost factor 12).
* Adds quantifiable rate limiting and lock behavior (5 failed logins per hour).
* Adds explicit response envelope contracts and stable error code expectations.
* Adds schema-level constraints and timestamp behavior.
* Adds performance SLO (under 2 seconds) and implementation-level quality constraints.

### Why This Is More Production-Ready

This prompt is production-ready because it minimizes ambiguity in security, API behavior, validation, persistence, and non-functional requirements.

It improves implementation reliability by:

* Reducing interpretation variance across engineers and AI generations.
* Translating business intent into verifiable acceptance criteria.
* Explicitly addressing common real-world auth risks (enumeration, lockouts, secure hashing, structured errors).
* Defining a predictable contract between frontend and backend teams.

### Confidence Score

> **9.5/10** - High confidence for implementation, testing, and handoff readiness, with only environment-specific deployment details left to finalize.
