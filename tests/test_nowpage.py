"""
Health tests for NowPage Generator.

Signature: Mourad.Soltani
"""

import pytest
from nowpage_gen import generate_html


def test_generate_basic():
    html = generate_html(
        name="Test User",
        currently="Building tools",
        projects=["Project A", "Project B"],
        location="Remote",
    )
    assert "Test User's Now Page" in html
    assert "Building tools" in html
    assert "<li>Project A</li>" in html
    assert "<li>Project B</li>" in html
    assert "Remote" in html
    assert "Mourad.Soltani" in html
    assert "<!DOCTYPE html>" in html


def test_empty_projects():
    html = generate_html(
        name="Solo",
        currently="Resting",
        projects=[],
        location="Home",
    )
    assert "No active projects listed." in html


def test_strips_whitespace():
    html = generate_html(
        name="Dev",
        currently="Coding",
        projects=["  Clean Project  ", ""],
        location="Earth",
    )
    assert "<li>Clean Project</li>" in html
    assert "<li></li>" not in html
