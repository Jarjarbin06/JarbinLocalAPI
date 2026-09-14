from pathlib import Path
import markdown
from fastapi import HTTPException
from fastapi.responses import HTMLResponse

from jarbinlocalapi.root import jarbinlocalapi
from jarbinlocalapi.templates.d.doc import template_doc
from jarbinlocalapi import (
    __name__ as title,
    __version__ as version
)
from jarbinlocalapi.root import JARBINLOCALAPI_DIR


DOCS_DIR = Path(JARBINLOCALAPI_DIR).resolve().parent / "docs"


@jarbinlocalapi.get("/doc/", response_class=HTMLResponse)
def get_doc_root():
    return get_doc("routes")


@jarbinlocalapi.get("/doc/{page:path}", response_class=HTMLResponse)
def get_doc(page: str):
    """
    Route: `/doc/<page>`

    Get a documentation page.
    """

    if page == "root":
        filename = "root.md"
    else:
        filename = f"{page.replace('/', '.')}.md"

    doc_path = DOCS_DIR / filename

    if not doc_path.is_file():
        raise HTTPException(
            status_code=404,
            detail=f"Documentation page not found: {page}",
        )

    content = doc_path.read_text(encoding="utf-8")

    html = markdown.markdown(
        content,
        extensions=[
            "fenced_code",
            "tables",
        ],
    )

    return template_doc.render(title = title, version = version, page = page, html = html)
