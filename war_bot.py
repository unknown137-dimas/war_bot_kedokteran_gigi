from csv import reader
from requests import post
from enum import Enum
from time import sleep


class OpsiForm(str, Enum):
    TEST = "test"
    LANTAI_2 = "lantai_2"
    LANTAI_4_AEROSOL = "lantai_4_aerosol"
    LANTAI_4_NON_AEROSOL = "lantai_4_non_aerosol"


print("\n### WAR BOT (►__◄) ###\n")
i = 1
for opsi in OpsiForm:
    print(f"[{i}] {opsi.name}")
    i += 1
opsi_form = list(OpsiForm)[int(input("\nPilih GForm: ")) - 1]


form_link_data = {
    "test": "https://docs.google.com/forms/d/e/1FAIpQLSeymRTVNmeLV3Qa46KAikzKoqEd-8K4d__4QRWxeru1kKTnDg",
    "lantai_2": "https://docs.google.com/forms/d/e/1FAIpQLSetrs82QQKByGzNdmELxNs0wzHW032jGNxLvQM28QsO19Y2gA",
    "lantai_4_aerosol": "https://docs.google.com/forms/d/e/1FAIpQLSeWht7ZR4uZTFD6iVKS9NlComTRmbUUPtjG52qHM_yeAVX9Vg",
    "lantai_4_non_aerosol": "https://docs.google.com/forms/d/e/1FAIpQLSesRl_cgAJ9loBxFXY_Ydvx8XZhRB6U7w2wVxdNwalj3Z-0wQ",
}

form_key_data = {
    "test": [
        "entry.1691393102",
        "entry.904420444",
        "entry.390058917",
        "entry.969267933",
        "entry.30694227",
        "entry.1899266012",
    ],
    "lantai_2": [
        "entry.399681891",
        "entry.1081351325",
        "entry.836358015",
        "entry.1566565725",
        "entry.1498675492",
        "entry.1837408953",
    ],
    "lantai_4_aerosol": [
        "entry.1655135643",
        "entry.385343329",
        "entry.848075042",
        "entry.1365019810",
        "entry.513389548",
    ],
    "lantai_4_non_aerosol": [
        "entry.1655135643",
        "entry.385343329",
        "entry.1674626645",
        "entry.1365019810",
        "entry.848075042",
        "entry.513389548",
    ],
}

form_link = form_link_data[opsi_form.value]
form_key = form_key_data[opsi_form.value]

headers = {"Content-Type": "application/x-www-form-urlencoded"}

print()
SUCCESS = False
with open(f"{opsi_form.value}.csv", "r") as csv_input:
    data_input = reader(csv_input, delimiter=";")
    data_header = next(data_input)
    for data in data_input:
        submit_data = dict(zip(form_key, data))
        print("Submitting...")
        while not SUCCESS:
            response = post(
                f"{form_link}/formResponse", data=submit_data, headers=headers
            )

            if "closedform" not in response.url:
                print(f"{opsi_form.name} -> SUCCESS")
                SUCCESS = True
            print("Exiting program in 3 seconds...")
            sleep(3)
