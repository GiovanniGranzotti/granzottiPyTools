import pytest
from libgranzottiPyTools.spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    'remetente',
    ['giogranzotti@hotmail.com', 'foo@bar.com.br']
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        'meireelenmacario@gamil.com',
        'Curso Python Pro',
        'Testando as funções e exercitando a programação em python. Por favor ignorar o email. kkkk'
    )

    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['giogranzotti', '']
)
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            'meireelenmacario@gamil.com',
            'Curso Python Pro',
            'Testando as funções e exercitando a programação em python. Por favor ignorar o email. kkkk'
        )
