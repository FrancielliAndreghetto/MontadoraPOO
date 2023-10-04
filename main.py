class Montadora:
  def __init__ (self, codigomontadora, estado, razaosocial):
    self.codigomontadora = codigomontadora
    self.estado = estado
    self.razaosocial = razaosocial
  def setCodigomontadora(self, codigomontadora):
    self.codigomontadora = codigomontadora
  def setEstado(self, estado):
    self.estado = estado
  def setRazaosocial(self, razaosocial):
    self.razaosocial = razaosocial
  def getCodigomontadora(self):
    return self.codigomontadora
  def getEstado(self):
    return self.estado
  def getRazaosocial(self):
    return self.razaosocial

class Modelo:
  def __init__(self, codigomodelo, nomemodelo, montadora):
    self.codigomodelo = codigomodelo
    self.nomemodelo = nomemodelo
    self.montadora = montadora
  def setCodigomodelo(self, codigomodelo):
    self.codigomodelo = codigomodelo
  def setNomemodelo(self, nomemodelo):
    self.nomemodelo = nomemodelo
  def setMontadora(self, montadora):
    self.montadora = montadora
  def getCodigomodelo(self):
    return self.codigomodelo
  def getNomemodelo(self):
    return self.nomemodelo
  def getMontadora(self):
    return self.montadora

class Carros:
  def __init__(self, placa, modelo, anofabri):
    self.placa = placa
    self.modelo = modelo
    self.anofabri = anofabri
  def setPlaca(self, placa):
    self.placa = placa
  def setModelo(self, modelo):
    self.modelo = modelo
  def setAnofabri(self, anofabri):
    self.anofabri = anofabri
  def getPlaca(self):
    return self.placa
  def getModelo(self):
    return self.modelo
  def getAnofabri(self):
    return self.anofabri

listamontadoras = []
listacarros = []
listamodelos = []

while True:
  print('-----MENU PRINCIPAL-----')
  print('1 - cadastrar montadora')
  print('2 - Cadastrar modelo')
  print('3 - Cadastrar carros')
  print('4 - Imprimir dados')
  print('5 - Alterar atributo')
  print('6 - sair')
  operação = int(input('Digite a operação que deseja realizar: '))
  if operação == 1:
    while True:
      cadasmont = input('Cadastrar montadora [S/N]:')
      if cadasmont == 'S' or cadasmont == 's':
        codigomontadora = int(input('Digite código montadora: '))
        estado = input('Digite o estado: ')
        razaosocial = input('Digite a razão social: ')
        montadora = Montadora(codigomontadora, estado, razaosocial)
        listamontadoras.append(montadora)
      if cadasmont == 'N' or cadasmont == 'n':
        break
  if operação == 2:
    while True:
      cadasmodel = input('Cadastrar modelo? [S/N]: ')
      if cadasmodel == 'S' or cadasmodel == 's':
        codigomodelo = input('Digite o código do modelo: ')
        nomemodelo = int(input('Digite o nome do modelo: '))
        montadora = input('Digite a montadora: ')
        for x in listamontadoras:
          if montadora == x.getRazaosocial():
            montadora = x
      modelo = Modelo(codigomodelo, nomemodelo, montadora)
      listamodelos.append(modelo)
      if cadasmodel == 'N' or cadasmodel == 'n':
        break

  if operação == 3:
    cadascarro = input('Cadastrar carro? [S/N]: ')
    if cadascarro == 'S' or cadascarro == 's':
      placa = int(input('Digite a placa do veículo: '))
      modelo = input('Digite o modelo: ')
      anofabri = int(input('Digite o ano de fabricação: '))
      for x in listamodelos:
        if modelo == x.getNomemodelo():
          modelo == x
    carro = Carros(placa, modelo, anofabri)
    listacarros.append(carro)
    if cadascarro == 'N' or cadascarro == 'n':
      break

  if operação == 4:
    while True:
      dados = input('Deseja imprimir os dados? [S/N]: ')
      if dados == 'S' or dados == 's':
        print('---DADOS MONTADORA---')
        for montadora in listamontadoras:
          print(f'Codigo da montadora: {montadora.getCodigomontadora()}')
          print(f'Estado: {montadora.getEstado()}')
          print(f'Razão Social: {montadora.getRazaosocial()}')
          print()
          print('---MODELOS---')
          for modelo in listamodelos:
            print(f'Codigo modelo: {modelo.getNomemodelo()}')
            print(f'Nome modelo: {modelo.getNomemodelo()}')
            print(f'Modelo: {modelo.montadora.getRazaosocial()}')
            print()
          for carros in listacarros:
            print('---CARROS---')
            print(f'Placa:{carros.getPlaca()}')
            print(f'Modelo:{carros.modelo.getNomemodelo()}')
            print(f'Ano de fabricação: {carros.getAnofabri()}')
      if dados ==  'N' or dados == 'n':
        break

  if operação == 5:
    print('-----MENU DE ALTERAÇÃO-----')
    print('1 - Alterar atributos da montadora')
    print('2 - Alterar atributos do modelo')
    print('3 - Alterar atributos do carro')
    alteração = int(input('Digite a sua opção: '))

    if alteração == 1:
      altmont = input('Deseja alterar dados da montadora? [S/N]: ')
      if altmont == 'S' or altmont == 's':
        codigoalt = int(input('Digite o código da montadora que deseja alterar o dado: '))
        novocodigo = int(input('Digite o novo código: '))
        novoestado = input('Digite o novo estado: ')
        novarazaosocial = input('Digite a nova razão social: ')
        for montadora in listamontadoras:
          if montadora.getCodigomontadora() == codigoalt:
            if novocodigo != '':
              montadora.setCodigomontadora(int(novocodigo))
            if novoestado != '':
              montadora.setEstado(novoestado)
            if novarazaosocial != '':
              montadora.setRazaosocial(novarazaosocial)
        if altmont == 'N' or altmont == 'n':
          break

    if alteração == 2:
      altmodel = input('Deseja alterar dados do modelo? [S/N]: ')
      if altmodel == 'S' or altmodel == 's':
        codigo = int(input('Digite o código do modelo que deseja alterar o dado: '))
        novocodigo = int(input('Digite o novo código: '))
        novonome = input('Digite o novo nome: ')
        novamontadora = input('Digite a nova montadora: ')
        for modelo in listamodelos:
          if modelo.getCodigomodelo() == codigo:
            if novocodigo != '':
              modelo.setCodigomodelo(int(novocodigo))
            if novonome != '':
              modelo.setNomemodelo(novonome)
            if novamontadora != '':
              modelo.setMontadora(novamontadora)
              for x in listamontadoras:
                if x.getCodigomontadora() == int(novocodigo):
                  listamontadoras = x
        if altmodel == 'N' or altmodel == 'n':
          break

    if alteração == 3:
      altcarro = input('Deseja alterar dados do carro? [S/N]: ')
      if altcarro == 'S' or altcarro == 's':
        placa = int(input('Digite a placa do carro que deseja alterar o dado: '))
        novaplaca = input('Digite a nova placa: ')
        novomodelo = input('Digite o novo modelo: ')
        novoano = input('Digite o novo ano fabricação: ')
        for carros in listacarros:
          if carros.getPlaca() == placa:
            if novaplaca != '':
              carros.setPlaca(int(novaplaca))
            if novomodelo != '':
              for x in listamodelos:
                if x.getNomemodelo() == novomodelo:
                  modelo = x
              carro.setModelo(modelo)
            if novoano != '':
              carro.setAnofabri(novoano)
        if altcarro == 'N' or altcarro == 'n':
          break

  if operação == 6:
    break