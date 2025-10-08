"""High-level views that orchestrate the storytelling experience."""

from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from .forms import ContactSubmissionForm
from .models import ContactSubmission, Project, Service, Testimonial


class HomePageView(FormView):
    """Hero landing page mixing insights, case studies, and lead capture."""

    template_name = "portfolio/home.html"
    form_class = ContactSubmissionForm
    success_url = reverse_lazy("portfolio:home")

    def get_context_data(self, **kwargs):
        """Inject curated content slices that power the homepage layout."""
        context = super().get_context_data(**kwargs)
        context.update(
            {
                "featured_projects": Project.objects.featured()[:3],
                "services": Service.objects.published()[:6],
                "testimonials": Testimonial.objects.featured()[:3],
                "metrics": self._build_metrics(),
            }
        )
        return context

    def form_valid(self, form):
        """Persist a new contact submission and share a reassuring toast."""
        ContactSubmission.objects.create(**form.cleaned_data)
        messages.success(self.request, "Thanks for reaching out. We will respond within one business day.")
        return super().form_valid(form)

    def form_invalid(self, form):
        """Return the form with helpful inline feedback when validation fails."""
        messages.error(self.request, "We could not submit your message. Please correct the errors below.")
        return super().form_invalid(form)

    def _build_metrics(self):
        """Aggregate lightweight business metrics to surface in the UI."""
        return {
            "projects": Project.objects.published().count(),
            "clients": Project.objects.published().values("client_name").distinct().count(),
            "testimonials": Testimonial.objects.published().count(),
        }


def health_view(_request):
    """Lightweight liveness probe that avoids database access."""
    return JsonResponse({"status": "ok"}, status=200)
