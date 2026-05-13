# Precision Lab: From Vague to Precise Prompts

**Duration:** 30 minutes
**Goal:** Experience how precision transforms AI output quality

---

## Setup (2 minutes)

1. Open your AI tool (GitHub Copilot)
2. Create a scratch file for your prompts and outputs
3. You'll build the SAME feature 3 times with increasing precision

---

## The Feature

**Build a user authentication system** with:
- User login
- User registration
- Password management

That's intentionally vague. You'll add precision each round.

---

## Round 1: Your Natural Baseline (5 minutes)

### Do This:
1. Write how you'd normally prompt AI for this feature (don't overthink)
2. Submit to AI, capture the output
3. Quick review: What did AI assume? What's missing?

### Example Natural Prompts:
- "Create a user authentication system"
- "Build login and registration for a web app"
- "I need user management with passwords"

### Quick Assessment:
```
Round 1 Prompt:
[Your prompt here]

What AI Assumed (that you didn't specify):
- Tech stack: ___________
- Auth method: __________
- Database: _____________
- Password rules: _______
- Error handling: _______

Missing Critical Pieces:
- [ ] Security measures
- [ ] API structure
- [ ] Data validation
- [ ] Error messages
- [ ] Other: __________

Confidence Level: ___/10
```

**Don't spend more than 5 minutes. This is your baseline.**

---

## Round 2: Apply Precision Techniques (10 minutes)

### Do This:
1. Check the **precision-cheatsheet.md** file
2. Pick 3-4 techniques to improve your prompt
3. Rewrite your prompt with these techniques
4. Submit to AI, capture output
5. Compare: What improved from Round 1?

### Recommended Starter Techniques:
- **Be Clear and Direct** - Specify exactly what you want
- **Give Context** - Tell AI the tech stack/constraints
- **Break Down Steps** - Structure the task logically (don't ask for reasoning)
- **Use Examples** - Show the format you want (e.g., error response structure)

### Example Round 2 Prompt:
```
Create user authentication with:

Requirements:
- Email-based login (not username)
- Password: min 8 chars, 1 uppercase, 1 number
- Password reset via email

Tech Stack:
- React + TypeScript frontend
- Node.js/Express backend
- PostgreSQL database

Success Criteria:
- User can register, login, reset password
- Passwords hashed with bcrypt
- Return JWT tokens
```

### Quick Assessment:
```
Techniques Applied:
□ Clear and direct
□ Role/context given
□ Examples provided
□ Steps broken down
□ Tech stack specified

Improvements from Round 1:
- AI no longer assumed: __________
- Now includes: __________
- Better handling of: __________

Confidence Level: ___/10 (was ___/10 in Round 1)
```

---

## Round 3: Maximum Precision (10 minutes)

### Do This:
1. Apply ALL relevant techniques from the cheatsheet
2. Add everything you know: requirements, constraints, errors, formats
3. Make the most comprehensive prompt possible
4. Submit to AI, capture output
5. Compare all 3 rounds

### Additional Elements to Add:
```
Security:
- Bcrypt cost factor 12
- Rate limiting: 5 attempts/hour
- Session expiry: 24 hours

Error Handling:
- Invalid credentials: "Invalid email or password"
- Locked account: "Too many attempts. Try again in 1 hour."
- Network error: "Connection failed. Please try again."

API Structure:
- POST /api/auth/register
- POST /api/auth/login
- POST /api/auth/reset-password

Response Format:
{
  success: boolean,
  data?: { token: string, expiresIn: number },
  error?: { code: string, message: string }
}
```

### Quick Assessment:
```
Additional Techniques Applied:
□ Security requirements
□ Error scenarios
□ API endpoints defined
□ Success criteria
□ Data schemas
□ Performance constraints

Production Readiness:
- [ ] Could deploy as-is
- [ ] Needs minor tweaks only
- [ ] Still needs significant work

Confidence Level: ___/10 (R1: ___/10, R2: ___/10)
```

---

## Compare & Measure

### Quality Assessment

| Metric | Round 1 | Round 2 | Round 3 |
|--------|---------|---------|---------|
| **Prompt Length** | ___ lines | ___ lines | ___ lines |
| **Quality Score** | ___/10 | ___/10 | ___/10 |
| **Assumptions Made by AI** | Many / Some / Few | Many / Some / Few | Many / Some / Few |
| **Rework Needed** | Hours / Minutes / None | Hours / Minutes / None |
| **Production Ready?** | Yes / No | Yes / No | Yes / No |

### Time Investment
- Round 1: 2 min prompt + ___ min fixing = ___ total
- Round 2: 5 min prompt + ___ min fixing = ___ total
- Round 3: 10 min prompt + ___ min fixing = ___ total

### Key Insights
1. Which techniques had the biggest impact?
2. Was the extra precision time worth it?
3. Where would you use this in real work?

---

## The Precision Paradox

**Appears slower:** Writing precise prompts takes more time upfront
**Actually faster:** Less rework, fewer follow-ups, higher confidence

**Example Math:**
- Vague: 2 min prompt + 30 min debugging + 15 min explaining = 47 min
- Precise: 10 min prompt + 5 min verification = 15 min
- **Net savings: 32 minutes**

---

## Apply This Week

Pick ONE real task where you'll apply precision:
- [ ] Writing a Jira story
- [ ] Code review comment
- [ ] Documentation
- [ ] Feature implementation
- [ ] Bug fix
- [ ] Other: ___________

**Commit:** "This week I will apply precision techniques to ___________"

---

## Quick Reference

**See `precision-cheatsheet.md` for:**
- Industry-standard techniques (Anthropic, OpenAI)
- Engineering-specific additions
- Copy-paste examples
- Before/after comparisons

**Remember:** It's not about writing MORE, it's about being SPECIFIC.

---

**End of Lab**
Total time: 25 minutes
Deliverable: 3 prompts showing progression from vague to precise