class Engine:
    def __init__(self, *args, **kwargs) -> None: ...

class Instruction:
    def __init__(self, *args, **kwargs) -> None: ...
    def to_string(self) -> str: ...
    @property
    def address(self) -> int: ...
    @property
    def mnemonic(self) -> str: ...
    @property
    def raw(self) -> bytes: ...
    @property
    def size(self) -> int: ...