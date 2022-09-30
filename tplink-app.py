#!/usr/bin/env python3
from tplink_api import fetchers, RouterSession

rt = RouterSession("192.168.0.1", "admin", "admin")

#general = fetchers.status.GeneralStatus.fetch(rt)
#print(general.lan)

#stats = fetchers.wlan.WLANStats.fetch(rt)
#leases = fetchers.dhcp.DHCPLeases.fetch(rt)


wlanset = fetchers.wlansettings.WLANSettings.fetch(rt)

surv = fetchers.survey.Survey.fetch(rt)


import pprint
"""pp = pprint.PrettyPrinter(indent=2)
pp.pprint(general.dict())
pp.pprint(stats.dict())
pp.pprint(leases.dict())
#pp.pprint(logout)
#pp.pprint(wlanset.dict())"""




if wlanset != surv:
  print("Channels NOT The Same, will update repeater's channel")
  print(fetchers.wlansettings.WLANSettings.syncChannels(rt, surv))
  
else: 
  print("Same Channels. All OK!")
  
  logout = fetchers.logout.Logout.fetch(rt)
