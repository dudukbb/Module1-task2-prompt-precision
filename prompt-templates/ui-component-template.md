# UI Component Prompt Template

## EPAM A!Tech Bootcamp — Reusable Precision Prompt Templates

---

## Purpose

Use this template when prompting AI to build a React UI component. Fill in the bracketed placeholders before submitting.

---

## Template

```text
Create a [ComponentName] React component.

Context:
- Framework: React [version]
- Language: TypeScript
- Styling: [Tailwind CSS / CSS Modules / styled-components / plain CSS]
- This component is part of: [authentication flow / dashboard / settings / etc.]

Purpose:
[One sentence describing what this component does and where it is used.]

Props interface:
- [propName]: [TypeScript type] — [required / optional] — [description]
- [propName]: [TypeScript type] — [required / optional] — [description]

UI structure:
- [Element 1: e.g., email input field with label]
- [Element 2: e.g., password input field with show/hide toggle]
- [Element 3: e.g., submit button with loading state]

Behavior requirements:
- [Behavior 1: e.g., disable submit button while request is pending]
- [Behavior 2: e.g., show inline field-level validation errors on blur]
- [Behavior 3: e.g., display top-level API error message below the form]
- [Behavior 4: e.g., redirect to /dashboard on successful submission]

Validation rules (client-side):
- [Field 1]: [validation rule]
- [Field 2]: [validation rule]

Accessibility requirements:
- [Requirement: e.g., all inputs must have associated labels]
- [Requirement: e.g., error messages must use role=alert]

State to manage:
- [State 1: e.g., isLoading boolean for async submit]
- [State 2: e.g., apiError string for server error display]

Success criteria:
- [Condition 1: e.g., form submits with valid data and shows loading state]
- [Condition 2: e.g., invalid input blocks submission and shows inline errors]
- [Condition 3: e.g., API errors are displayed without crashing the component]
```

---

## Usage Notes

* Define all props with TypeScript types — avoid using `any`.
* Describe behavior requirements explicitly to prevent missing edge states.
* Include accessibility requirements for production-oriented components.
* State management scope should be clear: local state vs. lifted state vs. external store.
- States: [loading, error, success]
- Styling: [Tailwind/CSS/styled-components]
- Events: [onClick, onChange, etc.]
- Accessibility: [ARIA labels, keyboard nav]