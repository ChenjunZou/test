import re
from dataclasses import dataclass, field


@dataclass
class ContactForm:
    """Contact form with validation."""

    name: str = ""
    email: str = ""
    subject: str = ""
    message: str = ""
    errors: dict[str, str] = field(default_factory=dict)

    def populate(self, form_data: dict) -> None:
        """Populate form from request data."""
        self.name = form_data.get("name", "").strip()
        self.email = form_data.get("email", "").strip()
        self.subject = form_data.get("subject", "").strip()
        self.message = form_data.get("message", "").strip()
        self.errors = {}

    def validate(self) -> bool:
        """Validate form fields. Returns True if valid."""
        self.errors = {}

        if not self.name:
            self.errors["name"] = "Name is required."
        elif len(self.name) > 100:
            self.errors["name"] = "Name must be 100 characters or fewer."

        if not self.email:
            self.errors["email"] = "Email is required."
        elif not self._is_valid_email(self.email):
            self.errors["email"] = "Please enter a valid email address."

        if not self.subject:
            self.errors["subject"] = "Subject is required."
        elif len(self.subject) > 200:
            self.errors["subject"] = "Subject must be 200 characters or fewer."

        if not self.message:
            self.errors["message"] = "Message is required."
        elif len(self.message) < 10:
            self.errors["message"] = "Message must be at least 10 characters."
        elif len(self.message) > 5000:
            self.errors["message"] = "Message must be 5000 characters or fewer."

        return len(self.errors) == 0

    @staticmethod
    def _is_valid_email(email: str) -> bool:
        """Validate email format."""
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))
