from typing import Any, ClassVar, Iterator, Optional

import lief # type: ignore
import lief.pdb # type: ignore
import lief.pdb.Type # type: ignore

class CompilationUnit:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def functions(self) -> Iterator[Optional[lief.pdb.Function]]: ...
    @property
    def module_name(self) -> str: ...
    @property
    def object_filename(self) -> str: ...
    @property
    def sources(self) -> Iterator[str]: ...

class DebugInfo(lief.DebugInfo):
    def __init__(self, *args, **kwargs) -> None: ...
    def find_public_symbol(self, name: str) -> Optional[lief.pdb.PublicSymbol]: ...
    def find_type(self, name: str) -> Optional[lief.pdb.Type]: ...
    @staticmethod
    def from_file(filepath: str) -> Optional[lief.pdb.DebugInfo]: ...
    @property
    def age(self) -> int: ...
    @property
    def compilation_units(self) -> Iterator[Optional[lief.pdb.CompilationUnit]]: ...
    @property
    def guid(self) -> str: ...
    @property
    def public_symbols(self) -> Iterator[Optional[lief.pdb.PublicSymbol]]: ...
    @property
    def types(self) -> Iterator[Optional[lief.pdb.Type]]: ...

class Function:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def RVA(self) -> int: ...
    @property
    def code_size(self) -> int: ...
    @property
    def name(self) -> str: ...
    @property
    def section_name(self) -> str: ...

class PublicSymbol:
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def RVA(self) -> int: ...
    @property
    def demangled_name(self) -> str: ...
    @property
    def name(self) -> str: ...
    @property
    def section_name(self) -> str: ...

class Type:
    class KIND:
        ARRAY: ClassVar[Type.KIND] = ...
        BITFIELD: ClassVar[Type.KIND] = ...
        CLASS: ClassVar[Type.KIND] = ...
        ENUM: ClassVar[Type.KIND] = ...
        FUNCTION: ClassVar[Type.KIND] = ...
        INTERFACE: ClassVar[Type.KIND] = ...
        MODIFIER: ClassVar[Type.KIND] = ...
        POINTER: ClassVar[Type.KIND] = ...
        SIMPLE: ClassVar[Type.KIND] = ...
        STRUCTURE: ClassVar[Type.KIND] = ...
        UNION: ClassVar[Type.KIND] = ...
        UNKNOWN: ClassVar[Type.KIND] = ...
        __name__: str
        def __init__(self, *args, **kwargs) -> None: ...
        def __ge__(self, other) -> bool: ...
        def __gt__(self, other) -> bool: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> Any: ...
        def __int__(self) -> int: ...
        def __le__(self, other) -> bool: ...
        def __lt__(self, other) -> bool: ...
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def kind(self) -> lief.pdb.Type.KIND: ...

def load(path: str) -> Optional[lief.pdb.DebugInfo]: ...
