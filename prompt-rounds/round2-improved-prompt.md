## Round 2: Improved Prompt Example

### Prompt
Build a user authentication system for a web application.

Use this exact tech stack:

* Frontend: React + TypeScript
* Backend: Node.js + Express
* Database: PostgreSQL

Context:

* This is a foundational auth module for a production-oriented SaaS-style app.
* Users must be able to register, log in, and manage their password safely.
* Login must be email-based.

Feature requirements:

* Registration endpoint and UI flow that accepts email and password.
* Login endpoint and UI flow using email and password.
* Password management flow that supports password update for authenticated users.
* Passwords must be hashed with bcrypt before storing in PostgreSQL.
* Use JWT for authentication after successful login.
* Include basic error handling for common cases:
	* duplicate email on registration
	* invalid login credentials
	* missing required fields
	* expired or invalid JWT

Implementation expectations:

* Define backend API endpoints clearly (method + route + purpose).
* Use request/response JSON consistently across frontend and backend.
* Add minimal input validation for email format and password presence.
* Keep code modular and readable (separate routes, controllers/services, and DB access).

### Success Criteria

* A user can register with email and password, and the password is stored as a bcrypt hash.
* A registered user can log in with valid credentials and receives a JWT.
* Authenticated users can update their password successfully.
* Invalid credentials and invalid/expired tokens return clear error responses.
* Frontend can complete registration, login, and password update flows against the backend API.

---

### Quick Analysis

**What improved compared to Round 1:**

* The prompt now defines a concrete tech stack, architecture direction, and authentication approach.
* It includes explicit functional scope (registration, login, password update).
* It adds implementation constraints and expected behaviors for errors and API structure.
* It introduces measurable success criteria instead of a generic request.

**What assumptions were reduced:**

* No guesswork about frontend/backend/database technologies.
* No ambiguity on login mechanism (email-based).
* No ambiguity on password security approach (bcrypt).
* No ambiguity on auth session strategy (JWT).
* Fewer assumptions around expected failure handling and delivery quality.

**Confidence level:**

8/10 (good for implementation planning and first-pass delivery, with only minor details left for refinement)
