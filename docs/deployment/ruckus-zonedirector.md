---
title: Ruckus ZoneDirector
---

Ruckus Zone Director Passpoint Conversion - Basic Settings[¶](https://longfi-solutions.github.io/deployment/cambium/#cambium-passpoint-conversion-basic-settings "Permanent link")

For support, please contact: [support@longfisolutions.com](mailto:support@longfisolutions.com)

High-Level Steps:[¶](https://longfi-solutions.github.io/deployment/cambium/#high-level-steps "Permanent link")

1. Deploy Local RadSecProxy
2. ZoneDirector Configuration
3. **Configure AAA Server**
4. **Configure AAA Server Accounting**
5. **Configure Hotspot 2.0 Services**
6. **Create WLAN**
7. **Create WLAN Group**
8. Test & Validate

Deploy Local RadSecProxy[¶](https://longfi-solutions.github.io/deployment/cambium/#deploy-local-radsecproxy "Permanent link")

Ruckus ZoneDirector does not support RadSec natively, so we need a Local RadSecProxy running on a Virtual Machine on-site, or in a cloud VM that can be accessed via a VPN tunnel from the local network.  Please visit our public GitHub repository for instructions on deploying the local radsecproxy:

[https://github.com/LongFi-Solutions/longfi-radsecproxy](https://github.com/LongFi-Solutions/longfi-radsecproxy)

Take note of the IP address and shared secret of your Local RadSecProxy deployment.  You will need this to configure the AAA RADIUS servers in Zone Director.

**Step 1: Configure AAA Server**

1. Navigate to **Configure** → **AAA Servers**
2. Click **Create New**
3. Configure:
    - **Name**: LongFi Proxy
    - **Type**: RADIUS
    - **Auth Server Address**: {Primary IP}
    - **Port**: {AUTH_PORT}
    - **Shared Secret**: {Secret}
4. Click **OK**

**Step 2: Configure AAA Server Accounting**

1. Navigate to **Configure** → **AAA Servers**
2. Click **Create New**
3. Configure:
    - **Name**: LongFi Accounting
    - **Type**: RADIUS Accounting
    - **Auth Server Address**: {Primary IP}
    - **Port**: {AUTH_PORT}
    - **Shared Secret**: {Secret}
4. Click **OK**

**Step 3: Configure Hotspot 2.0 Services**

1. Navigate to **Configure** → **Hotspot 2.0 Services**
2. Under **Service Provider Profiles,** Click **Create New**
3. Configure:

3.1 – Name: Enter a descriptive profile name.

3.2 - Under **Domain Name List,** Click **Create New and add the following domains:**

freedomfi.com

hellohelium.com

longfisolutions.com

3.3 – Click in Advanced Options and under **Roaming Consortium List,** Click **Create New and add the following:**

Name: Orion - Organization ID: F4F5E8F5F4

Name: Uplink - Organization ID: 2A2F830000

3.4 – The configuration under **NAI Realm List and under 3GPP Cellular Network information will be provided in your Carrier Offload Approval Email. These may only be activated for approved sites.**

**3.5 – Click OK**

**Step 4: Configure Hotspot 2.0 Services**

1. Navigate to **Configure** → **Hotspot 2.0 Services**
2. Under **Operator Profiles,** Click **Create New**
3. Configure:

3.1 - Add a Name

3.2 – Venue information. Specify the Group and Type as the option that best matches your site.

3.3 – Internet Option - Enable the Specified with connectivity to internet option

3.4 - **Access Network Type – Chargeable Public**

**3.5 - IP Address Type – IPv4 Address - Single NATed private address**

**3.6 -  IP Address Type – IPv6 Address – Not Available**

**3.7 - Operator Friendly Name – Click in Create NEW, chose Englis under Language and under Name add LONGFISOLUTIONS:US. Click Save**

**3.8 - Service Provider Profiles – Enable the Service Provider Profile previously created.**

**3.9 – Click OK**

**Step 5: Create WLAN**

1. Navigate to **Configure** → **WLANs**
2. Under WLANs, Click **Create New**
3. Configure:

**3.1 Name – Add the WLAN name**

**3.2 ESSID – Add the SSID name**

**3.3 Type - Hotspot 2.0**

**3.4 Method - 802.1x EAP**

**3.5 Fast BSS Transition – Enable Enable 802.11r FT Roaming**

**3.6 Encryption Options – Enable WPA2 and AES**

**3.7 Hotspot 2.0 Operator – Choose the previously created Operator**

**3.8 Authentication Server - Choose the previously created Radius Server**

**3.9 Wireless Client Isolation – Enable  Isolate wireless client traffic from other clients on the same AP &  Isolate wireless client traffic from all hosts on the same VLAN/subnet. Choose the Gateway & DNS option**

**3.10 Under** [**Advanced Options**](https://10.0.161.100/admin/conf_wlans.jsp)**, next to Accounting Server, choose the previously created Radius Accounting Server**

**3.11 Proxy ARP – Enable Proxy ARP**

**3.12 Inactivity Timeout - Terminate idle user session after 5 minutes of inactivity**

**3.13 Radio Resource Management - Enable 802.11k Neighbor-list Report**

**Step 6: Create WLAN Group**

1. Under WLAN Groups, Click **Create New**
2. **Choose the previously created passpoint WLAN and add other members as needed.**
