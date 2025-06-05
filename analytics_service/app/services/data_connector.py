import requests
from datetime import datetime

class DataConnector:
    DEAL_SERVICE_URL = "http://deal-service:8000"
    CUSTOMER_SERVICE_URL = "http://customer-service:8001"

    @staticmethod
    def get_deals(date_range):
        response = requests.get(
            f"{DEAL_SERVICE_URL}/deals",
            params={"start_date": date_range.start_date, "end_date": date_range.end_date}
        )
        return response.json()

    @staticmethod
    def get_customers():
        response = requests.get(f"{CUSTOMER_SERVICE_URL}/customers")
        return response.json()