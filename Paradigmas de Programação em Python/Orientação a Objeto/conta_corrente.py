#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f'Cliente: {self.nome}, CPF: {self.cpf}'


class ContaCorrente:
    def __init__(self, numero, saldo, cliente=None):
        self.numero = numero
        self.saldo = saldo
        self.cliente = cliente

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
        else:
            print('Saldo insuficiente')

    def transferir(self, conta_destino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            conta_destino.depositar(valor)
        else:
            print('Saldo insuficiente')

    def __str__(self):
        return f'Conta {self.numero}, Cliente: {self.cliente}, Saldo: {self.saldo}'


cliente1 = Cliente('Lucas', '123.456.789-00')

conta1 = ContaCorrente(numero=234, cliente=cliente1, saldo=1000)
conta1.depositar(500)
conta1.sacar(200)
conta1.transferir(ContaCorrente(222, 10000), 200)
print(conta1)

