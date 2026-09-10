"""Corre tu decide() contra un banco de tareas de práctica, en tu propio
ordenador. No llama a la Arena ni gasta presupuesto — solo te deja ver, tarea
a tarea, qué destino elegirías y por qué, antes de enviar nada.

Uso: python practice_harness.py
"""
from __future__ import annotations

import json
from pathlib import Path

from router._contract import Task
from router.decide import decide

TASKS_PATH = Path(__file__).parent / "practice_tasks.json"


def main() -> None:
    tasks = json.loads(TASKS_PATH.read_text(encoding="utf-8"))
    print(f"{'tarea':<10} {'ruta':<8} {'destino':<20} razonamiento")
    print("-" * 78)
    for item in tasks:
        task = Task.from_dict(item)
        try:
            decision = decide(task)
        except NotImplementedError:
            print(f"{task.task_id:<10} decide() todavía no está implementada")
            continue
        print(f"{task.task_id:<10} {decision.route:<8} {decision.target:<20} {decision.reasoning}")


if __name__ == "__main__":
    main()
