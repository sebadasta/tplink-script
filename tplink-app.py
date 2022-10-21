#!/usr/bin/env python3
import os
from dotenv import load_dotenv
from tplink_api import fetchers, RouterSession
import datetime


load_dotenv()
rt = RouterSession(os.getenv("TPLINK_IP"), os.getenv("TPLINK_USER"), os.getenv("TPLINK_PASSWORD"))

wlanset = fetchers.wlansettings.WLANSettings.fetch(rt)
surv = fetchers.survey.Survey.fetch(rt)



if wlanset != surv:
  print(datetime.datetime.now().strftime("%c"))
  print("Channels NOT The Same, will update repeater's channel")
  print(fetchers.wlansettings.WLANSettings.syncChannels(rt, surv))
 
else: 
  print("Same Channels. All OK!")
  logout = fetchers.logout.Logout.fetch(rt)
