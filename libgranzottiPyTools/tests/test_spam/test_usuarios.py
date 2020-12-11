from libgranzottiPyTools.spam.modelos import Usuario


def test_salvar_usuarios(sessao):
    usuario = Usuario(nome='Giovanni', email='giogranzotti@hotmail.com')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuarios(sessao):
    usuarios = [
        Usuario(nome='Giovanni', email='giogranzotti@hotmail.com'),
        Usuario(nome='Meire', email='meireelenmacario@gmail.com')
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
