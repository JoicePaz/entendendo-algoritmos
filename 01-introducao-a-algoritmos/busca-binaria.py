def busca_binaria(lista, item):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:

      meio = (inicio + fim) // 2
      chute = lista[meio]

      if chute == item:
        return meio

      if chute > item:
        fim = meio - 1
      else:
        inicio = meio + 1

    return None


if __name__ == '__main__':
    lista = [1, 3, 5, 7, 9]
    print(busca_binaria(lista, 5))  #

