from typing import Callable, Sequence


def parametrize(
        parameter_names: str,
        arguments: Sequence[Sequence],
) -> Callable:
    ...
