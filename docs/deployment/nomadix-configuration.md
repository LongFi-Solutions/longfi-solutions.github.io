---
title: Nomadix Configuration
---

1 - Configure the WLAN

* Log into the Nomadix WLAN controller using your credentials:
* Click on the Config tab at the top of the screen, expand the WLAN section and select Add WiFi from the left-hand navigation menu.
* Click on Add WiFi/WLAN in the content area:

![](/assets/images/Nomadix%20-%201.jpg)

* Enter the required information, being sure to select WPA2-802.1X for encryption type. 

![](/assets/images/20261005-214053.png)

* Expand the Advanced Settings option and enter the **NAS ID** you provided during registration and onboarding. This can also be found in your Carrier Offload Approval Email.

![](/assets/images/20261005-214344.png)

* Click Next and specify the AP Group and other information to apply the new WLAN.
* In the Network Type option, choose 5G. We normally don't recommend enabling 2.4 GHz in all but the highest density environments (large public venue) as most modern clients will avoid 2.4, and this band is not voice-grade.
* In that same window, you can choose the VLAN ID.
* Under Support Radio, choose ALL

![](/assets/images/20261005-214943.png)

* Click Finish.

2- Configure the Radsec server

- The newly created WLAN is going to show up on the list. Click on Edit.

![](/assets/images/20261005-215703.png)

* Click [Radius Server Settings]

![](/assets/images/20261005-215822.png)

* Click on the Radsec Server tab, then click on Add Server

![](/assets/images/20261005-220029.png)

* Fill in the RadSec server information.
    - Radsec ID: Any number, usually 1 or 2
    - Server IP: 34.176.6.104
    - Server Port: 2083 
    - TLS Timeout(s): 5
* Click Save

![](/assets/images/20261005-220342.png)

* Click Add Server again to add the secondary Radsec server.
    - Radsec ID: Any number, usually 1 or 2
    - Server IP: **136.107.123.32**
    - Server Port: 2083 
    - TLS Timeout(s): 5
* Click Save
* Click on Local Certificate Info

![](/assets/images/20261005-220731.png)

* Upload the Certificates provided during registration and onboarding. 
    - Click on Certificate to upload the **.cert** file
    - Click on Private Key to upload the **.key** file
    - Enter the Password which is **radsec**
    - Click on CA to upload the **.ca** file

![](/assets/images/20261005-221348.png)

* Click  Upload & Load

3 - Configure the Hotspot 2.0

- Expand the AP section in the left-hand navigation menu and select Hotspot2.0:
- Enter a template name such as Passpoint and select the SSID that was created in the previous steps from the drop-down list:

![](/assets/images/20261005-221736.png)

* Click Advanced Settings
* Expand the Advanced Settings and scroll down to the Cellular section. Complete the settings as per the description below:

![](/assets/images/20261005-221937.png)

* Scroll down to the end of the settings and click Save.

4 - Configure the NAS ID

- Click on the Maintenance tab at in the top menu bar, expand the System section in the left-hand navigation menu and select Web Console:

![](/assets/images/20261005-222609.png)

- Using the command input box, send the sequence of commands shown below to configure the NAS-Identifier:

```json
configure 
wlan-config 1 
nas-id <nas-identifier provided during onboarding> 
exit 
exit 
wr
```

![](/assets/images/20261005-222749.png)
