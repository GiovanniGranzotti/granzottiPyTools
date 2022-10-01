# granzottiPyTools
Para aprender a usar o pytools

\\[![Build Status](https://travis-ci.com/GiovanniGranzotti/granzottiPyTools.svg?branch=main)](https://travis-ci.com/GiovanniGranzotti/granzottiPyTools)
\\[![Updates](https://pyup.io/repos/github/GiovanniGranzotti/granzottiPyTools/shield.svg)](https://pyup.io/repos/github/GiovanniGranzotti/granzottiPyTools/)
\\[![Python 3](https://pyup.io/repos/github/GiovanniGranzotti/granzottiPyTools/python-3-shield.svg)](https://pyup.io/repos/github/GiovanniGranzotti/granzottiPyTools/)
\\[![codecov](https://codecov.io/gh/GiovanniGranzotti/granzottiPyTools/branch/main/graph/badge.svg?token=SUXUN1E58H)](https://codecov.io/gh/GiovanniGranzotti/granzottiPyTools)
   
Suportada a versão 3 do python.

Para instalar:
```console
py -3 -m venv .venv
source .venv\Scripts\activate
pip install -r requirements-dev.txt
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
* no dia **05/11/2020** Integrei com o PyUp.
* no dia **11/11/2020** Criado o arquivo setup.py.
* no dia **15/11/2020** Feito o realese no pypi e no testpypi.
* no dia **20/11/2020** Atualizando os arqivos e tentando consertar a versão do projeto.
* no dia **20/11/2020** Feito o realese no pypi test server da versão 0.2.2. Links últeis:
    
    [How to upload your package to the Python Package Index (PyPI) test server](https://kynan.github.io/blog/2020/05/23/how-to-upload-your-package-to-the-python-package-index-pypi-test-server) 
    
    [Using TestPyPI](https://packaging.python.org/guides/using-testpypi/)

* no dia **24/11/2020** Instalação do Pytest.
* no dia **25/11/2020** Criado arquivo para testes e configurado o pytest.
* no dia **27/11/2020** Adicionado cobertura de código no projeto. Link útil:

    [codecov overview](https://pytest-cov.readthedocs.io/en/latest/readme.html#installation)
    
* no dia **27/11/2020** Aprendi TDD e Baby Steps.
* no dia **30/11/2020** Aprendi a usar o Parametrize.
* no dia **03/12/2020** Aprendi a criar exceções.
* no dia **05/12/2020** Aprendi a isolar testes.
* no dia **06/12/2020** Aprendi a usar Setup e Tear down com Fixture.
* no dia **08/12/2020** Criei o arquivo Conftest.
* no dia **10/12/2020** Produção de código testável.
* no dia **12/12/2020** Injeção de dependências.
* no dia **14/12/2020** Uso do Mock.
* no dia **19/12/2020** Aprendi a isolar testes com fixture e mock.
* no dia **20/12/2020** Aprendi a usar a biblioteca pytest-mock.
* no dia **17/01/2021** Terminado o Pytools.
