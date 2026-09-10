"""Tu router. Implementa decide() — es la única función que la Arena llama.

Recibe una Task (task_id, prompt, context, constraints) — un ticket de
desarrollo del propio proyecto CaixaBank Tech Arena — y debe devolver una Decision:
a qué modelo del catálogo enrutas el ticket, o si lo derivas a un
desarrollador humano ("human_developer").
"""
from __future__ import annotations

from router._contract import Decision, Task


def decide(task: Task) -> Decision:
    raise NotImplementedError("Implementa decide() en router/decide.py")
