import json
from dotenv import load_dotenv

from file import *
from mail import *

from modules.urls import *
from modules.keywords import *
from modules.blacklists import *

def main():

    load_dotenv()

    result = []

    modules = [
        Urls(),
        Keywords(),
        Blacklists()
    ]

    mail = Mail(read_file("../mail_samples/eml_sample_4.eml"))

    for module in modules:
        module.check_mail(mail)
        result.append(module.get_output())

    write_file("./output.json", json.dumps(result))


if __name__ == "__main__":
    main()