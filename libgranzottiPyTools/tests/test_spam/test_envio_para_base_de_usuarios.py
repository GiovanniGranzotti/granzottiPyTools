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
    enviador = Enviador()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'giogranzotti@hotmail.com',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
        )
    assert len(usuarios) == enviador.qtd_emails_enviados
