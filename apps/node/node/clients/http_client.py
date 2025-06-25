from typing import Any, Dict

from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from .exceptions import HttpPostException
from .models import HttpPostResponse


class HttpClient:
    def __init__(self):
        self.http = Session()

    def add_retry_strategy(
        self,
        retries: int = 3,
        status: int = 429,
        backoff_factor: int = 2,
        mount: str = "http://",
    ):
        self.http.mount(
            mount,
            HTTPAdapter(
                max_retries=Retry(
                    total=retries, backoff_factor=backoff_factor, status=status
                )
            ),
        )

    def post(
        self, route: str, body: Dict[Any, Any], headers: Dict[str, str]
    ) -> HttpPostResponse:
        try:
            print(f"Seiding post request to {route} | {body} | {headers}")
            raw_response = self.http.post(route, json=body, headers=headers)

            raw_response.raise_for_status()

            return HttpPostResponse(
                status=raw_response.status_code, body=raw_response.json()
            )

        except Exception as e:
            print(f"Failed to send or decode post request - {e}")
            raise HttpPostException(e)
