from dataclasses import dataclass

from tplink_api.parse.utils import extract_vars
from tplink_api.router import RouterInterface

from .fetcher import Fetcher


@dataclass
class Survey(Fetcher):
    ssid: list[str]
    mac_filter_enabled: bool
    mac_filter_whitelist: bool
    clients: list

    @classmethod
    def fetch(cls, router: RouterInterface):
        stats_raw = cls._load_page(router, 1)     
        return stats_raw

    @staticmethod
    def _load_page(router: RouterInterface, page: int) -> dict:
        doc = router.page("popupSiteSurveyRpm", params={"Page": page})

        siteList = list(extract_vars(doc, [
            "siteList"]).values())
            
	       
        print("Master SSID: ",siteList[0][1])
        print("Master Channel: ", siteList[0][3])

        return siteList[0][3]
