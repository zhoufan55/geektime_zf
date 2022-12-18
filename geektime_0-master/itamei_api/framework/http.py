import re
from dataclasses import dataclass
import requests
from requests import Response as RequestsResponse


@dataclass
class Request:
    method: str = None
    host: str = None
    path: str = None
    query: dict = None
    headers: dict = None
    type: str = None
    data: dict = None

    def send(self):
        raw = None
        requests_response = requests.request(
            method=self.method,
            url=self.host + self.path,
            headers=self.headers,
            data=raw,
            auth=None,
            # proxies={
            #     'http': 'http://127.0.0.1:8080',
            #     'https': 'http://127.0.0.1:8080'
            # },
            verify=False
        )
        r = Response(requests_response)
        return r


@dataclass
class Response:
    def __int__(self, requests_response):
        self.r: RequestsResponse = requests_response

    def json(self):
        return self.r.json()

    @property
    def data(self):
        return self.r.text

    @property
    def status_code(self):
        return self.r.status_code
