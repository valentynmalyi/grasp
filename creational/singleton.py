from __future__ import annotations

from typing import Optional


class Singleton:
    instance: Optional[Singleton] = None

    @staticmethod
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            return cls.instance
        return cls.instance


instance1 = Singleton()
instance2 = Singleton()
print(instance2 is instance1)
