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
class WorkExperience:
    """Represents a work experience entry."""

    company: str
    role: str
    start: str
    end: str
    description: str
    highlights: list[str] = field(default_factory=list)

    @classmethod
    def get_all(cls) -> list["WorkExperience"]:
        """Get all work experience entries (newest first)."""
        return [
            WorkExperience(
                company="Acme Corp",
                role="Senior Software Engineer",
                start="2023",
                end="Present",
                description=(
                    "Led backend development of the customer-facing platform, "
                    "improving request throughput and reliability."
                ),
                highlights=[
                    "Designed a service layer serving millions of monthly requests",
                    "Mentored three engineers and ran the team code-review rotation",
                    "Cut p95 latency by 35% through query and caching work",
                ],
            ),
            WorkExperience(
                company="Bright Studio",
                role="Full-Stack Developer",
                start="2020",
                end="2023",
                description=(
                    "Built and shipped several customer-facing web products end-to-end."
                ),
                highlights=[
                    "Shipped a billing dashboard used by the finance team",
                    "Introduced automated testing, raising coverage above 80%",
                    "Collaborated with design on a shared component library",
                ],
            ),
            WorkExperience(
                company="Startly",
                role="Junior Developer",
                start="2018",
                end="2020",
                description=(
                    "Contributed features and fixes across a multi-tenant SaaS app."
                ),
                highlights=[
                    "Implemented onboarding flows used by new customers",
                    "Resolved production bugs and improved on-call runbooks",
                    "Owned the internal admin tools and reporting scripts",
                ],
            ),
            WorkExperience(
                company="Nimbus Labs",
                role="Backend Engineering Intern",
                start="2017",
                end="2018",
                description=(
                    "Supported the platform team building data ingestion pipelines "
                    "and internal tooling during an internship."
                ),
                highlights=[
                    "Built a job-status dashboard for the operations team",
                    "Wrote integration tests for the event ingestion service",
                    "Documented onboarding steps for new interns",
                ],
            ),
            WorkExperience(
                company="Campus Open Source Club",
                role="Open Source Contributor",
                start="2016",
                end="2017",
                description=(
                    "Contributed to community-driven web projects while completing coursework."
                ),
                highlights=[
                    "Submitted pull requests improving accessibility on the club website",
                    "Helped organize a beginner-friendly hackathon for new students",
                    "Wrote introductory guides for the Flask workshop series",
                ],
            ),
        ]


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