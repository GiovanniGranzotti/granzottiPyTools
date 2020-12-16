from unittest.mock import Mock

from libgranzottiPyTools import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'giovanni', 'id': 101380,
        'avatar_url': 'https://avatars3.githubusercontent.com/u/101380?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('giovanni')
    assert 'https://avatars3.githubusercontent.com/u/101380?v=4' == url
