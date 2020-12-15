from unittest.mock import Mock

import pytest

from libgranzottiPyTools.spam.enviador_de_email import Enviador
from libgranzottiPyTools.spam.main import EnviadorDeSpam
from libgranzottiPyTools.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Giovanni', email='giogranzotti@hotmail.com'),
            Usuario(nome='Meire', email='meireelenmacario@gmail.com')
        ],
        [
            Usuario(nome='Giovanni', email='giogranzotti@hotmail.com'),
        ]
    ]
)
def test_qtd_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'giogranzotti@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Giovanni', email='giogranzotti@hotmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'meireelenmacario@gmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'meireelenmacario@gmail.com',
        'giogranzotti@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
