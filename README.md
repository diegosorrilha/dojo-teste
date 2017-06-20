# dojo-teste

Coding Dojo da Comunidade WTTD


## Como brincar?

1. Faça o clone desse repositório
 
`git clone git@github.com:diegosorrilha/wttd-dojo.git`

2. Crie um virtualenv com Python 3.5
3. Ative seu virtualenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes.

```console
git clone git@github.com:diegosorrilha/eventex-diegosorrilha.git wttd
cd wttd 
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements-dev.txt
cp contrib/env-sample .env
python manage.py test
```
