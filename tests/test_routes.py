class TestHomePage:
    def test_home_returns_200(self, client):
        response = client.get("/")
        assert response.status_code == 200

    def test_home_contains_welcome(self, client):
        response = client.get("/")
        assert b"Welcome" in response.data

    def test_home_contains_recent_posts(self, client):
        response = client.get("/")
        assert b"Deploying Web Apps" in response.data


class TestAboutPage:
    def test_about_returns_200(self, client):
        response = client.get("/about")
        assert response.status_code == 200

    def test_about_contains_profile_name(self, client):
        response = client.get("/about")
        assert b"Pierre" in response.data

    def test_about_contains_skills(self, client):
        response = client.get("/about")
        assert b"Python" in response.data


class TestBlogPage:
    def test_blog_returns_200(self, client):
        response = client.get("/blog")
        assert response.status_code == 200

    def test_blog_contains_posts(self, client):
        response = client.get("/blog")
        assert b"Deploying Web Apps" in response.data

    def test_blog_pagination(self, client):
        response = client.get("/blog?page=1&per_page=2")
        assert response.status_code == 200
        assert b"Page 1 of 2" in response.data


class TestBlogPostPage:
    def test_existing_post_returns_200(self, client):
        response = client.get("/blog/welcome-to-my-blog")
        assert response.status_code == 200
        assert b"Welcome to My Blog" in response.data

    def test_nonexistent_post_returns_404(self, client):
        response = client.get("/blog/nonexistent-post")
        assert response.status_code == 404
        assert b"Not Found" in response.data


class TestContactPage:
    def test_contact_get_returns_200(self, client):
        response = client.get("/contact")
        assert response.status_code == 200
        assert b"Contact" in response.data

    def test_contact_valid_submission(self, client):
        response = client.post("/contact", data={
            "name": "Test User",
            "email": "test@example.com",
            "subject": "Test Subject",
            "message": "This is a test message that is long enough.",
        }, follow_redirects=True)
        assert response.status_code == 200
        assert b"Thank you" in response.data

    def test_contact_invalid_submission(self, client):
        response = client.post("/contact", data={
            "name": "",
            "email": "invalid",
            "subject": "",
            "message": "",
        })
        assert response.status_code == 200
        assert b"correct the errors" in response.data

    def test_contact_missing_fields(self, client):
        response = client.post("/contact", data={})
        assert response.status_code == 200
