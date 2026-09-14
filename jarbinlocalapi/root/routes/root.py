from pathlib import Path
import markdown
from fastapi import HTTPException
from fastapi.responses import HTMLResponse

from jarbinlocalapi.root import jarbinlocalapi
from jarbinlocalapi.root import JARBINLOCALAPI_DIR


@jarbinlocalapi.get("/")
def get_root():
    """
    Route: `/`

    Get server status.
    """
    return {"status": "OK"}


DOCS_DIR = Path(JARBINLOCALAPI_DIR).resolve().parent / "docs"


page_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page} — JarbinLocalAPI</title>

    <link
        rel="stylesheet"
        href="/static/css/docs.css"
    >
</head>

<body>
    <main>
        {html}
    </main>
</body>
</html>
"""


@jarbinlocalapi.get("/d/", response_class=HTMLResponse)
def get_doc_root():
    return get_doc("root")


@jarbinlocalapi.get("/d/{page:path}", response_class=HTMLResponse)
def get_doc(page: str):
    """
    Route: `/d/<page>`

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

    return HTMLResponse(page_template.format(page=page, html=html))