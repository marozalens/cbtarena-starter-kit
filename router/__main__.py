"""Plumbing — no lo edites. Lee una Task por stdin, llama a decide(), y
escribe la Decision por stdout. La Arena ejecuta este módulo como
`python -m router` en un proceso aparte: nunca importa tu código directamente.

Cualquier print() que hagas dentro de decide() se redirige a stderr, para que
no rompa la única línea de JSON que la Arena espera leer en stdout.
"""
from __future__ import annotations

import contextlib
import io
import json
import sys

from router._contract import Task
from router.decide import decide


def main() -> None:
    task = Task.from_dict(json.loads(sys.stdin.read()))

    captured = io.StringIO()
    with contextlib.redirect_stdout(captured):
        decision = decide(task)
    stray_output = captured.getvalue()
    if stray_output:
        print(stray_output, file=sys.stderr, end="")

    print(json.dumps(decision.to_dict()))


if __name__ == "__main__":
    main()
