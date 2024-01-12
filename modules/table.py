from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.align import Align


def print_data(table_title, data):
    console = Console()
    table = Table(show_footer=False)
    table_centered = Align.left(table)
    data = data["spaceTrack"]

    contents = []

    for prop in data:
        contents.append(get_row_content(prop, data[prop]))

    with Live(table_centered, console=console,
              screen=False):
        table.add_column(
            table_title, no_wrap=True)

        for content in contents:
            if len(content) > 0:
                table.add_row(content)

    table.width = None


def get_row_content(key, value):
    key = key.upper().replace("_", " ")

    return f"[b white]{key}[/]: [cyan]{value} [/]"
