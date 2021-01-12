# Descrição
> Separação silábica simples usando PyHyphen

## Requerimentos

Para instalar as dependências é necessário ter no máximo o python3.6. No python3.7 existe um problema na instalação do pyhyphen

OS X e Linux:

```sh
sudo apt-get install python3-pip
sudo pip3 install virtualenv
```
## Instalação

OS X e Linux

Crie um novo ambiente virtual para o Python3.6:

```sh
cd $SEU_DIRETORIO_DO_PROJETO
virtualenv -p /usr/bin/python3.6 venv
```

O $SEU_DIRETORIO_DO_PROJETO nada mais é onde está salvo o arquivo main.py.

Instale as libs necessárias:

```sh
source venv/bin/activate
pip install -r requirements.txt
```

## Como usar

Execute o código abaixo, como mostra o comando abaixo, e informe qual palavra deseja fazer a separação silábica

```sh
python main.py
```

## Licença

Este projeto é licenciado sobre os termos da MIT License (veja o arquivo
LICENSE).