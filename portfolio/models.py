"""Domain models powering the studio portfolio experience."""

from django.db import models
from django.utils import timezone


class PublishedQuerySet(models.QuerySet):
    """Reusable queryset with helpers for commonly filtered collections."""

    def published(self):
        """Return only entities marked as publishable."""
        return self.filter(is_published=True)

    def featured(self):
        """Return highlighted items that are also published."""
        return self.published().filter(is_featured=True)


class Service(models.Model):
    """A high-level capability offered by the consultancy."""

    title = models.CharField(max_length=150)
    summary = models.TextField()
    is_published = models.BooleanField(default=True)
    display_order = models.PositiveSmallIntegerField(default=0)

    objects = PublishedQuerySet.as_manager()

    class Meta:
        ordering = ["display_order", "title"]

    def __str__(self) -> str:  # pragma: no cover - human readable representation
        return self.title


class Tag(models.Model):
    """A concise descriptor applied to projects for quick filtering."""

    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default="#2b2d42")

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:  # pragma: no cover
        return self.name


class ProjectStatus(models.TextChoices):
    """Lifecycle stages a project can reside in."""

    PLANNING = "planning", "Planning"
    IN_PROGRESS = "in_progress", "In Progress"
    COMPLETE = "complete", "Complete"


class Project(models.Model):
    """A case study detailing a successful client engagement."""

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=250)
    description = models.TextField()
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name="projects")
    client_name = models.CharField(max_length=120)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=ProjectStatus.choices, default=ProjectStatus.PLANNING)
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)
    hero_image = models.ImageField(upload_to="projects", blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name="projects")
    impact_score = models.PositiveSmallIntegerField(default=0)

    objects = PublishedQuerySet.as_manager()

    class Meta:
        ordering = ["-start_date", "title"]

    def __str__(self) -> str:  # pragma: no cover
        return self.title

    @property
    def duration_days(self) -> int:
        """Compute the total days the project has been active."""
        reference = self.end_date or timezone.now().date()
        return (reference - self.start_date).days


class Testimonial(models.Model):
    """Social proof reinforcing the value of a delivered project."""

    client_name = models.CharField(max_length=120)
    client_role = models.CharField(max_length=150)
    quote = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, blank=True, related_name="testimonials")
    is_featured = models.BooleanField(default=False)
    is_published = models.BooleanField(default=True)

    objects = PublishedQuerySet.as_manager()

    class Meta:
        ordering = ["-is_featured", "client_name"]

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.client_name} – {self.client_role}"


class ContactSubmission(models.Model):
    """An inbound request from a prospective client or collaborator."""

    name = models.CharField(max_length=120)
    email = models.EmailField()
    company = models.CharField(max_length=120, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    resolved = models.BooleanField(default=False)
    internal_notes = models.TextField(blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.name} <{self.email}>"
