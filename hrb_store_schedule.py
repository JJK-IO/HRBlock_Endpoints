import json
from datetime import datetime, date, time

import requests

office_id = 16569
system_request = requests.get("http://www.hrblock.com/gateway/services/tpf/meta/appmeta")
contact_id = json.loads(system_request.text)['response']['contactId']

payload = {
    "officeId": office_id,
    "contactId": contact_id
}

employee_request = requests.post("http://www.hrblock.com/gateway/services/tpf/taxpro/basicinfo-bm", json=payload)
employee_list = []

for employee in json.loads(employee_request.text)['response']['taxProList']:
    employee_list.append(employee['employeeId'])

date_formatted = date.strftime(date.today(), "%Y-%m-%d")
cur_hour = time.strftime(datetime.now().time(), "%H")

payload = {
    "numberOfSlots": 4,
    "duration": "",
    "clientRating": 1,
    "earliestAppointment": True,
    "multiState": False,
    "appointmentServiceType": "OFFICE",
    "spanishIndicator": False,
    "slotFilter": "TP",
    "officeList": [office_id],
    "employeeList": [employee_list],
    "appointmentStartDateTime": date_formatted + "T08:00:00",
    "appointmentEndDateTime": date_formatted + "T22:00:00",
    "contactId": contact_id,
    "appointmentStartDateTimeUser": date_formatted + "T" + cur_hour + ":00:00",
    "serviceType": 1,
    "catpFlowType": "CATPNonBestMatch",
    "employeeRole": 1
}

appointment_request = requests.post("http://www.hrblock.com/gateway/services/tpf/appointment/available-slots",
                                    json=payload)
appointment_list = json.loads(appointment_request.text)['response']['officeAppointmentList'][0]['appointmentList']
print(appointment_list)
