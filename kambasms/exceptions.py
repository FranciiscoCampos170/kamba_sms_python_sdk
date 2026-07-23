class KambaError(Exception):
    """Exceção base da KambaSMS."""
    pass

class KambaValidationError(KambaError):
    """Erro de validação no lado do cliente."""
    pass

class KambaAPIError(KambaError):
    """Erro retornado pela API KambaSMS."""
    def __init__(self, message: str, status_code: int, details: dict | None = None):
        super().__init__(message)
        self.status_code = status_code
        self.details = details or {}