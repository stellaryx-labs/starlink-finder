import requests
from rich.align import Align
from rich.console import Console
from rich.live import Live
from rich.table import Table
from modules.option import *

console = Console()


def get_api_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(
            f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None


def print_data(starlink_name, data):
    console = Console()
    table = Table(show_footer=False)
    table_centered = Align.left(table)

    contents = []

    data = data["spaceTrack"]
    for prop in data:
        contents.append(get_row_content(prop, data[prop]))

    with Live(table_centered, console=console,
              screen=False):
        table.add_column(
            f"Information for {starlink_name} 🛰️", no_wrap=True)

        for content in contents:
            if len(content) > 0:
                table.add_row(content)

    table.width = None


def get_row_content(key, value):
    key = key.upper().replace("_", " ")

    return f"[b white]{key}[/]: [blue]{value} [/]"


def print_menu():
    f = open('./assets/graphics.txt', 'r', encoding="utf8")
    content = f.read()
    console.print("[bold blue]" + content + "[/blue bold]")
    f = open('./assets/details.txt', 'r', encoding="utf8")
    details = f.read()
    console.print("[bold blue]" + details + "[/blue bold]")
    f.close()


def main():
    print_menu()
    starlink_name = console.input("Enter Starlink Satellite Name:")
    print("Retrieving Information for " + starlink_name)
    api_url = "https://api.spacexdata.com/v4/starlink/"

    data = get_api_data(api_url)
    found = False

    if data:
        for entry in data:
            if entry["spaceTrack"]["OBJECT_NAME"] == starlink_name:
                print_data(starlink_name, entry)
                found = True

    if found == False:
        print("entry not found")

    option()


def option():
    options = [
        "Run Again",
        "Exit Tool"
    ]

    option = generate_option(options)

    if option == 1:
        main()
    else:
        return


if __name__ == "__main__":
    main()
