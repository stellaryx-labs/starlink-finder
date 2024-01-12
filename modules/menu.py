from rich.console import Console

console = Console()


def print_menu():
    f = open('./assets/graphics.txt', 'r', encoding="utf8")
    content = f.read()
    console.print("[bold blue]" + content + "[/blue bold]")
    f = open('./assets/details.txt', 'r', encoding="utf8")
    details = f.read()
    console.print("[bold blue]" + details + "[/blue bold]")
    f.close()
