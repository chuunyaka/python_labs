from pathlib import Path
import csv
from pathlib import Path
from typing import Union, Iterable, Sequence

def ensure_parent_dir(path: Union[str, Path]) -> None:
    """Создает родительские директории для указанного пути, если они не существуют."""
    Path(path).parent.mkdir(parents=True, exist_ok=True) 

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Открывает файл и возвращает его содержимое в виде одной строки.
    Если файл пустой, возвращает пустую строку.
    Для смены кодировки используйте аргумент, например: encoding="cp1251"
    """
    p = Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    """Создает или перезаписывает CSV-файл с разделителем ','."""
    p = Path(path)
    ensure_parent_dir(p)   
    rows = list(rows)
    
    if rows:
            first_len = len(rows[0])
            if not all(len(r) == first_len for r in rows):
                raise ValueError("Все строки в rows должны иметь одинаковую длину.")
            if header is not None and len(header) != first_len:
                raise ValueError("Длина заголовка должна совпадать с длиной строк.")
    
    if not rows and header is None:
        p.write_bytes(b"")
        return

    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)
