from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    def __str__(self):
        return f"{self.endereco}"

class Imovel(models.Model):
    clienteFk = models.ForeignKey(Cliente,related_name="ClientetoImovel",on_delete=models.CASCADE)
    endereco = models.TextField()
    largura = models.DecimalField(max_digits=7, decimal_places=2)
    comprimento = models.DecimalField(max_digits=7, decimal_places=2)
    def __str__(self):
        return f"{self.endereco}"

class Fatura(models.Model):
    clienteFk = models.ForeignKey(Cliente, related_name="ClienteToFatura",on_delete=models.CASCADE)
    imovelFk = models.ForeignKey(Imovel, related_name="ImovelToFatura",on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.clienteFk.nome}"
