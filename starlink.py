from rich.console import Console
from modules.option import *
from modules.menu import *
from modules.table import *
from modules.api import *
from modules.indicators import *

console = Console()

API_URL = "https://api.spacexdata.com/v4/starlink/"


def main():
    print_menu()
    starlink_name = console.input(
        "[bold blue]Enter Starlink Satellite Name: [/ bold blue]")
    print("\n")

    data = get_api_data(API_URL)
    found = False
    table_title = f"Information for {starlink_name} 🛰️"

    if data:
        for entry in data:
            if entry["spaceTrack"]["OBJECT_NAME"] == starlink_name:
                print_data(table_title, entry)
                found = True

    if found == False:
        print_error("Starlink Satellite Not Found!")

    generate_options()


def generate_options():
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
