from ..client import KambaClient

class OtpResource:
    def __init__(self, client: KambaClient):
        self._client = client

    def send(self, phone: str) -> dict:
        return self._client.request("POST", "/otp/send", {"phone": phone})

    def verify(self, phone: str, code: str) -> dict:
        return self._client.request("POST", "/otp/verify", {
            "phone": phone, "code": code
        })