# 🇦🇴 KambaSMS Python SDK

[![PyPI Version](https://img.shields.io/pypi/v/kambasms.svg)](https://pypi.org/project/kambasms/)
[![Python Version](https://img.shields.io/pypi/pyversions/kambasms.svg)](https://pypi.org/project/kambasms/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

SDK oficial e leve da **KambaSMS** para integração de envio de mensagens SMS em Angola. Zero dependências externas (usa `urllib` nativo), tipagem forte e validações rigorosas para as operadoras angolanas.

## ✨ Funcionalidades

- 🚀 **Zero Dependências**: Utiliza `urllib` nativo do Python — sem `requests`, sem `httpx`.
- 🛡️ **Validação no Cliente**: Deteta números inválidos, URLs ou emojis *antes* de fazer a chamada à API.
- 💎 **Tipagem Forte**: Type hints completos para melhor experiência em IDEs.
- 🔐 **OTP como Serviço**: Autenticação por SMS com rate limiting e expiração incluídos.
- 📦 **MVP Completo**: Envio único, envio em massa, agendamento, OTP e gestão de saldo.

## 📦 Instalação

```bash
pip install kambasms
```
> **Nota:** Requer Python **3.8** ou superior.

## ⚡ Início Rápido

### 1. Inicialização
```python
from kambasms import KambaSMS

client = KambaSMS(api_key="kamba_tua_chave_aqui")
```

### 2. Enviar um SMS Único
```python
sms = client.sms.send(
	to="+244923456789",
	text="O seu código de verificação é 1234.",
	sender_id="KAMBA"  # Opcional: usa o da API Key se omitido
)

print(f"✅ SMS Enviado! ID: {sms['message_id']}")
print(f"Saldo Restante: {sms['remaining_balance']}")
```
### 3. Envio em Massa (Bulk)
```python
response = client.sms.send_bulk(
	name="Campanha Natal 2024",
	sender_id="PROMO",
	text="Feliz Natal! Aproveite 20% de desconto.",
	recipients=[
		"+244923456789",
		"+244933123456",
		"+244943987654"
	]
)

print(f"✅ Job criado! ID: {response['job_id']} | Total: {response['total']}")
```
### 4. Agendar um SMS
```python
from datetime import datetime, timedelta

data_futura = datetime.utcnow() + timedelta(hours=2)

response = client.sms.schedule(
	to="+244923456789",
	text="Lembrete: A sua consulta está marcada para amanhã.",
	sender_id="CLINICA",
	scheduled_at=data_futura  # Aceita datetime ou string ISO 8601
)

print("✅ SMS agendado com sucesso!")
```

### 5. Consultar Saldo e Histórico
# Verificar Saldo
```python
balance = client.account.get_balance()
print(f"Saldo atual: {balance['balance']} SMS")
```
# Ver Histórico (últimos 100 por padrão)
```python
history = client.account.get_history(limit=10)
for msg in history:
	print(f"Para: {msg['to']} | Status: {msg['status']}")
```

## 🔐 OTP Service
Serviço gerido de autenticação por SMS. Rate limiting (3/hora/número), expiração (5min) e validação incluídos.
    
### Enviar OTP
```python
otp = client.otp.send(phone="+244912345678")

print(f"Expira em: {otp['expires_in']} segundos")
# → Expira em: 300 segundos
```
### Verificar OTP

> ⚠️ O endpoint `verify` é **público** — não requer API Key. Pode ser chamado diretamente do frontend.

```python
result = client.otp.verify(
	phone="+244912345678",
	code="123456"
)

if result["success"]:
	print("✅ Código válido!")
else:
	print("❌ Código inválido ou expirado.")
```
### Regras do OTP

| Regra | Valor |
| --- | --- |
| Formato do código | 6 dígitos numéricos |
| Validade | 5 minutos |
| Rate limit (envio) | 3 OTPs/hora por número |
| Rate limit (verificação) | 20 tentativas/15min |
| Custo | 1 crédito SMS por envio |


## 🛡️ Regras de Validação (Específicas para Angola)
O SDK faz validações automáticas no lado do cliente. Se estas regras forem violadas, o SDK lança uma `KambaValidationError` **sem sequer chamar a API**.

1. **Formato do Número**: Deve começar obrigatoriamente com `+244` seguido de exatamente 9 dígitos.
2. **Sem URLs**: Mensagens contendo URLs são rejeitadas (filtradas como spam pelas operadoras).
3. **Sem Emojis**: Caracteres emoji não são suportados.
4. **Limite de Caracteres**: Máximo de 160 caracteres por SMS.

## ⚠️ Tratamento de Erros
```python
from kambasms import KambaSMS, KambaValidationError, KambaAPIError

client = KambaSMS(api_key="kamba_...")

try:
	client.sms.send(
		to="923456789",  # Erro: Falta o +244
		text="Visite www.kambasms.ao 🚀",  # Erro: Tem URL e Emoji
		sender_id="KAMBA"
	)
except KambaValidationError as e:
	# Erro de validação do SDK (dados inválidos)
	print(f"🚫 Dados inválidos: {e}")

except KambaAPIError as e:
	# Erro retornado pelo servidor (saldo insuficiente, rate limit, etc.)
	print(f"🔌 Erro da API ({e.status_code}): {e}")

except Exception as e:
	# Erro de rede ou inesperado
	print(f"💥 Erro inesperado: {e}")
```

## 📚 Documentação Completa
Para mais detalhes sobre endpoints avançados, webhooks de entrega e gestão de conta, consulta a [Documentação Oficial da KambaSMS](https://www.kambasms.ao/dashboard/docs).
    
## 🆘 Suporte
Encontraste um bug ou tens uma sugestão?
    
- Abre uma [Issue neste repositório](https://github.com/FranciiscoCampos170/kamba_sms_python_sdk/issues).
- Contacta a nossa equipa: [support@kambasms.ao](mailto:support@kambasms.ao).
    
## 📄 Licença
Este projeto está licenciado sob a [Licença MIT]().


