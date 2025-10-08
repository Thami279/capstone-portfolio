from datetime import date

from django.test import TestCase
from django.urls import reverse

from portfolio.models import ContactSubmission, Project, ProjectStatus, Service, Testimonial


class HomePageViewTests(TestCase):
    def setUp(self):
        self.service = Service.objects.create(title="Product Discovery", summary="Shape the roadmap.")
        self.project = Project.objects.create(
            title="Workflow Automation",
            slug="workflow-automation",
            summary="Automated mission-critical ops.",
            description="Delivered a modern automation platform.",
            service=self.service,
            client_name="Orbit",
            start_date=date(2023, 5, 1),
            end_date=date(2023, 9, 1),
            status=ProjectStatus.COMPLETE,
            is_featured=True,
        )
        self.testimonial = Testimonial.objects.create(
            client_name="Jordan",
            client_role="VP Engineering",
            quote="Changed the way we ship.",
            project=self.project,
            is_featured=True,
        )

    def test_homepage_renders_expected_context(self):
        response = self.client.get(reverse("portfolio:home"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.project, response.context["featured_projects"])
        self.assertIn(self.service, response.context["services"])
        self.assertIn(self.testimonial, response.context["testimonials"])
        self.assertEqual(
            response.context["metrics"],
            {
                "projects": 1,
                "clients": 1,
                "testimonials": 1,
            },
        )

    def test_successful_contact_submission_creates_record_and_redirects(self):
        payload = {
            "name": "Taylor",
            "email": "taylor@example.com",
            "company": "Aurora",
            "message": "We would love guidance on scaling our data platform responsibly.",
        }
        response = self.client.post(reverse("portfolio:home"), payload, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(ContactSubmission.objects.filter(email="taylor@example.com").exists())
        messages = list(response.context["messages"])
        self.assertTrue(any("Thanks for reaching out" in str(message) for message in messages))

    def test_invalid_contact_submission_shows_errors(self):
        payload = {
            "name": "Mo",
            "email": "mo@example.com",
            "message": "Too short",
        }
        response = self.client.post(reverse("portfolio:home"), payload)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please provide enough detail")
        self.assertFalse(ContactSubmission.objects.exists())
