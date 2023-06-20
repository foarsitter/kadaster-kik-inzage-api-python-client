from typing import Any
from typing import Dict


def remove_optional_params(**kwargs: Any) -> Dict[str, Any]:
    return {key: value for key, value in kwargs.items() if value is not None}
