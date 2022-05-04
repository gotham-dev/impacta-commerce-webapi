# ImpactaCommerce - Web API

API REST para o e-commerce fictício da disciplica Framework Full Stack.

## Desenvolvimento

### Configurando ambiente python

1. Crie um ambiente virtual 
```sh 
# Cria
python3 -m venv venv

#Ativa
. venv/bin/activate
```
2. Instale todas as dependências necessárias listadas em `requirements.txt`
```sh
pip3 install -r requirements.txt
```
3. Execute os comandos a seguir para executar localmente em modo de desenvolvimento.

```sh
# Para habilitar o hot reload e outras configs quando em desenvolvimento
export FLASK_ENV=development

# Para informar onde está sua aplicação flask
export FLASK_APP=api

# Para inicializar a aplicação
python3 run.py
```