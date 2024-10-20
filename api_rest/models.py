from django.db import models
from django.utils.timezone import now

#produtos
class Produtos(models.Model):
    nome = models.CharField(max_length=255, default='')
    descricao = models.TextField(default='', blank=True)
    quantidade = models.IntegerField(default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateField(auto_now_add=True)
    editado_em = models.DateField(auto_now=True)
    
    def __str__(self):
        return f'Nome: {self.nome} / Quantidade: {self.quantidade} / Preço: {self.preco}'

    def editar_produto(self, edit_nome, edit_descricao, edit_quantidade, edit_preco):
        if self.id is None:
            return "Erro: produto não encontrado"
        self.nome = edit_nome
        self.descricao = edit_descricao
        self.quantidade = edit_quantidade
        self.preco = edit_preco
        self.editado_em = now()
        self.save()
        return f'Produto {self.nome} editado com sucesso'

    def excluir_produto(self):
        if id is None:
            return "Erro: produto não encontrado"
        nome_produto = self.nome
        self.delete()
        return f'Produto {nome_produto} excluído com sucesso'

#clientes
class Clientes(models.Model):
    nome = models.CharField(max_length=255, default='')
    telefone = models.CharField(max_length=255, default='')

    def __str__(self):
        return f'Nome: {self.nome} / Telefone: {self.telefone}'
    
    def editar_cliente(self,edit_nome, edit_telefone):
        if self.id is None:
            return "Erro: cliente não encontrado"
        self.nome = edit_nome
        self.telefone = edit_telefone
        self.save()
        return f'Cliente: {self.nome} editado com sucesso'
    
    def excluir_cliente(self):
        if id is None:
            return "Erro: cliente não encontrado"
        nome_cliente = self.nome
        self.delete()
        return f'Produto {nome_cliente} excluído com sucesso'

#pedidos
class Pedidos(models.Model):
    nome = models.CharField(default='', max_length=255)
    descricao = models.TextField(default='', blank=True)
    produto = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default = 0)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateField(auto_now_add=True)
    editado_em = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"Pedido {self.nome} / Produto: {self.produto.nome} / Quantidade: {self.quantidade} / Preço: {self.preco}"
    
    def editar_pedido(self, edit_nome, edit_descricao, edit_quantidade, edit_preco):
        if self.id is None:
            return "Erro: pedido não encontrado"
        self.nome = edit_nome
        self.descricao = edit_descricao
        self.quantidade = edit_quantidade
        self.preco = edit_preco
        self.editado_em = now()
        self.save()
        return f'Pedido: {self.id} - {self.nome}: editado com sucesso'
    
    def excluir_pedido(self):
        if id is None:
            return "Erro: pedido não encontrado"
        nome_pedido = self.nome
        self.delete()
        return f'Produto {nome_pedido} excluído com sucesso'