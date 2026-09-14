import time
from typing import Callable, TypeVar
from jarbinlocalapi.root.models.error import SystemInfoError

T = TypeVar("T")


def retry(
        function: Callable[[], T],
        attempts: int = 5,
        delay: float = 0.05,
    ) -> T:
    last_error = None

    for attempt in range(attempts):
        try:
            return function()

        except Exception as error:
            last_error = error

            if attempt < attempts - 1:
                time.sleep(delay)

    raise SystemInfoError from last_error
