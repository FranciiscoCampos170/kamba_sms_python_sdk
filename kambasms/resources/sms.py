from datetime import datetime
from ..client import KambaClient
from ..validators import validate_angolan_phone, validate_message_content

class SmsResource:
    def __init__(self, client: KambaClient):
        self._client = client

    def send(self, to: str, text: str, sender_id: str | None = None) -> dict:
        validate_angolan_phone(to)
        validate_message_content(text)
        payload = {"to": to, "text": text}
        if sender_id:
            payload["sender_id"] = sender_id
        return self._client.request("POST", "/messages/send", payload)

    def send_bulk(self, name: str, sender_id: str, text: str, recipients: list[str]) -> dict:
        validate_message_content(text)
        for phone in recipients:
            validate_angolan_phone(phone)
        if len(recipients) > 1000:
            raise ValueError("O limite máximo é de 1000 destinatários por envio em massa.")
        return self._client.request("POST", "/messages/bulk", {
            "name": name, "sender_id": sender_id, "text": text, "recipients": recipients
        })

    def schedule(self, to: str, text: str, sender_id: str, scheduled_at: str | datetime) -> dict:
        validate_angolan_phone(to)
        validate_message_content(text)
        ts = scheduled_at.isoformat() if isinstance(scheduled_at, datetime) else scheduled_at
        return self._client.request("POST", "/messages/schedule", {
            "to": to, "text": text, "sender_id": sender_id, "scheduled_at": ts
        })