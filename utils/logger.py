import json
import os
from datetime import datetime
import logging
LOG_FILE = "reports/test_logs.json"


def log_json(data):
    # Add timestamp
    data["timestamp"] = datetime.now().isoformat()

    # Create file if not exists
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

    # Append log
    with open(LOG_FILE, "r+") as f:
        logs = json.load(f)
        logs.append(data)
        f.seek(0)
        json.dump(logs, f, indent=4)

