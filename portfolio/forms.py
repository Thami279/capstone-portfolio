"""Form objects that translate user intent into validated data."""

from django import forms

from .models import ContactSubmission


class ContactSubmissionForm(forms.ModelForm):
    """Capture the essential details we need before a project kickoff call."""

    class Meta:
        model = ContactSubmission
        fields = ["name", "email", "company", "message"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }

    def clean_message(self):
        """Encourage meaningful briefs so the team can craft a valuable response."""
        message = self.cleaned_data["message"]
        if len(message.strip()) < 20:
            raise forms.ValidationError("Please provide enough detail so we can respond meaningfully.")
        return message
