import requests
import json
from datetime import datetime

system_details = requests.get("http://www.hrblock.com/gateway/services/tpf/meta/appmeta")
office_details = requests.get("http://www.hrblock.com/locator-service/officeservice/tpf/001/data/getOfficeDetailsByTaxID?oid=16569")

system_date = json.loads(system_details.text)['response']['systemDate']

schedule = {
    "curWeek": {
        "sun": {
            "date": datetime.strptime(json.loads(office_details.text)['ftLocations'][0]['week1_sun'].split("<br>")[0]+" / "+system_date.split("-")[0], '%m / %d / %Y'),
            "hours": json.loads(office_details.text)['ftLocations'][0]['week1_sun'].split("<br>")[1]
        },
        "mon": {
            "date": datetime.strptime(json.loads(office_details.text)['ftLocations'][0]['week1_mon'].split("<br>")[0]+" / "+system_date.split("-")[0], '%m / %d / %Y'),
            "hours": json.loads(office_details.text)['ftLocations'][0]['week1_mon'].split("<br>")[1]
        },
        "tues": {
            "date": datetime.strptime(json.loads(office_details.text)['ftLocations'][0]['week1_tues'].split("<br>")[0]+" / "+system_date.split("-")[0], '%m / %d / %Y'),
            "hours": json.loads(office_details.text)['ftLocations'][0]['week1_tues'].split("<br>")[1]
        },
        "wed": {
            "date": datetime.strptime(json.loads(office_details.text)['ftLocations'][0]['week1_wed'].split("<br>")[0]+" / "+system_date.split("-")[0], '%m / %d / %Y'),
            "hours": json.loads(office_details.text)['ftLocations'][0]['week1_wed'].split("<br>")[1]
        },
        "thur": {
            "date": datetime.strptime(json.loads(office_details.text)['ftLocations'][0]['week1_thur'].split("<br>")[0]+" / "+system_date.split("-")[0], '%m / %d / %Y'),
            "hours": json.loads(office_details.text)['ftLocations'][0]['week1_thur'].split("<br>")[1]
        },
        "fri": {
            "date": datetime.strptime(json.loads(office_details.text)['ftLocations'][0]['week1_fri'].split("<br>")[0]+" / "+system_date.split("-")[0], '%m / %d / %Y'),
            "hours": json.loads(office_details.text)['ftLocations'][0]['week1_fri'].split("<br>")[1]
        },
        "sat": {
            "date": datetime.strptime(json.loads(office_details.text)['ftLocations'][0]['week1_sat'].split("<br>")[0]+" / "+system_date.split("-")[0], '%m / %d / %Y'),
            "hours": json.loads(office_details.text)['ftLocations'][0]['week1_sat'].split("<br>")[1]
        }
    },
    "nextWeek": {
        "sun": {
            "date": datetime.strptime(json.loads(office_details.text)['ftLocations'][0]['week2_sun'].split("<br>")[0]+" / "+system_date.split("-")[0], '%m / %d / %Y'),
            "hours": json.loads(office_details.text)['ftLocations'][0]['week2_sun'].split("<br>")[1]
        },
        "mon": {
            "date": datetime.strptime(json.loads(office_details.text)['ftLocations'][0]['week2_mon'].split("<br>")[0]+" / "+system_date.split("-")[0], '%m / %d / %Y'),
            "hours": json.loads(office_details.text)['ftLocations'][0]['week2_mon'].split("<br>")[1]
        },
        "tues": {
            "date": datetime.strptime(json.loads(office_details.text)['ftLocations'][0]['week2_tues'].split("<br>")[0]+" / "+system_date.split("-")[0], '%m / %d / %Y'),
            "hours": json.loads(office_details.text)['ftLocations'][0]['week2_tues'].split("<br>")[1]
        },
        "wed": {
            "date": datetime.strptime(json.loads(office_details.text)['ftLocations'][0]['week2_wed'].split("<br>")[0]+" / "+system_date.split("-")[0], '%m / %d / %Y'),
            "hours": json.loads(office_details.text)['ftLocations'][0]['week2_wed'].split("<br>")[1]
        },
        "thur": {
            "date": datetime.strptime(json.loads(office_details.text)['ftLocations'][0]['week2_thur'].split("<br>")[0]+" / "+system_date.split("-")[0], '%m / %d / %Y'),
            "hours": json.loads(office_details.text)['ftLocations'][0]['week2_thur'].split("<br>")[1]
        },
        "fri": {
            "date": datetime.strptime(json.loads(office_details.text)['ftLocations'][0]['week2_fri'].split("<br>")[0]+" / "+system_date.split("-")[0], '%m / %d / %Y'),
            "hours": json.loads(office_details.text)['ftLocations'][0]['week2_fri'].split("<br>")[1]
        },
        "sat": {
            "date": datetime.strptime(json.loads(office_details.text)['ftLocations'][0]['week2_sat'].split("<br>")[0]+" / "+system_date.split("-")[0], '%m / %d / %Y'),
            "hours": json.loads(office_details.text)['ftLocations'][0]['week2_sat'].split("<br>")[1]
        }
    }
}
print(schedule)
