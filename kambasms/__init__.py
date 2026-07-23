from .client import KambaClient
from .resources.sms import SmsResource
from .resources.account import AccountResource
from .exceptions import KambaError, KambaValidationError, KambaAPIError

class KambaSMS(KambaClient):
    def __init__(self, api_key: str, base_url: str = "https://nexasms-api.onrender.com"):
        super().__init__(api_key, base_url)
        self.sms = SmsResource(self)
        self.account = AccountResource(self)

__all__ = ["KambaSMS", "KambaError", "KambaValidationError", "KambaAPIError"]