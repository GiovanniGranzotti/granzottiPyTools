from libgranzottiPyTools.spam.db import Conexao
from libgranzottiPyTools.spam.db import Sessao
from libgranzottiPyTools.spam.modelos import Usuario


def test_salvar_usuarios():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome='Giovanni')
    sessao.salvar(usuario)
    for u in sessao.usuarios:
        print(u.nome)
    print(id(sessao.usuarios), id(sessao.contador))
    for u in Sessao.usuarios:
        print(u.nome)
    print(id(Sessao.usuarios), id(Sessao.contador))
    assert isinstance(usuario.id, int)
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuarios():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome='Giovanni'), Usuario(nome='Meire')]
    for usuario in usuarios:
        sessao.salvar(usuario)
    for u in sessao.usuarios:
        print(u.nome)
    print(id(sessao.usuarios), id(sessao.contador))
    for u in Sessao.usuarios:
        print(u.nome)
    print(id(Sessao.usuarios), id(Sessao.contador))
    assert usuarios == sessao.listar()
    sessao.roll_back()
    sessao.fechar()
    conexao.fechar()
