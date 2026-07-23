from kambasms import KambaSMS, KambaValidationError, KambaAPIError

client = KambaSMS(api_key="kamba_tua_chave_de_teste_aqui")

try:
    balance = client.account.get_balance()
    print(f"✅ Saldo atual: {balance['balance']} SMS")

    sms = client.sms.send(
        to="+244923456789",
        text="Teste do SDK Python KambaSMS.",
        sender_id="KAMBA"
    )
    print(f"✅ SMS Enviado! ID: {sms['message_id']} | Saldo: {sms['remaining_balance']}")

    # Teste de validação (deve falhar no cliente)
    try:
        client.sms.send(to="923456789", text="Visite www.kambasms.ao 🚀", sender_id="KAMBA")
    except KambaValidationError as e:
        print(f"🛡️ Validação funcionou: {e}")

except KambaAPIError as e:
    print(f"❌ Erro API ({e.status_code}): {e}")
except Exception as e:
    print(f"❌ Erro: {e}")