import json
import sys
from dotenv import load_dotenv

from file import *
from mail import *

from modules.urls import *
from modules.keywords import *
from modules.blacklists import *

def main():

    if (len(sys.argv) < 2):
        print(f"Usage: {sys.argv[0]} filename")
        
        exit(1)

    file = sys.argv[1]

    load_dotenv()

    result = []

    modules = [
        Urls(),
        Keywords(),
        Blacklists()
    ]

    mail = Mail(read_file(file))

    for module in modules:
        module.check_mail(mail)
        result.append(module.get_output())

    write_file("./result.json", json.dumps(result))


if __name__ == "__main__":
    main()