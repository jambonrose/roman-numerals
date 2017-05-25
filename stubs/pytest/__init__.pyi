from contextlib import ContextManager
from typing import Type

from . import mark  # noqa F401


def raises(exception: Type) -> ContextManager[None]:
    ...
