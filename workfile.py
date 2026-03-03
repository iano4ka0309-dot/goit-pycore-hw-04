import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def show_directory(path, prefix=""):
    for item in path.iterdir():
        if item.is_dir():
            print(prefix + Fore.BLUE + item.name)
            show_directory(item, prefix + "    ")
        else:
            print(prefix + Fore.GREEN + item.name)

path = Path(sys.argv[1])

if not path.exists():
    print("нема такої адреси!")
    sys.exit(1)

if not path.is_dir():
    print("це не папка!")
    sys.exit(1)

print(Fore.YELLOW + str(path))
show_directory(path)