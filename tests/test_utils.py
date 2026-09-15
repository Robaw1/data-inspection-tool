from my_ai_project.utils import get_greeting


def test_get_greeting():
    assert get_greeting() == "Hello, AI project!"
