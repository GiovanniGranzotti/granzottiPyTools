import pytest

from libgranzottiPyTools.spam.db import Conexao
from libgranzottiPyTools.spam.modelos import Usuario


@pytest.fixture
def conexao():
    # Setup
    conexao_obj = Conexao()
    yield conexao_obj
    # Tear down
    conexao_obj.fechar()


@pytest.fixture()
def sessao(conexao):
    # Setup
    sessao_obj = conexao.gerar_sessao()
    yield sessao_obj
    # Tear down
    sessao_obj.roll_back()
    sessao_obj.fechar()


def test_salvar_usuarios(sessao):
    usuario = Usuario(nome='Giovanni')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [Usuario(nome='Giovanni'), Usuario(nome='Meire')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
