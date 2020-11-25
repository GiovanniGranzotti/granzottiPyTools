# granzottiPyTools
Para aprender a usar o pytools

[![Build Status](https://travis-ci.com/GiovanniGranzotti/libpythonpro.svg?branch=master)](https://travis-ci.com/GiovanniGranzotti/libpythonpro)
[![Updates](https://pyup.io/repos/github/GiovanniGranzotti/granzottiPyTools/shield.svg)](https://pyup.io/repos/github/GiovanniGranzotti/granzottiPyTools/)
[![Python 3](https://pyup.io/repos/github/GiovanniGranzotti/granzottiPyTools/python-3-shield.svg)](https://pyup.io/repos/github/GiovanniGranzotti/granzottiPyTools/)
   
Suportada a versão 3 do python.

Para instalar:
```console
py -3 -m venv .venv
source .venv\Scripts\activate
pip install -r requiremets-dev.txt
```

Para conferir qualidade do código:
```console
flake8
```

Para fazer upload no pypi test server:
```console
twine upload --repository testpypi dist\*
```

Para instalar a partir do pypi test server:
```console
pip install -i https://test.pypi.org/simple/ libgranzottiPyTools
```

* no dia **27/10/2020** aprendi a usar o gitignore. Os links úteis foram:

    [Criar gitignore](https://medium.com/@devmasterteam/touch-para-criar-um-arquivo-gitignore-9bb2d453ac53)

    [Editar e salvar um arquivo gitignore](https://pt.stackoverflow.com/questions/254320/como-salvar-e-sair-no-vim/254322#254322?newreg=6321e3c5676941688ba522414f4b6af9)
 
* no dia **28/10/2020** aprendi a instalar bibliotecas de terceiros.
* no dia **29/10/2020** aprendi a criar o arquivo requirements para instalação das dependêcias.
* no dia **29/10/2020** aprendi a usar o flake8.
* no dia **29/10/2020** configurei o travis CI.
* no dia **5/11/2020** Integrei com o PyUp.
* no dia **11/11/2020** Criado o arquivo setup.py.
* no dia **15/11/2020** Feito o realese no pypi e no testpypi.
* no dia **20/11/2020** Atualizando os arqivos e tentando consertar a versão do projeto.
* no dia **20/11/2020** Feito o realese no pypi test server da versão 0.2.2. Links últeis:
    
    [How to upload your package to the Python Package Index (PyPI) test server](https://kynan.github.io/blog/2020/05/23/how-to-upload-your-package-to-the-python-package-index-pypi-test-server) 
    
    [Using TestPyPI](https://packaging.python.org/guides/using-testpypi/)

* no dia **24/11/2020** Instalação do Pytest.