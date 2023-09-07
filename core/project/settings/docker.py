if IN_DOCKER:  # type: ignore # noqa: F821
    temp_middle = 'django.middleware.security.SecurityMiddleware'
    assert MIDDLEWARE[:1] == [temp_middle]  # type: ignore # noqa: F821
