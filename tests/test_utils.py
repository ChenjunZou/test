from datetime import datetime

import pytest

from app.utils import (
    format_date,
    paginate,
    reading_time,
    sanitize_input,
    slugify,
    truncate,
)


class TestSanitizeInput:
    def test_escapes_ampersand(self):
        assert sanitize_input("a & b") == "a &amp; b"

    def test_escapes_less_than(self):
        assert sanitize_input("<script>") == "&lt;script&gt;"

    def test_escapes_greater_than(self):
        assert sanitize_input("a > b") == "a &gt; b"

    def test_escapes_double_quote(self):
        assert sanitize_input('say "hi"') == "say &quot;hi&quot;"

    def test_escapes_single_quote(self):
        assert sanitize_input("it's") == "it&#x27;s"

    def test_empty_string(self):
        assert sanitize_input("") == ""

    def test_no_special_chars(self):
        assert sanitize_input("hello world") == "hello world"

    def test_multiple_special_chars(self):
        result = sanitize_input('<a href="x">&</a>')
        assert "&lt;" in result
        assert "&amp;" in result
        assert "&quot;" in result


class TestFormatDate:
    def test_long_format(self):
        dt = datetime(2024, 3, 15, 10, 30)
        assert format_date(dt, "long") == "March 15, 2024"

    def test_short_format(self):
        dt = datetime(2024, 3, 15, 10, 30)
        assert format_date(dt, "short") == "03/15/2024"

    def test_iso_format(self):
        dt = datetime(2024, 3, 15, 10, 30)
        assert format_date(dt, "iso") == "2024-03-15"

    def test_default_is_long(self):
        dt = datetime(2024, 1, 1)
        assert format_date(dt) == "January 01, 2024"

    def test_unknown_format_raises(self):
        dt = datetime(2024, 1, 1)
        with pytest.raises(ValueError, match="Unknown format"):
            format_date(dt, "unknown")


class TestPaginate:
    def test_first_page(self):
        items = list(range(10))
        result = paginate(items, page=1, per_page=3)
        assert result["items"] == [0, 1, 2]
        assert result["page"] == 1
        assert result["total"] == 10
        assert result["total_pages"] == 4
        assert result["has_prev"] is False
        assert result["has_next"] is True

    def test_middle_page(self):
        items = list(range(10))
        result = paginate(items, page=2, per_page=3)
        assert result["items"] == [3, 4, 5]
        assert result["has_prev"] is True
        assert result["has_next"] is True

    def test_last_page(self):
        items = list(range(10))
        result = paginate(items, page=4, per_page=3)
        assert result["items"] == [9]
        assert result["has_prev"] is True
        assert result["has_next"] is False

    def test_page_below_one_clamped(self):
        items = list(range(5))
        result = paginate(items, page=0, per_page=2)
        assert result["page"] == 1

    def test_page_above_max_clamped(self):
        items = list(range(5))
        result = paginate(items, page=100, per_page=2)
        assert result["page"] == 3

    def test_per_page_below_one_clamped(self):
        items = list(range(5))
        result = paginate(items, page=1, per_page=0)
        assert result["per_page"] == 1

    def test_empty_list(self):
        result = paginate([], page=1, per_page=5)
        assert result["items"] == []
        assert result["total"] == 0
        assert result["total_pages"] == 1


class TestSlugify:
    def test_basic_slug(self):
        assert slugify("Hello World") == "hello-world"

    def test_special_characters_removed(self):
        assert slugify("Hello! World?") == "hello-world"

    def test_multiple_spaces(self):
        assert slugify("hello   world") == "hello-world"

    def test_leading_trailing_hyphens_stripped(self):
        assert slugify("--hello--") == "hello"

    def test_underscores_become_hyphens(self):
        assert slugify("hello_world") == "hello-world"

    def test_empty_string(self):
        assert slugify("") == ""


class TestTruncate:
    def test_short_text_unchanged(self):
        assert truncate("hello", length=100) == "hello"

    def test_long_text_truncated(self):
        text = "This is a long sentence that should be truncated"
        result = truncate(text, length=20)
        assert len(result) <= 20
        assert result.endswith("...")

    def test_custom_suffix(self):
        result = truncate("hello world foo bar", length=15, suffix="…")
        assert result.endswith("…")

    def test_exact_length_not_truncated(self):
        text = "exact"
        assert truncate(text, length=5) == "exact"


class TestReadingTime:
    def test_short_text(self):
        assert reading_time("one two three") == 1

    def test_longer_text(self):
        text = " ".join(["word"] * 400)
        assert reading_time(text) == 2

    def test_custom_wpm(self):
        text = " ".join(["word"] * 100)
        assert reading_time(text, wpm=100) == 1
