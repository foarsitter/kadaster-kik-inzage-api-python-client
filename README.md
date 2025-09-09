# Kadaster - KIK Inzage API Python client

[![PyPI](https://img.shields.io/pypi/v/kadaster-kikinzage-client.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/kadaster-kikinzage-client.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/kadaster-kikinzage-client)][pypi status]
[![License](https://img.shields.io/pypi/l/kadaster-kikinzage-client)][license]

[![Read the documentation at https://kadaster-kik-inzage-api-python-client.readthedocs.io/](https://img.shields.io/readthedocs/kadaster-kik-inzage-api-python-client/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/foarsitter/kadaster-kik-inzage-api-python-client/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/foarsitter/kadaster-kik-inzage-api-python-client/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/kadaster-kikinzage-client/
[read the docs]: https://kadaster-kik-inzage-api-python-client.readthedocs.io/
[tests]: https://github.com/foarsitter/kadaster-kik-inzage-api-python-client/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/foarsitter/kadaster-kik-inzage-api-python-client
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Features

- Fully typed client for the [Kadaster KIK Inzage API] version 6.0
- Asyncio support with httpx

## Requirements

- Pydantic V2
- httpx

## Installation

You can install _ Kadaster - KIK Inzage API Python client_ via [pip] from [PyPI]:

```console
$ pip install kadaster-kikinzage-client
```

## Usage

```python

import os
from kikinzage.client import DefaultClient,AsyncClient
from kikinzage.models import Formaat, Eigendomsinformatie


def create_client(client_class):
    client = client_class(
        # required
        password=os.getenv("KIK_PASSWORD"),
        username=os.getenv("KIK_PASSWORD"),
        # for testing
        # base_url="https://service10.kadaster.nl/kik-inzage-eto/v6/"
        base_url="https://service10.kadaster.nl/kik-inzage/v6/",
        # optional defaults added to each request when available
        formaat=Formaat.PDF_JSON,
        klantreferentie="Standaard klantreferentie",
        hyperlinkopproduct=True,
        inkoopnummer="Standaard inkoopnummer",
        gebruikeridentificatie="Standaard gebruikeridentificatie",
    )

    return client


kik = create_client(DefaultClient)

info: Eigendomsinformatie = kik.eigendomsinformatie_postcode("4884ME", "16")

async with create_client(AsyncClient) as kik:
    info_async: Eigendomsinformatie = await kik.eigendomsinformatie_kadastraalobjectidentificatie("BRD01K:G:0000", "1")

```

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_ Kadaster - KIK Inzage API Python client_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/foarsitter/kadaster-kik-inzage-api-python-client/issues
[pip]: https://pip.pypa.io/
[kadaster kik inzage api]: https://developer.kadaster.nl/schemas/-/categories/2669182

<!-- github-only -->

[license]: https://github.com/foarsitter/kadaster-kik-inzage-api-python-client/blob/main/LICENSE
[contributor guide]: https://github.com/foarsitter/kadaster-kik-inzage-api-python-client/blob/main/CONTRIBUTING.md
[command-line reference]: https://kadaster-kik-inzage-api-python-client.readthedocs.io/en/latest/usage.html

Changes...
