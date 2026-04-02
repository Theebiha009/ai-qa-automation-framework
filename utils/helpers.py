import json
import csv

def load_json_data(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

def load_csv_data(file_path):
    data = []
    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convert types (IMPORTANT)
            row["totalprice"] = int(row["totalprice"])
            row["depositpaid"] = row["depositpaid"].lower() == "true"
            data.append(row)
    return data

def build_payload(data):
    return {
        "firstname": data["firstname"],
        "lastname": data["lastname"],
        "totalprice": data["totalprice"],
        "depositpaid": data["depositpaid"],
        "bookingdates": {
            "checkin": data["checkin"],
            "checkout": data["checkout"]
        },
        "additionalneeds": data["additionalneeds"]
    }