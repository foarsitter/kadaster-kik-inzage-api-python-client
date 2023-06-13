import os

import pytest

from kikinzage.client.default import DefaultClient


@pytest.fixture
def kik() -> DefaultClient:
    password = os.getenv("KIK_PASSWORD")
    username = os.getenv("KIK_USERNAME")

    if not password or not username:  # pragma: no cover
        raise Exception(
            "KIK_PASSWORD and KIK_USERNAME environment variables must be set"
        )

    return DefaultClient(
        username=username,
        password=password,
    )
