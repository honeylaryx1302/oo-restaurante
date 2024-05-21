from restaurante import Restaurante

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican food', 'Mexicana')
restaurante_japones = Restaurante('japa', 'japonesa')

restaurante_mexicano.alternar_estado()


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()