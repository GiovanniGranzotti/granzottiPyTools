from unittest.mock import Mock

import pytest

from libgranzottiPyTools import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars3.githubusercontent.com/u/101380?v=4'
    resp_mock.json.return_value = {
        'login': 'giovanni', 'id': 101380,
        'avatar_url': url,
    }
    get_mock = mocker.patch('libgranzottiPyTools.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('giovanni')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('renzon')
    assert 'https://avatars.githubusercontent.com/u/3457115?v=4' == url
