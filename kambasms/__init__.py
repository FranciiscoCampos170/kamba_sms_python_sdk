from .client import KambaClient
from .resources.sms import SmsResource
from .resources.account import AccountResource
from .exceptions import KambaError, KambaValidationError, KambaAPIError
from .resources.otp import OtpResource

class KambaSMS(KambaClient):
    def __init__(self, api_key: str, base_url: str = "https://nexasms-api.onrender.com"):
        super().__init__(api_key, base_url)
        self.sms = SmsResource(self)
        self.account = AccountResource(self)
        self.otp = OtpResource(self)

__all__ = ["KambaSMS", "KambaError", "KambaValidationError", "KambaAPIError"]