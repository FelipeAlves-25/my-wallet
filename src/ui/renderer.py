from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

dir = Path(__file__).parent / "templates"

env = Environment(
        loader = FileSystemLoader(dir),
        autoescape=select_autoescape("html"))

def render(template: str, **context):
    return env.get_template(template).render(**context)

