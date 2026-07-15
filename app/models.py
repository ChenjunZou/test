from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class BlogPost:
    """Represents a blog post."""

    title: str
    slug: str
    content: str
    summary: str
    published_at: datetime
    tags: list[str] = field(default_factory=list)

    # In-memory store for demo purposes
    _posts: list["BlogPost"] = field(default=None, init=False, repr=False)

    @classmethod
    def _get_store(cls) -> list["BlogPost"]:
        """Get or initialize the in-memory post store."""
        if not hasattr(cls, "_store") or cls._store is None:
            cls._store = [
                BlogPost(
                    title="Welcome to My Blog",
                    slug="welcome-to-my-blog",
                    content="This is my first blog post. Welcome!",
                    summary="A warm welcome to my personal blog.",
                    published_at=datetime(2024, 1, 15, 10, 0),
                    tags=["welcome", "personal"],
                ),
                BlogPost(
                    title="Learning Python",
                    slug="learning-python",
                    content="Python is an amazing language for web development.",
                    summary="My journey learning Python for web development.",
                    published_at=datetime(2024, 2, 20, 14, 30),
                    tags=["python", "programming"],
                ),
                BlogPost(
                    title="Flask Tips and Tricks",
                    slug="flask-tips-and-tricks",
                    content="Here are some useful Flask patterns I've discovered.",
                    summary="Useful patterns for Flask web development.",
                    published_at=datetime(2024, 3, 10, 9, 15),
                    tags=["python", "flask", "web"],
                ),
                BlogPost(
                    title="Deploying Web Apps",
                    slug="deploying-web-apps",
                    content="A guide to deploying Flask applications.",
                    summary="Step-by-step deployment guide.",
                    published_at=datetime(2024, 4, 5, 16, 45),
                    tags=["deployment", "devops"],
                ),
            ]
        return cls._store

    @classmethod
    def get_all(cls) -> list["BlogPost"]:
        """Get all posts sorted by date (newest first)."""
        posts = cls._get_store()
        return sorted(posts, key=lambda p: p.published_at, reverse=True)

    @classmethod
    def get_recent(cls, limit: int = 3) -> list["BlogPost"]:
        """Get the most recent posts."""
        return cls.get_all()[:limit]

    @classmethod
    def get_by_slug(cls, slug: str) -> Optional["BlogPost"]:
        """Find a post by its slug."""
        for post in cls._get_store():
            if post.slug == slug:
                return post
        return None

    @classmethod
    def get_by_tag(cls, tag: str) -> list["BlogPost"]:
        """Get all posts with a specific tag."""
        return [p for p in cls.get_all() if tag in p.tags]


@dataclass
class Profile:
    """Represents user profile information."""

    name: str
    title: str
    bio: str
    email: str
    github: str = ""
    linkedin: str = ""
    skills: list[str] = field(default_factory=list)

    @classmethod
    def get_default(cls) -> "Profile":
        """Get the default profile."""
        return cls(
            name="Pierre",
            title="Software Developer",
            bio="Passionate developer who loves building web applications.",
            email="contact@example.com",
            github="https://github.com/ChenjunZou",
            linkedin="",
            skills=["Python", "Flask", "JavaScript", "SQL", "Git"],
        )


@dataclass
class Project:
    """Represents a portfolio project."""

    title: str
    description: str
    url: str = ""
    repo_url: str = ""
    tags: list[str] = field(default_factory=list)

    @classmethod
    def get_all(cls) -> list["Project"]:
        """Get all portfolio projects."""
        return [
            Project(
                title="Personal Website",
                description="A Flask-based personal website with blog, portfolio, and contact features.",
                url="",
                repo_url="https://github.com/ChenjunZou",
                tags=["Flask", "Python", "Jinja2"],
            ),
            Project(
                title="Task Tracker CLI",
                description="A command-line task manager with persistent storage and tagging.",
                url="",
                repo_url="https://github.com/ChenjunZou",
                tags=["Python", "CLI", "SQLite"],
            ),
            Project(
                title="Weather Dashboard",
                description="A responsive weather dashboard consuming a public weather API.",
                url="",
                repo_url="https://github.com/ChenjunZou",
                tags=["JavaScript", "HTML", "CSS"],
            ),
            Project(
                title="REST API Service",
                description="A small REST API service with authentication and pagination.",
                url="",
                repo_url="https://github.com/ChenjunZou",
                tags=["Flask", "REST", "SQL"],
            ),
        ]