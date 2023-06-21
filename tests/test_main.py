"""Test cases for the __main__ module."""
import pytest
from click.testing import CliRunner
from respx import MockRouter

from kikinzage import __main__


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(__main__.main)
    assert result.exit_code == 0


def test_postcode_succeeds(respx_mock: MockRouter, runner: CliRunner) -> None:
    """It exits with a status code of zero."""
    result = runner.invoke(
        __main__.eigendomsinformatie, ["test.json", "postcode", "4884ME", "16"]
    )
    assert result.exit_code == 0
