# Gerenciador de Cadastro de Montadoras, Modelos e Carros em Python

Este código Python é um sistema de cadastro de montadoras, modelos de carros e carros. Ele permite ao usuário realizar várias operações, incluindo o cadastro de montadoras, modelos de carros e carros, a impressão de dados cadastrados, a alteração de atributos e a saída do programa. Abaixo, está uma descrição das principais classes e funcionalidades do código:

Classes Principais:

Montadora: Esta classe representa uma montadora de carros e possui os atributos codigomontadora, estado e razaosocial. Ela possui métodos para configurar e obter esses atributos.

Modelo: Esta classe representa um modelo de carro e inclui os atributos codigomodelo, nomemodelo e montadora. Ela também possui métodos para configurar e obter esses atributos.

Carros: Esta classe representa um carro específico com os atributos placa, modelo e anofabri. Ela tem métodos para configurar e obter esses atributos.

Listas de Armazenamento:

listamontadoras: Uma lista para armazenar objetos da classe Montadora.
listacarros: Uma lista para armazenar objetos da classe Carros.
listamodelos: Uma lista para armazenar objetos da classe Modelo.
Funcionalidades Principais:

O código começa com um menu principal que permite ao usuário escolher entre várias operações.
Operações incluem o cadastro de montadoras, modelos de carros e carros, a impressão de dados cadastrados, a alteração de atributos e a saída do programa.
Para cada operação de cadastro (montadora, modelo e carro), o código solicita ao usuário os detalhes relevantes e cria objetos das respectivas classes para armazenar os dados.
A operação de impressão de dados exibe informações sobre montadoras, modelos e carros cadastrados.
A operação de alteração permite ao usuário escolher entre alterar atributos de montadoras, modelos ou carros e atualizar os dados correspondentes nas listas.
Notas Adicionais:

O código possui loops while aninhados para fornecer um fluxo contínuo de operações até que o usuário decida sair.
Os objetos de montadoras e modelos são vinculados aos carros cadastrados para representar as relações entre eles.
Esta descrição pode ser usada como uma breve explicação do código no GitHub para ajudar os outros a entenderem sua finalidade e funcionalidade. Certifique-se de fornecer informações adicionais, como pré-requisitos, instruções de uso e exemplos de entrada/saída, se necessário.