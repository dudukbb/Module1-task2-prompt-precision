# API Endpoint Prompt Template

## EPAM A!Tech Bootcamp — Reusable Precision Prompt Templates

---

## Purpose

Use this template when prompting AI to implement a backend API endpoint. Fill in the bracketed placeholders before submitting.

---

## Template

```text
Implement a [METHOD] /api/[path] endpoint for a [framework] backend.

Context:
- Application type: [SaaS / internal tool / public API]
- Runtime: [Node.js version / Python version]
- Framework: [Express / Fastify / Django / etc.]
- Database: [PostgreSQL / MongoDB / etc.]

Purpose:
[One sentence describing what this endpoint does and why it exists.]

Request contract:
- Method: [GET / POST / PUT / PATCH / DELETE]
- Path: /api/[resource]/[optional-sub-path]
- Auth required: [yes / no]
- Content-Type: application/json
- Request body:
  {
    "field1": "type and description",
    "field2": "type and description"
  }

Validation rules:
- [field1]: [required / optional], [validation constraint]
- [field2]: [required / optional], [validation constraint]

Business logic:
- [Step 1: what the endpoint does first]
- [Step 2: what it does next]
- [Step 3: what it returns on success]

Response contract:
- Success (HTTP [status]):
  {
    "success": true,
    "data": { ... }
  }
- Error (HTTP [status]):
  {
    "success": false,
    "error": {
      "code": "[STABLE_CODE]",
      "message": "[Human-readable message]"
    }
  }

Error scenarios to handle:
- [Scenario 1 and expected response code]
- [Scenario 2 and expected response code]

Success criteria:
- [Condition 1 that must be true for the endpoint to be considered complete]
- [Condition 2]
```

---

## Usage Notes

* Always specify runtime versions and framework.
* Define validation rules explicitly — do not rely on AI defaults.
* Use stable error codes so the frontend can branch on them reliably.
* Include all error scenarios that are known at prompt time.
- Auth: [required/optional/none]
- Request: [body/params structure]
- Response 200: [success structure]
- Response 4XX: [error cases]
- Stack: [language/framework]