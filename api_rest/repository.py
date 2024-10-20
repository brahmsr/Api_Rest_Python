from django import models
from django.core.exceptions import ObjectDoesNotExist
from .models import Produtos, Pedidos, Clientes

class ProdutoRepository:
    
    def criar_produto(self, nome, descricao, quantidade, preco):
        produto = Produtos.objects.create(
            nome= nome,
            descricao= descricao,
            quantidade= quantidade,
            preco= preco
        )
        return produto
    
    def obter_produto_por_id(self, produto_id):
        try:
            return Produtos.objects.get(id=produto_id)
        except ObjectDoesNotExist:
            return None
    
    def editar_produto(self, produto_id, nome, descricao, quantidade, preco):
        produto = self.obter_produto_por_id(produto_id)
        if produto is None:
            return "Erro: produto não encontrado"
        produto.nome = nome
        produto.descricao = descricao
        produto.quantidade = quantidade
        produto.preco = preco
        produto.save()
        return f'Produto {produto.nome} editado com sucesso'

    def excluir_produto(self, produto_id):
        produto = self.obter_produto_por_id(produto_id)
        if produto is None:
            return "Erro: produto não encontrado"
        produto.delete()
        return f'Produto {produto.nome} excluído com sucesso'

    def listar_todos_produtos(self):
        return Produtos.objects.all()
# -----------------------------------------------------------------------------
#pedidos
class PedidoRepository:

    def criar_pedido(self, nome, descricao, produto_id, quantidade, preco):
        try:
            produto = Produtos.objects.get(id=produto_id)
        except ObjectDoesNotExist:
            return "Erro: produto não encontrado"

        pedido = Pedidos.objects.create(
            nome=nome,
            descricao=descricao,
            produto=produto,
            quantidade=quantidade,
            preco=preco
        )
        
        return pedido

    def obter_pedido_por_id(self, pedido_id):
        try:
            return Pedidos.objects.get(id=pedido_id)
        except ObjectDoesNotExist:
            return None

    def editar_pedido(self, pedido_id, nome, descricao, quantidade, preco):
        pedido = self.obter_pedido_por_id(pedido_id)
        if pedido is None:
            return "Erro: pedido não encontrado"
        pedido.nome = nome
        pedido.descricao = descricao
        pedido.quantidade = quantidade
        pedido.preco = preco
        pedido.save()
        return f'Pedido {pedido.nome} editado com sucesso'

    def excluir_pedido(self, pedido_id):
        pedido = self.obter_pedido_por_id(pedido_id)
        if pedido is None:
            return "Erro: pedido não encontrado"
        pedido.delete()
        return f'Pedido {pedido.nome} excluído com sucesso'

    def listar_todos_pedidos(self):
        return Pedidos.objects.all()
# -----------------------------------------------------------------------------
#clientes
class ClienteRepository:

    def criar_cliente(self, nome, telefone):
        cliente = Clientes.objects.create(
            nome=nome,
            telefone=telefone
        )
        return cliente

    def obter_cliente_por_id(self, cliente_id):
        try:
            return Clientes.objects.get(id=cliente_id)
        except ObjectDoesNotExist:
            return None

    def editar_cliente(self, cliente_id, nome, telefone):
        cliente = self.obter_cliente_por_id(cliente_id)
        if cliente is None:
            return "Erro: cliente não encontrado"
        cliente.nome = nome
        cliente.telefone = telefone
        cliente.save()
        return f'Cliente {cliente.nome} editado com sucesso'
    
    def excluir_cliente(self, cliente_id):
        cliente = self.obter_cliente_por_id(cliente_id)
        if cliente is None:
            return "Erro: cliente não encontrado"
        cliente.delete()
        return f'Cliente {cliente.nome} excluído com sucesso'

    def listar_todos_clientes(self):
        return Clientes.objects.all()
