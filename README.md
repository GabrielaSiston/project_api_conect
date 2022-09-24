# rpchecker
O projeto é um aplicativo que verifica se um ou mais sites estão online em um determinado momento. O aplicativo obterá uma lista de URLs de destino na linha de comando e os verificará quanto à conectividade de forma síncrona.

# 1. Instalação

### Crie um ambiente virtual em Python 
$ python -virtualenv -p python3 myvenv

$ source myvenv/bin/activate


## 2. Instale os "requirements"
(myvenv) $ python -m pip install -r requirements.txt


## 3. Execute o projeto
(myvenv) $ python -m rpchecker -u python.org pypi.org docs.python.org

The status of "python.org" is: "O pai tá on!"

## 4. Features
rphecker fornece as seguintes opções:

-u ou --urls pega um ou mais URLs e verifica se eles estão online.

-f ou --input-file pega um arquivo contendo uma lista de URLs para verificar.


## 5. Sobre o autor
Gabriela Siston 
Linkedin: https://www.linkedin.com/in/gabriela-siston-dos-santos-257479236/

## 6. Licensa 

Para mais informações consultar projeto original em : <https://realpython.com/site-connectivity-checker-python/#conclusion>

