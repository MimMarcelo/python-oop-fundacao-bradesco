class Main: # A classe Main não possui atributos
  pass

print("Testando o projeto")


from classes.Cliente import Cliente
from classes.Conta import Conta

c1 = Cliente("Ana", "99999-9999")
print("Nome:", c1.nome, "Telefone:", c1.telefone)

conta = Conta(c1, 6565, 0)
print("Abrindo conta do cliente:", conta.titular.nome)
print("Conta:", conta.numero, "Saldo: %.2f" %conta.saldo)



