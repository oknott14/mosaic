from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class NetworkApi:
    def __init__(self):
        retry_strategy = Retry(total=5, backoff_factor=2, status=[429, 500])
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.http = Session()
        self.http.mount("http://", adapter)
