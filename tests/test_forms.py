from app.forms import ContactForm


class TestContactForm:
    def test_valid_form(self):
        form = ContactForm()
        form.populate({
            "name": "John Doe",
            "email": "john@example.com",
            "subject": "Hello",
            "message": "This is a test message that is long enough.",
        })
        assert form.validate() is True
        assert form.errors == {}

    def test_empty_name(self):
        form = ContactForm()
        form.populate({
            "name": "",
            "email": "john@example.com",
            "subject": "Hello",
            "message": "This is a valid message.",
        })
        assert form.validate() is False
        assert "name" in form.errors

    def test_name_too_long(self):
        form = ContactForm()
        form.populate({
            "name": "x" * 101,
            "email": "john@example.com",
            "subject": "Hello",
            "message": "This is a valid message.",
        })
        assert form.validate() is False
        assert "100 characters" in form.errors["name"]

    def test_empty_email(self):
        form = ContactForm()
        form.populate({
            "name": "John",
            "email": "",
            "subject": "Hello",
            "message": "This is a valid message.",
        })
        assert form.validate() is False
        assert "email" in form.errors

    def test_invalid_email_format(self):
        form = ContactForm()
        form.populate({
            "name": "John",
            "email": "not-an-email",
            "subject": "Hello",
            "message": "This is a valid message.",
        })
        assert form.validate() is False
        assert "valid email" in form.errors["email"]

    def test_valid_email_formats(self):
        valid_emails = [
            "user@example.com",
            "user.name@domain.co",
            "user+tag@sub.domain.org",
        ]
        for email in valid_emails:
            form = ContactForm()
            form.populate({
                "name": "John",
                "email": email,
                "subject": "Test",
                "message": "A valid message here.",
            })
            assert form.validate() is True, f"Failed for {email}"

    def test_empty_subject(self):
        form = ContactForm()
        form.populate({
            "name": "John",
            "email": "john@example.com",
            "subject": "",
            "message": "This is a valid message.",
        })
        assert form.validate() is False
        assert "subject" in form.errors

    def test_subject_too_long(self):
        form = ContactForm()
        form.populate({
            "name": "John",
            "email": "john@example.com",
            "subject": "x" * 201,
            "message": "This is a valid message.",
        })
        assert form.validate() is False
        assert "200 characters" in form.errors["subject"]

    def test_empty_message(self):
        form = ContactForm()
        form.populate({
            "name": "John",
            "email": "john@example.com",
            "subject": "Hello",
            "message": "",
        })
        assert form.validate() is False
        assert "message" in form.errors

    def test_message_too_short(self):
        form = ContactForm()
        form.populate({
            "name": "John",
            "email": "john@example.com",
            "subject": "Hello",
            "message": "short",
        })
        assert form.validate() is False
        assert "at least 10" in form.errors["message"]

    def test_message_too_long(self):
        form = ContactForm()
        form.populate({
            "name": "John",
            "email": "john@example.com",
            "subject": "Hello",
            "message": "x" * 5001,
        })
        assert form.validate() is False
        assert "5000 characters" in form.errors["message"]

    def test_populate_strips_whitespace(self):
        form = ContactForm()
        form.populate({
            "name": "  John  ",
            "email": "  john@example.com  ",
            "subject": "  Hello  ",
            "message": "  This is a valid message.  ",
        })
        assert form.name == "John"
        assert form.email == "john@example.com"
        assert form.subject == "Hello"
        assert form.message == "This is a valid message."

    def test_populate_handles_missing_keys(self):
        form = ContactForm()
        form.populate({})
        assert form.name == ""
        assert form.email == ""

    def test_multiple_errors(self):
        form = ContactForm()
        form.populate({
            "name": "",
            "email": "",
            "subject": "",
            "message": "",
        })
        assert form.validate() is False
        assert len(form.errors) == 4
