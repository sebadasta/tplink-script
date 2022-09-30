from dataclasses import dataclass

from tplink_api.parse.utils import extract_vars
from tplink_api.router import RouterInterface

from .fetcher import Fetcher


@dataclass
class WLANSettings(Fetcher):
    ssid: list[str]
    mac_filter_enabled: bool
    mac_filter_whitelist: bool
    clients: list

    @classmethod
    def fetch(cls, router: RouterInterface):
        stats_raw = cls._load_page(router, 1)
        return stats_raw
    
    @classmethod
    def syncChannels(cls, router: RouterInterface,masterChannel):
        stats_raw = cls._sync(router,str(masterChannel), 1)
        return stats_raw
        

    @staticmethod
    def _load_page(router: RouterInterface, page: int) -> dict:
            
        doc = router.page("WlanNetworkRpm", params={"Page": page})
        wlan_para = list(extract_vars(doc, ["wlanPara"]).values())
        print("Repeater Router Channel: ", wlan_para[0][10])
        response = wlan_para[0][10]
        
        return response
        
    @staticmethod
    def _sync(router: RouterInterface, masterChannel: str, page: int) -> dict:
            
        router.page("WlanNetworkRpm.htm?ssid1=ColgateDeEsta&ssid2=TP-LINK_GUEST_DC74&ssid3=TP-LINK_DC74_3&ssid4=TP-LINK_DC74_4&region=101&band=0&mode=5&chanWidth=2&channel="+masterChannel+"&rate=71&ap=1&broadcast=2&wdsbrl=2&brlssid=ColgateDeEsta&brlbssid=68-02-B8-2C-F1-E6&addrType=1&keytype=4&wepindex=1&authtype=1&keytext=YDeEstaTambien1807&Save=Save", params={"Page": page})
        
        
        response = "Channel Updated!"
        
        return response        
