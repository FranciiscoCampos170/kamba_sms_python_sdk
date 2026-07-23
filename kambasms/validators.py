import re
from .exceptions import KambaValidationError

_PHONE_REGEX = re.compile(r'^\+244[0-9]{9}$')
_URL_REGEX = re.compile(r'https?://|www\.|\.com\b|\.ao\b|\.net\b|\.org\b|\.co\b|\.io\b', re.IGNORECASE)
_EMOJI_REGEX = re.compile(
    r'[\U0001F600-\U0001F64F\U0001F300-\U0001F5FF\U0001F680-\U0001F6FF\U00002600-\U000026FF\U00002700-\U000027BF]'
)

def validate_angolan_phone(phone: str) -> None:
    if not _PHONE_REGEX.match(phone):
        raise KambaValidationError(
            f"Número de telefone inválido: '{phone}'. Deve ser +244 seguido de 9 dígitos (ex: +244923456789)."
        )

def validate_message_content(text: str) -> None:
    if _URL_REGEX.search(text):
        raise KambaValidationError(
            "Mensagens com links ou URLs não são permitidas. As operadoras angolanas filtram este conteúdo como spam."
        )
    if len(text) > 160:
        raise KambaValidationError(
            f"Mensagem demasiado longa ({len(text)}/160 caracteres). O limite é de 160 caracteres por SMS."
        )
    if _EMOJI_REGEX.search(text):
        raise KambaValidationError(
            "Emojis não são suportados. As operadoras angolanas podem bloquear ou cobrar múltiplos SMS por mensagens com emojis."
        )