from datetime import date, timedelta

from django.test import TestCase

from portfolio.models import ContactSubmission, Project, ProjectStatus, Service, Testimonial


class ProjectModelTests(TestCase):
    def setUp(self):
        self.service = Service.objects.create(title="Product Strategy", summary="Guide roadmaps with clarity.")

    def test_duration_days_uses_end_date_when_available(self):
        project = Project.objects.create(
            title="AI Enablement",
            slug="ai-enablement",
            summary="Scaled ML workflows.",
            description="Helping the team adopt accelerated experimentation.",
            service=self.service,
            client_name="Synth Labs",
            start_date=date(2024, 1, 1),
            end_date=date(2024, 2, 1),
            status=ProjectStatus.COMPLETE,
        )
        self.assertEqual(project.duration_days, 31)

    def test_duration_days_defaults_to_today_when_incomplete(self):
        project = Project.objects.create(
            title="Design Ops",
            slug="design-ops",
            summary="Unified design operations.",
            description="Establish holistic design practice.",
            service=self.service,
            client_name="Northwind Labs",
            start_date=date.today() - timedelta(days=10),
            status=ProjectStatus.IN_PROGRESS,
        )
        self.assertEqual(project.duration_days, 10)


class PublishedQuerySetTests(TestCase):
    def test_featured_and_published_filters(self):
        service = Service.objects.create(title="Engineering Leadership", summary="Run elite delivery teams.")
        primary = Project.objects.create(
            title="Payments Platform",
            slug="payments-platform",
            summary="Modernised checkout",
            description="Built a scalable checkout experience.",
            service=service,
            client_name="Acme Corp",
            start_date=date.today() - timedelta(days=30),
            end_date=date.today(),
            status=ProjectStatus.COMPLETE,
            is_featured=True,
        )
        secondary = Project.objects.create(
            title="Brand Refresh",
            slug="brand-refresh",
            summary="Elevated brand systems.",
            description="Repositioned the brand for enterprise sales.",
            service=service,
            client_name="Acme Corp",
            start_date=date.today() - timedelta(days=60),
            end_date=date.today(),
            status=ProjectStatus.COMPLETE,
            is_published=False,
        )
        highlighted = Project.objects.featured()
        self.assertIn(primary, highlighted)
        self.assertNotIn(secondary, highlighted)

    def test_testimonial_manager_returns_only_published_items(self):
        service = Service.objects.create(title="Analytics", summary="Insights at scale.")
        project = Project.objects.create(
            title="Insight Engine",
            slug="insight-engine",
            summary="Data-lake insights.",
            description="Built a unified analytics engine.",
            service=service,
            client_name="Futura",
            start_date=date.today(),
        )
        visible = Testimonial.objects.create(
            client_name="Jesse", client_role="CTO", quote="Outstanding velocity.", project=project
        )
        Testimonial.objects.create(
            client_name="Morgan", client_role="COO", quote="Transformed delivery.", project=project, is_published=False
        )
        self.assertQuerySetEqual(Testimonial.objects.published(), [visible], transform=lambda x: x)


class ContactSubmissionTests(TestCase):
    def test_string_representation_is_informative(self):
        submission = ContactSubmission.objects.create(
            name="Ava",
            email="ava@example.com",
            message="We need a partner for a high-stakes product launch roadmap.",
        )
        self.assertIn("Ava", str(submission))
        self.assertIn("ava@example.com", str(submission))
