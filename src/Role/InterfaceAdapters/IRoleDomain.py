from abc import ABC
from typing import List


class IRoleDomain(ABC):
    name: str
    slug: str
    enable: bool
    permissions: List[str]
