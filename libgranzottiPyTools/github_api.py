import requests


def buscar_avatar(usuario):
    """
    Busca um avatar de um usuário no GitHub

    :param usuario: str como nome de usuário no github
    :return: str com o link do avatarpi
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']
