from datetime import datetime

from app.models import BlogPost, Profile


class TestBlogPost:
    def setup_method(self):
        """Reset the store before each test."""
        if hasattr(BlogPost, "_store"):
            del BlogPost._store

    def test_get_all_returns_sorted_posts(self):
        posts = BlogPost.get_all()
        assert len(posts) == 4
        # Should be sorted newest first
        for i in range(len(posts) - 1):
            assert posts[i].published_at >= posts[i + 1].published_at

    def test_get_recent_default_limit(self):
        posts = BlogPost.get_recent()
        assert len(posts) == 3

    def test_get_recent_custom_limit(self):
        posts = BlogPost.get_recent(limit=2)
        assert len(posts) == 2

    def test_get_recent_limit_exceeds_count(self):
        posts = BlogPost.get_recent(limit=100)
        assert len(posts) == 4

    def test_get_by_slug_found(self):
        post = BlogPost.get_by_slug("welcome-to-my-blog")
        assert post is not None
        assert post.title == "Welcome to My Blog"

    def test_get_by_slug_not_found(self):
        post = BlogPost.get_by_slug("nonexistent-slug")
        assert post is None

    def test_get_by_tag(self):
        posts = BlogPost.get_by_tag("python")
        assert len(posts) == 2
        for post in posts:
            assert "python" in post.tags

    def test_get_by_tag_no_results(self):
        posts = BlogPost.get_by_tag("nonexistent-tag")
        assert posts == []

    def test_post_has_all_fields(self):
        post = BlogPost.get_by_slug("welcome-to-my-blog")
        assert post.title == "Welcome to My Blog"
        assert post.slug == "welcome-to-my-blog"
        assert post.content != ""
        assert post.summary != ""
        assert isinstance(post.published_at, datetime)
        assert isinstance(post.tags, list)


class TestProfile:
    def test_get_default_profile(self):
        profile = Profile.get_default()
        assert profile.name == "Pierre"
        assert profile.title == "Software Developer"
        assert profile.email == "contact@example.com"
        assert profile.github != ""
        assert isinstance(profile.skills, list)
        assert len(profile.skills) > 0

    def test_profile_creation(self):
        profile = Profile(
            name="Test User",
            title="Developer",
            bio="A bio",
            email="test@example.com",
        )
        assert profile.name == "Test User"
        assert profile.github == ""
        assert profile.skills == []
