from dataclasses import dataclass

from tplink_api.parse.utils import extract_vars
from tplink_api.router import RouterInterface

from .fetcher import Fetcher


@dataclass
class Logout(Fetcher):
    ssid: list[str]
    mac_filter_enabled: bool
    mac_filter_whitelist: bool
    clients: list

    @classmethod
    def fetch(cls, router: RouterInterface):
        stats_raw = cls._load_page(router, 1)

        return True

    @staticmethod
    def _load_page(router: RouterInterface, page: int) -> dict:
        router.page("LogoutRpm", params={"Page": page})
        

        return True
