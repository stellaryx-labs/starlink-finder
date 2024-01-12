from rich.console import Console

console = Console()


def print_error(log):
    console.print(f"[bold red] ERROR: {log} [/bold red]")


def print_log(log):
    console.print(f"[bold white] {log} [/bold white]")
