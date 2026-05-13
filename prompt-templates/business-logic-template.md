# Business Logic Prompt Template

## EPAM A!Tech Bootcamp — Reusable Precision Prompt Templates

---

## Purpose

Use this template when prompting AI to implement a service, use case, or business logic module. Fill in the bracketed placeholders before submitting.

---

## Template

```text
Implement the [FeatureName] business logic as a service module.

Context:
- Language: [TypeScript / Python / Java]
- Runtime: [Node.js version / runtime version]
- Architecture pattern: [controller-service-repository / clean architecture / etc.]
- This module belongs to: [authentication / billing / notifications / etc.]

Responsibility:
[One sentence describing what this module is responsible for and what it is not responsible for.]

Inputs:
- [input1]: [type] — [description]
- [input2]: [type] — [description]

Business rules:
- [Rule 1: the condition and outcome]
- [Rule 2: the condition and outcome]
- [Rule 3: any edge case or guard clause]

Security and validation requirements:
- [Requirement 1: e.g., hash passwords before persistence]
- [Requirement 2: e.g., never expose internal error messages to callers]

Outputs:
- Success: [describe what is returned on success]
- Failure: [describe how errors are surfaced — exceptions, result objects, etc.]

Dependencies:
- [Service or repository this module depends on]
- [External service or library if applicable]

Implementation constraints:
- [Constraint 1: e.g., keep functions pure and testable]
- [Constraint 2: e.g., avoid direct DB access; use repository layer]

Success criteria:
- [Condition 1 that must be true for this module to be considered complete]
- [Condition 2]
- [Condition 3]
```

---

## Usage Notes

* Define responsibility boundaries clearly to avoid logic leaking into the wrong layer.
* List business rules explicitly so the AI does not invent behavior.
* State security requirements in the prompt, not as an afterthought.
* Use success criteria to make the output testable and reviewable.
- [functional requirement 1]
- [functional requirement 2]

Constraints:
- [performance/security/tech constraint]

Success when:
- [measurable outcome]