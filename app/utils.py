import re
from datetime import datetime
from typing import Any


def sanitize_input(text: str) -> str:
    """Sanitize user input by escaping HTML special characters."""
    replacements = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#x27;",
    }
    for char, escape in replacements.items():
        text = text.replace(char, escape)
    return text


def format_date(dt: datetime, fmt: str = "long") -> str:
    """Format a datetime for display.

    Args:
        dt: The datetime to format.
        fmt: Format style - 'long', 'short', or 'iso'.
    """
    if fmt == "long":
        return dt.strftime("%B %d, %Y")
    elif fmt == "short":
        return dt.strftime("%m/%d/%Y")
    elif fmt == "iso":
        return dt.strftime("%Y-%m-%d")
    else:
        raise ValueError(f"Unknown format: {fmt}")


def paginate(items: list[Any], page: int, per_page: int) -> dict:
    """Paginate a list of items.

    Args:
        items: Full list of items to paginate.
        page: Current page number (1-based).
        per_page: Number of items per page.

    Returns:
        Dict with keys: items, page, per_page, total, total_pages,
        has_prev, has_next.
    """
    if page < 1:
        page = 1
    if per_page < 1:
        per_page = 1

    total = len(items)
    total_pages = max(1, (total + per_page - 1) // per_page)

    if page > total_pages:
        page = total_pages

    start = (page - 1) * per_page
    end = start + per_page

    return {
        "items": items[start:end],
        "page": page,
        "per_page": per_page,
        "total": total,
        "total_pages": total_pages,
        "has_prev": page > 1,
        "has_next": page < total_pages,
    }


def slugify(text: str) -> str:
    """Convert text to a URL-friendly slug."""
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def truncate(text: str, length: int = 100, suffix: str = "...") -> str:
    """Truncate text to a given length, adding a suffix if truncated."""
    if len(text) <= length:
        return text
    return text[: length - len(suffix)].rsplit(" ", 1)[0] + suffix


def reading_time(text: str, wpm: int = 200) -> int:
    """Estimate reading time in minutes."""
    word_count = len(text.split())
    minutes = max(1, round(word_count / wpm))
    return minutes
