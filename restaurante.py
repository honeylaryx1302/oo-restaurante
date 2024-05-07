class restaurante:
    def __init__(self,nome,categoria):
        self.nome =  nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f'{self.nome}' | {self.categoria}
    

restaurante_praca =  restaurante('praça','Gourmet')
restaurante_pizza = restaurante('pizza','Italiana')

restaurantes =[restaurante_pizza,restaurante_praca]


print(restaurante_praca)
print(restaurante_pizza)