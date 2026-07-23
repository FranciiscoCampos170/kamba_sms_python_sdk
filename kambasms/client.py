import json
import urllib.request
import urllib.error
from typing import Any
from .exceptions import KambaError, KambaAPIError

class KambaClient:
    def __init__(self, api_key: str, base_url: str = "https://nexasms-api.onrender.com"):
        if not api_key:
            raise KambaError("A apiKey é obrigatória para inicializar o KambaSMS.")
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")

    def request(self, method: str, endpoint: str, data: dict | None = None) -> dict[str, Any]:
        url = f"{self._base_url}{endpoint}"
        headers = {
            "Content-Type": "application/json",
            "x-api-key": self._api_key,
        }

        body = json.dumps(data).encode("utf-8") if data else None
        req = urllib.request.Request(url, data=body, headers=headers, method=method)

        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            error_body = e.read().decode("utf-8")
            try:
                error_data = json.loads(error_body)
                message = error_data.get("error", "Erro desconhecido na API KambaSMS")
            except json.JSONDecodeError:
                message = "Erro desconhecido na API KambaSMS"
            raise KambaAPIError(message, e.code, error_data if isinstance(error_data, dict) else {}) from e
        except urllib.error.URLError as e:
            raise KambaError(f"Erro de rede: {e.reason}") from e