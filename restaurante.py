class Restaurante:
    restaurantes = []

    def __init__(self,nome,categoria):
        self.nome =  nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome}' | {self.categoria}

    def listar_restaurantes():
            print(f'{"nome do restaurante".ljust(25)} | {"categoria".ljust(25)} | {"status".ljust(25)}')
            for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)}')
            
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza express', 'Italiana')

Restaurante.listar_restaurantes()