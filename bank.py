from __future__ import annotations
import traceback


menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[c] Cadastrar conta
[q] Sair

=> """

AGENCIA = "0001"
LIMITE_SAQUES = 3
usuario_cadastrados: set[str] = set()
contas_cadastradas: dict[str, Conta] = {}


class Conta:
    contas = 0

    def __init__(self, cpf: str):
        if contas_cadastradas.get(cpf) != None:
            raise Exception("CPF já cadastrado")

        self.saldo = 0
        self.contas += 1
        self.conta = f"{self.contas:04}"
        self.agencia = AGENCIA
        self.limite = 500
        self.extrato = ""
        self.numero_saques = 0
        self.cpf = cpf
        usuario_cadastrados.add(cpf)

        contas_cadastradas[cpf] = self


def cadastrar_usuario(cpf):
    pass


def cadastrar_conta(cpf):
    try:
        Conta(cpf)
    except Exception as e:
        print("Erro ao criar conta")
        print(e)
    else:
        print("Conta criada com sucesso")


def depositar(cpf, valor):
    if contas_cadastradas.get(cpf) == None:
        raise Exception("CPF não cadastrado")

    if valor > 0:
        contas_cadastradas[cpf].saldo += valor
        contas_cadastradas[cpf] += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")


def sacar(cpf, valor):
    if contas_cadastradas.get(cpf) == None:
        raise Exception("CPF não cadastrado")

    if contas_cadastradas[cpf].valor > contas_cadastradas[cpf].saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif contas_cadastradas[cpf].valor > contas_cadastradas[cpf].limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif contas_cadastradas[cpf].numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")

    elif contas_cadastradas[cpf].valor > 0:
        contas_cadastradas[cpf].saldo -= valor
        contas_cadastradas[cpf].extrato += f"Saque: R$ {valor:.2f}\n"
        contas_cadastradas[cpf].numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")


def extrato(cpf):
    if contas_cadastradas.get(cpf) == None:
        raise Exception("CPF não cadastrado")

    print("\n================ EXTRATO ================")
    print(
        "Não foram realizadas movimentações."
        if not contas_cadastradas[cpf].extrato
        else contas_cadastradas[cpf].extrato
    )
    print(f"\nSaldo: R$ {contas_cadastradas[cpf].saldo:.2f}")
    print("==========================================")


def main():
    while True:

        opcao = input(menu)

        if opcao == "d":  # Despositar
            cpf = input("Informe o cpf: ")
            valor = float(input("Informe o valor do depósito: "))

        elif opcao == "s":  # Sacar
            cpf = input("Informe o cpf: ")
            valor = float(input("Informe o valor do saque: "))

        elif opcao == "e":  # Extrato
            cpf = input("Informe o cpf: ")
            extrato(cpf)

        elif opcao == "c":  # Criar conta
            cpf = input("Informe o cpf: ")
            cadastrar_conta(cpf)
            print(contas_cadastradas)

        elif opcao == "q":  # Sair
            break

        else:
            print(
                "Operação inválida, por favor selecione novamente a operação desejada."
            )


main()
