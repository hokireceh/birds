import requests

from hokireceh_claimer import base
from core.headers import headers


def get_info(data, proxies=None):
    url = "https://api.birds.dog/user"
    guild_url = "https://api.birds.dog/guild/join/6719d2d7dd68f56877d35b7c"

    try:
        join_guild = requests.get(
            url=guild_url,
            headers=headers(tele_auth=data),
            proxies=proxies,
            timeout=20,
        )
        response = requests.get(
            url=url,
            headers=headers(tele_auth=data),
            proxies=proxies,
            timeout=20,
        )
        data = response.json()
        balance = data["balance"]

        base.log(f"{base.green}Balance: {base.white}{balance:,}")

        return data
    except:
        return None
