from __future__ import annotations

import praw
import pytest


@pytest.fixture(scope='session')
def monkeysession(request):
    from _pytest.monkeypatch import MonkeyPatch

    mpatch = MonkeyPatch()
    yield mpatch
    mpatch.undo()


# noinspection PyMethodMayBeStatic
class MockRedditor:
    def me(self):
        return 'Mocked Redditor'


class MockSubmission:
    def __init__(self, title, created_utc: float = 0.0):
        self.title = title
        self.author = 'testauthor'
        self.created_utc = created_utc


# noinspection PyUnusedLocal
# noinspection PyMethodMayBeStatic
class MockSubreddit:
    def __init__(self, display_name: str, *args, **kwargs):
        self.display_name = display_name
        self.subscribers = 1_000_000
        self.accounts_active = 5_000
        self.public_description = 'A test subreddit'
        self.created_utc = 1234567890.0
        self.subreddit_type = 'public'
        self.over18 = False

    def __repr__(self):  # pragma: nocover
        return self.display_name

    def controversial(self, *args, **kwargs):
        return [MockSubmission('controversial') for _ in range(kwargs['limit'])]

    def gilded(self, *args, **kwargs):
        return [MockSubmission('gilded') for _ in range(kwargs['limit'])]

    def hot(self, *args, **kwargs):
        return [MockSubmission('hot') for _ in range(kwargs['limit'])]

    def new(self, *args, **kwargs):
        # 3 posts on 2025-01-15 and 2 posts on 2025-01-14, newest first
        dated_posts = [
            MockSubmission('new', created_utc=1736946000.0),  # 2025-01-15 15:00 UTC
            MockSubmission('new', created_utc=1736935200.0),  # 2025-01-15 12:00 UTC
            MockSubmission('new', created_utc=1736924400.0),  # 2025-01-15 09:00 UTC
            MockSubmission('new', created_utc=1736870400.0),  # 2025-01-14 18:00 UTC
            MockSubmission('new', created_utc=1736856000.0),  # 2025-01-14 14:00 UTC
        ]
        limit = kwargs['limit']
        if limit >= 5:
            return dated_posts
        return [MockSubmission('new') for _ in range(limit)]

    def random_rising(self, *args, **kwargs):
        return [MockSubmission('random_rising') for _ in range(kwargs['limit'])]

    def rising(self, *args, **kwargs):
        return [MockSubmission('rising') for _ in range(kwargs['limit'])]

    def top(self, *args, **kwargs):
        return [MockSubmission('top') for _ in range(kwargs['limit'])]


# noinspection PyUnusedLocal
class MockReddit:
    def __init__(self, *args, **kwargs):
        self.user = MockRedditor()
        self.subreddit = MockSubreddit


@pytest.fixture(scope='session', autouse=True)
def mock_reddit(monkeysession):
    monkeysession.setattr(praw, 'Reddit', MockReddit)
