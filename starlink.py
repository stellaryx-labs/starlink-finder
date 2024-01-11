import requests
from rich.console import Console

console = Console()

def get_api_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: Unable to fetch data. Status code: {response.status_code}")
        return None

def print_data(data):
    return

def print_menu():
    f = open('./assets/graphic.txt', 'r', encoding="utf8")
    content = f.read()
    console.print("[bold blue]" + content + "[/blue bold]")
    f = open('./assets/details.txt', 'r', encoding="utf8")
    details = f.read()
    console.print("[bold blue]" + details + "[/blue bold]")
    f.close()


def main():
    starlink_id = console.input("Enter Starlink ID:")
    print(starlink_id)
    api_url = "https://api.spacexdata.com/v4/starlink/" + starlink_id
    
    data = get_api_data(api_url)

    if data:
        for entry in data:
            print(entry)

if __name__ == "__main__":
    main()

