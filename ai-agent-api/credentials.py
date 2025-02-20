import os

# Set environment variables or replace with actual values
HOST = os.getenv("PF_HOST", "your_host")
USERNAME = os.getenv("PF_USERNAME", "your_username")
PASSWORD = os.getenv("PF_PASSWORD", "your_password")
BASE_URL = f"https://{HOST}:9999/pf-admin-api/v1"
# BASE_URL = f"http://127.0.0.1:8000"

HEADERS = {
    "X-Xsrf-Header": "PingFederate",
    "Content-Type": "application/json"
}

