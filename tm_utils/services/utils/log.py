from logging import LoggerAdapter, getLogger
from typing import Any, Dict


class ContextLogger(LoggerAdapter):
    def __init__(self, logger=None, context: Dict[str, Any] = None):
        if logger is None:
            logger = getLogger(__name__)
        super().__init__(logger, context or {})

    def process(self, msg, kwargs):
        context_str = " ".join(f"{k}={v}" for k, v in self.extra.items())
        return f"[{context_str}] {msg}", kwargs

    def set_context(self, **kwargs):
        if not isinstance(self.extra, dict):
            self.extra = dict(self.extra)
        self.extra.update(kwargs)

    def clear_context(self):
        if not isinstance(self.extra, dict):
            self.extra = dict(self.extra)
        self.extra.clear()
