"""Command-line interface."""
import json
import os
from json import JSONDecodeError
from pathlib import Path

import click
import httpx
from click import Context

from kikinzage.client import DefaultClient
from kikinzage.client import RequestFixtures
from kikinzage.models import Formaat


@click.group()
@click.version_option()
def main() -> None:
    """Kadaster - KIK Inzage API Python client."""


@main.group()
@click.argument("filename", type=str)
@click.pass_context
def eigendomsinformatie(
    ctx: Context,
    filename: str,
) -> None:
    """Eigendomsinformatie."""
    ctx.ensure_object(dict)

    ctx.obj["filename"] = filename


@eigendomsinformatie.command()
@click.pass_context
@click.argument("postcode", type=str)
@click.argument("huisnummer", type=str)
def postcode(ctx: Context, postcode: str, huisnummer: str) -> None:
    """Eigendomsinformatie - Postcode."""

    log_response = ResponseStorage()
    response_path = Path(ctx.obj["filename"])

    kik = DefaultClient(
        username=os.getenv("KIK_USERNAME", default="EMPTY"),
        password=os.getenv("KIK_PASSWORD", default="EMPTY"),
        event_hooks={"response": [log_response]},
    )

    kik.eigendomsinformatie_postcode_get(
        postcode=postcode,
        huisnummer=huisnummer,
        formaat=Formaat.JSON,
        klantreferentie="onbekend",
    )

    with response_path.open("w+") as f:
        json.dump(log_response.responses, f, indent=4)


if __name__ == "__main__":
    main(prog_name="kadaster-kik-inzage-api-python-client")  # pragma: no cover


class ResponseStorage:
    def __init__(self) -> None:
        self.responses: RequestFixtures = {}

    def __call__(self, response: httpx.Response) -> None:
        response.read()

        try:
            data = response.json()
        except (JSONDecodeError, UnicodeDecodeError):  # pragma: no cover
            data = {"binary": True}

        key = str(response.url)

        if key not in self.responses:
            self.responses[key] = {}
        if response.request.method not in self.responses[key]:  # pragma: no cover
            self.responses[key][response.request.method] = {}

        self.responses[key][response.request.method][
            str(response.status_code)
        ] = data  # pragma: no cover
