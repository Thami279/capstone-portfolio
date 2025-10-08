# Mentor Clarification – Capstone Portfolio Resubmission

**Student:** Thamsanqa Mngoma (TM25040018010)  
**Date:** 4 October 2025  
**Course:** Software Engineering – Task 20

## Repository URL Correction
- The mentor reviewed `https://github.com/thamymngoma/capstone-portfolio`, which returns 404.  
- The live public repository is `https://github.com/Thami279/capstone-portfolio` (capitalised username). Please verify against this URL.

## Verification Snapshot
- Django dev server: running cleanly at `http://127.0.0.1:8001/`; admin panel reachable.  
- Database: migrations applied; tables (e.g. `portfolio_project`) present and queried without errors.  
- Automated tests: all 9 tests pass locally (`python manage.py test`, ~0.03s).  
- Seed data: 3 projects, 6 services, 3 testimonials, and contact form entries render correctly.  
- Forms & security: contact form submits successfully with CSRF protection; authentication flows confirmed.  
- Documentation & structure: docstrings, Sphinx config, Dockerfile, and project layout reviewed—no outstanding issues.

## Repository Status
- Branch: `main`  
- Latest commit: "Fix database issues and ensure all functionality works correctly"  
- Push status: up to date on GitHub.

**Conclusion:** The portfolio application is feature-complete and stable. All mentor-raised issues are resolved; the project is ready for resubmission using the corrected repository link above.
