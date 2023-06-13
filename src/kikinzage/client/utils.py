from typing import Any
from typing import Dict


def kwargs_as_params(**kwargs: Any) -> Dict[str, Any]:
    return {key: value for key, value in kwargs.items() if value is not None}
