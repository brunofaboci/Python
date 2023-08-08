def cria_conta(params=None):
    if params is None:
        params = {"numero": 00, "titular": "", "saldo": 0, "limite": 0}
    conta = {"numero":  params["numero"],
             "titular": params["titular"],
             "saldo":   params["saldo"],
             "limite":  params["limite"]}
    return conta


def deposita(conta, valor):
    conta["saldo"] += valor


def saca(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    return conta["saldo"]


dados_conta = {"numero": 123, "titular": "Bruno", "saldo": 150, "limite": 1000}
conta_corrente = cria_conta(dados_conta)
print(extrato(conta_corrente))
deposita(conta_corrente, 100)
print(extrato(conta_corrente))
saca(conta_corrente, 80)
print(extrato(conta_corrente))
