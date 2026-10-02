"""Regenerate the open-source contribution sections of README.md from the GitHub search API."""

import json
import os
import re
import urllib.parse
import urllib.request
from pathlib import Path

USER = os.environ.get("GITHUB_USER", "wenchen76")
README = Path(__file__).resolve().parent.parent / "README.md"
API = "https://api.github.com/search/issues"


def search(query: str) -> list[dict]:
    """Return all search results for a GitHub issues/PRs query, newest first."""
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    items, page = [], 1
    while True:
        params = urllib.parse.urlencode(
            {"q": query, "sort": "created", "order": "desc", "per_page": 100, "page": page}
        )
        request = urllib.request.Request(f"{API}?{params}", headers=headers)
        with urllib.request.urlopen(request) as response:
            batch = json.load(response)["items"]
        items.extend(batch)
        if len(batch) < 100:
            return items
        page += 1


def repo_of(item: dict) -> str:
    return item["repository_url"].removeprefix("https://api.github.com/repos/")


def render(items: list[dict]) -> str:
    if not items:
        return "_None yet._"
    lines = ["| Date | Project | Title |", "|---|---|---|"]
    for item in items:
        repo = repo_of(item)
        title = item["title"].replace("|", "\\|")
        lines.append(
            f"| {item['created_at'][:10]} | `{repo}` | [{title}]({item['html_url']}) (#{item['number']}) |"
        )
    return "\n".join(lines)


def replace_section(text: str, name: str, body: str) -> str:
    pattern = re.compile(rf"(<!-- {name}:start -->).*?(<!-- {name}:end -->)", re.S)
    return pattern.sub(lambda m: f"{m.group(1)}\n{body}\n{m.group(2)}", text)


def main() -> None:
    # Exclude the user's own repositories (forks and personal projects).
    upstream = f"author:{USER} -user:{USER}"
    sections = {
        "merged": search(f"{upstream} is:pr is:merged"),
        "open": search(f"{upstream} is:pr is:open"),
        "issues": search(f"{upstream} is:issue"),
    }
    text = README.read_text()
    for name, items in sections.items():
        text = replace_section(text, name, render(items))
    README.write_text(text)


if __name__ == "__main__":
    main()
