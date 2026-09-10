"""The Task/Decision contract, as plain stdlib dataclasses — no dependency on
the Arena's own code or on any third-party package. Don't edit this file:
it's the plumbing that lets ``python -m router`` talk to the Arena over
stdin/stdout JSON. Your logic goes in ``decide.py``.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Task:
    task_id: str
    prompt: str
    context: dict = field(default_factory=dict)
    constraints: dict = field(default_factory=dict)

    @staticmethod
    def from_dict(d: dict) -> "Task":
        return Task(
            task_id=d["task_id"],
            prompt=d["prompt"],
            context=d.get("context", {}),
            constraints=d.get("constraints", {}),
        )


@dataclass
class Decision:
    route: str  # "model" | "human"
    target: str  # a model_id from the catalog, or "human_review"
    reasoning: str = ""
    confidence: float | None = None

    def to_dict(self) -> dict:
        return {
            "route": self.route,
            "target": self.target,
            "reasoning": self.reasoning,
            "confidence": self.confidence,
        }
