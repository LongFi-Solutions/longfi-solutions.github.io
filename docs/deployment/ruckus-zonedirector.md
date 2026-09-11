---
title: Ruckus ZoneDirector
---

Ruckus Zone Director Passpoint Conversion - Basic Settings

For support, please contact: [support@longfisolutions.com](mailto:support@longfisolutions.com)

***

## High-Level Steps:

1. Deploy Local RadSecProxy
2. ZoneDirector Configuration
3. Configure AAA Server
4. Configure AAA Server Accounting
5. Configure Hotspot 2.0 Services
6. Create WLAN
7. Create WLAN Group
8. Test & Validate

Deploy Local RadSecProxy

Ruckus ZoneDirector does not support RadSec natively, so we need a Local RadSecProxy running on a Virtual Machine on-site, or in a cloud VM that can be accessed via a VPN tunnel from the local network.  Please visit our public GitHub repository for instructions on deploying the local radsecproxy:

[https://github.com/LongFi-Solutions/longfi-radsecproxy](https://github.com/LongFi-Solutions/longfi-radsecproxy)

Take note of the IP address and shared secret of your Local RadSecProxy deployment.  You will need this to configure the AAA RADIUS servers in Zone Director.

***

### **Step 1: Configure AAA Server**

1. Navigate to **Configure** → **AAA Servers**
2. Click **Create New**
3. Configure:
    - **Name**: LongFi Proxy
    - **Type**: RADIUS
    - **Auth Server Address**: {Primary IP}
    - **Port**: {AUTH_PORT}
    - **Shared Secret**: {Secret}
4. Click **OK**

![](/assets/images/ZoneDirector%20-%201%20AAA.png)

***

### **Step 2: Configure AAA Server Accounting**

1. Navigate to **Configure** → **AAA Servers**
2. Click **Create New**
3. Configure:
    - **Name**: LongFi Accounting
    - **Type**: RADIUS Accounting
    - **Auth Server Address**: {Primary IP}
    - **Port**: {AUTH_PORT}
    - **Shared Secret**: {Secret}
4. Click **OK**

![](/assets/images/ZoneDirector%20-%202%20AAA%20Acc.png)

***

### **Step 3: Configure Hotspot 2.0 Services**

1. Navigate to **Configure** → **Hotspot 2.0 Services**
2. Under **Service Provider Profiles,** Click **Create New**
3. Configure:

- 3.1 – **Name** - Enter a descriptive profile name.
- 3.2 - Under **Domain Name List,** Click **Create New and add the following domains:**

```text title="Domain Name List"
freedomfi.com
hellohelium.com
longfisolutions.com
```

- 3.3 – Click Advanced Options and, under **Roaming Consortium List,** Click **Create New** and add the following:

```text
Name: Orion - Organization ID: F4F5E8F5F4
Name: Uplink - Organization ID: 2A2F830000
```

![](/assets/images/ZoneDirector%20-%203%20hotspot.png)

3.4 – NAI Realm and 3GPP Cellular Network - Use the values provided in your Carrier Offload Approval Email. These settings may only be activated for approved sites.

3.5  Click **OK** to save the profile.

***

### **Step 4: Configure Hotspot 2.0 Services**

1. Navigate to **Configure** → **Hotspot 2.0 Services**
2. Under **Operator Profiles,** Click **Create New**
3. Configure:

3.1 – **Name** - Enter a descriptive operator profile name.

3.2 – **Venue information** - Select the Group and Type that best match the site.

3.3 – **Internet Option** - Enable the Specified with connectivity to internet option

3.4 - **Access Network Type – Chargeable Public**

**3.5 - IP Address Type – IPv4 Address - Single NATed private address**

**3.6 -  IP Address Type – IPv6 Address – Not Available**

**3.7 - Operator Friendly Name –** Click **Create NEW,** choose **English** under **Language,** and under **Name** add **LONGFISOLUTIONS:US.** Click **Save**

**3.8 - Service Provider Profiles –** Enable the **Service Provider Profile** created in **Step 3.**

**3.9 –** Click **OK** to save the profile.

 ![](/assets/images/ZoneDirector%20-%204%20profiles.png)

***

### **Step 5: Create WLAN**

1. Navigate to **Configure** → **WLANs**
2. Under **WLANs**, Click **Create New**
3. Configure:

**3.1 Name** – Enter the WLAN name

**3.2 ESSID** – Enter the SSID name

**3.3 Type - Hotspot 2.0**

**3.4 Method - 802.1x EAP**

**3.5 Fast BSS Transition – Do NOT Enable 802.11r FT Roaming**

**3.6 Encryption Options – Enable WPA2 and AES**

**3.7 Hotspot 2.0 Operator –** Select the **Operator Profile** created in **Step 4.**

**3.8 Authentication Server -** Select the **RADIUS server** created in **Step 1.**

**3.9 Wireless Client Isolation –** Enable both **client-isolation options.** For VLAN/subnet isolation, select **Gateway & DNS.**

**3.10  Accounting Server -** Under **Advanced Options,** select the **RADIUS Accounting server** created in Step 2.

**3.11 Access VLAN – Enter the correct VLAN for this SSID**

**3.12 Proxy ARP – Enable Proxy ARP**

**3.13 Inactivity Timeout - Terminate idle user session after 5 minutes of inactivity**

 ![](/assets/images/ZoneDirector%20-%205%20WLAN.png)

***

### **Step 6: Create WLAN Group**

1. Under **WLAN** Groups, Click **Create New**
2. Select the **Passpoint WLAN** created in **Step 5** and add any other WLAN members required for the site.

### **Step 7: Add the NAS ID**

1. SSH into the ZoneDirector, as you can't do this via the GUI.

Legacy SSH commands: ssh -o HostKeyAlgorithms=+ssh-rsa,ssh-dss -o PubkeyAcceptedKeyTypes=+ssh-rsa,ssh-dss admin@<YOUR-ZD-IP-HERE>

2. Configure the NAS ID

In the CLI, configure the NAS ID under the WLAN you created in step 5.

This is what it looks like in Ruckus CLI:  

,,,

Welcome to the Ruckus Wireless ZoneDirector 3000 Command Line Interface

ruckus>

ruckus> enable

ruckus# config

You have all rights in this mode.

ruckus(config)# wlan "LongFi Passpoint"

The WLAN service 'LongFi Passpoint' has been loaded. To save the WLAN service, type 'end' or 'exit'.

ruckus(config-wlan)# nasid-type user-define <YOUR-NAS-ID-HERE>

The command was executed successfully. To save the changes, type 'end' or 'exit'.

ruckus(config-wlan)# end

The WLAN service 'LongFi Passpoint' has been updated and saved.

Your changes have been saved.

ruckus(config)# exit

Your changes have been saved.

ruckus#

,,,
