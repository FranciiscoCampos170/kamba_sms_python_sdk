from ..client import KambaClient

class AccountResource:
    def __init__(self, client: KambaClient):
        self._client = client

    def get_balance(self) -> dict:
        return self._client.request("GET", "/credits/balance")

    def get_history(self, limit: int = 100) -> list[dict]:
        return self._client.request("GET", f"/messages?limit={limit}")