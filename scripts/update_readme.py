"""Regenerate the open-source contribution sections of README.md from the GitHub API."""

import json
import os
import re
import urllib.parse
import urllib.request
from pathlib import Path

USER = os.environ.get("GITHUB_USER", "wenchen76")
README = Path(__file__).resolve().parent.parent / "README.md"
API = "https://api.github.com"


def get(url: str) -> dict:
    headers = {"Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers)) as response:
        return json.load(response)


def search(query: str) -> list[dict]:
    """Return all search results for a GitHub issues/PRs query, newest first."""
    items, page = [], 1
    while True:
        params = urllib.parse.urlencode(
            {"q": query, "sort": "created", "order": "desc", "per_page": 100, "page": page}
        )
        batch = get(f"{API}/search/issues?{params}")["items"]
        items.extend(batch)
        if len(batch) < 100:
            return items
        page += 1


def manual_issues(text: str) -> list[dict]:
    """Fetch the issues listed by URL in the README's `working-manual` comment."""
    match = re.search(r"<!-- working-manual(.*?)-->", text, re.S)
    urls = re.findall(r"https://github\.com/([\w.-]+/[\w.-]+)/issues/(\d+)", match.group(1)) if match else []
    return [get(f"{API}/repos/{repo}/issues/{number}") for repo, number in urls]


def newest_first(items: list[dict]) -> list[dict]:
    unique = {item["html_url"]: item for item in items}
    return sorted(unique.values(), key=lambda item: item["created_at"], reverse=True)


def repo_of(item: dict) -> str:
    return item["repository_url"].removeprefix(f"{API}/repos/")


def render(items: list[dict], show_kind: bool = False) -> str:
    # Group by repository, keeping repositories in order of their newest item.
    groups: dict[str, list[dict]] = {}
    for item in items:
        groups.setdefault(repo_of(item), []).append(item)
    blocks = []
    for repo, repo_items in groups.items():
        lines = [f"**{repo}**", ""]
        for item in repo_items:
            label = f"#{item['number']}"
            if show_kind:
                kind = "PR" if "pull_request" in item else "Issue"
                status = (item.get("state_reason") or item["state"]).replace("_", " ")
                label = f"{kind} {label} · {status}"
            lines.append(f"- [{item['title']}]({item['html_url']}) `{label}`")
        blocks.append("\n".join(lines))
    return "\n\n".join(blocks)


def replace_section(text: str, name: str, body: str) -> str:
    pattern = re.compile(rf"(<!-- {name}:start -->).*?(<!-- {name}:end -->)", re.S)
    inner = f"\n{body}\n" if body else "\n"
    return pattern.sub(lambda m: f"{m.group(1)}{inner}{m.group(2)}", text)


def main() -> None:
    text = README.read_text()
    # Exclude the user's own repositories (forks and personal projects).
    upstream = f"author:{USER} -user:{USER}"
    sections = {
        "merged": search(f"{upstream} is:pr is:merged"),
        # Hand-picked issues that are still open, plus open issues assigned to the user.
        "working": newest_first(
            [item for item in manual_issues(text) if item["state"] == "open"]
            + search(f"assignee:{USER} -user:{USER} is:issue is:open")
        ),
        "open": search(f"{upstream} is:pr is:open"),
        # Unmerged PRs plus closed issues assigned to the user (excluding ones they opened).
        "closed": newest_first(
            search(f"{upstream} is:pr is:closed is:unmerged")
            + search(f"assignee:{USER} -author:{USER} -user:{USER} is:issue is:closed")
        ),
        "issues": search(f"{upstream} is:issue"),
    }
    for name, items in sections.items():
        text = replace_section(text, name, render(items, show_kind=name == "closed"))
    README.write_text(text)


if __name__ == "__main__":
    main()
