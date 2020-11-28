from libgranzottiPyTools.spam.enviador_de_email import Enviador


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


def test_remetente():
    enviador = Enviador()
    resultado = enviador.enviar(
        'giogranzotti@hotmail.com',
        'meireelenmacario@gamil.com',
        'Curso Python Pro',
        'Testando as funções e exercitando a programação em python. Por favor ignorar o email. kkkk'
    )
    assert 'giogranzotti@hotmail.com' in resultado
