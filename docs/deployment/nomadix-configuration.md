---
title: Nomadix
---

# Nomadix Passpoint Configuration – Basic Settings

This guide provides the basic steps required to configure Passpoint on a Nomadix WLAN controller for use with LongFi carrier offload services.

For support, please contact: [**support@longfisolutions.com**](mailto:support@longfisolutions.com)

***

###  High-Level Steps:

1. Configure the WLAN
2. Configure the RadSec servers
3. Configure Hotspot 2.0
4. Configure the NAS Identifier (NAS-ID)

***

### 1 - Configure the WLAN

- Log in to the Nomadix WLAN controller using your administrator credentials.
- Click the **Config** tab at the top of the screen.
- Expand the **WLAN** section in the left-hand navigation menu and select **Add WiFi**.
- Click **Add WiFi/WLAN**.

![](/assets/images/Nomadix%20-%201.jpg)

* Enter the required WLAN information. For the encryption type, select **WPA2-802.1X**.

![](/assets/images/20261005-214053.png)

* Expand **Advanced Settings** and enter the **NAS-ID** provided during the LongFi registration and onboarding process. You can also find your NAS-ID in your **Carrier Offload Approval Email**.

![](/assets/images/20261005-214344.png)

- Click **Next** and select the appropriate **AP Group** and other settings for the new WLAN.
- Under **Network Type**, select **5G**.
LongFi generally recommends using the **5 GHz band** for Passpoint deployments. We recommend enabling 2.4 GHz only when there is a specific coverage or deployment requirement, such as certain high-density or large public environments. Most modern mobile devices prefer 5 GHz when adequate coverage is available, and 5 GHz generally provides better performance and capacity for carrier offload.
- Select the appropriate **VLAN ID** for the Passpoint WLAN.
- Under **Support Radio**, select **ALL**.

![](/assets/images/20261005-214943.png)

* Review the configuration and click **Finish**.

### 2 - Configure the Radsec server

- Locate the newly created WLAN in the WLAN list and click **Edit**.

![](/assets/images/20261005-215703.png)

* Select **Radius Server Settings**.

![](/assets/images/20261005-215822.png)

* Open the **Radsec Server** tab and click **Add Server**.

![](/assets/images/20261005-220029.png)

* Primary RadSec Server

Enter the following information:

- **RadSec ID:** A unique numeric ID, typically `1`
- **Server IP:** `34.176.6.104`
- **Server Port:** `2083`
- **TLS Timeout:** `5` seconds

Click **Save**.

![](/assets/images/20261005-220342.png)

* Secondary RadSec Server

Click **Add Server** again and enter the secondary server information:

- **RadSec ID:** A different unique numeric ID, typically `2`
- **Server IP:** `136.107.123.32`
- **Server Port:** `2083`
- **TLS Timeout:** `5` seconds

Click **Save**.

![](/assets/images/20261005-220731.png)

* Upload the RadSec Certificates
* Click **Local Certificate Info**.
* Upload the certificates provided during the LongFi registration and onboarding process:
    - **Certificate:** Upload the `.cert` file.
    - **Private Key:** Upload the `.key` file.
    - **Password:** Enter `radsec`.
    - **CA:** Upload the `.ca` file.
* Click **Upload & Load**.

The Nomadix controller should now have the client certificate, private key, and CA certificate required to establish secure RadSec connections with the LongFi authentication servers.

![](/assets/images/20261005-221348.png)

### 3 - Configure the Hotspot 2.0

- Expand the **AP** section in the left-hand navigation menu and select **Hotspot2.0**.
- Enter a descriptive template name, such as **Passpoint**.
- From the SSID drop-down menu, select the WLAN created in the previous steps.

![](/assets/images/20261005-221736.png)

- Click **Advanced Settings**.
- Expand **Advanced Settings** and scroll to the **Cellular** section.
- Configure the Cellular settings using the values provided by LongFi during onboarding, as shown in the example below.

![](/assets/images/20261005-221937.png)

* Review the configuration, scroll to the bottom of the page, and click **Save**.

### 4 - Configure the NAS ID

- The NAS Identifier must also be configured through the Nomadix Web Console.
- Click the **Maintenance** tab in the top menu.
- Expand **System** in the left-hand navigation menu and select **Web Console**.

![](/assets/images/20261005-222609.png)

- In the command input box, enter the following commands, line by line:

```json
configure 
wlan-config 1 
nas-id <nas-identifier provided during onboarding> 
exit 
exit 
wr
```

Replace `<NAS-ID provided during onboarding>` with the NAS Identifier assigned to your deployment.

> **Important:** Make sure you are modifying the correct WLAN configuration. The `wlan-config 1` value must correspond to the WLAN configured for LongFi Passpoint service.

The Passpoint WLAN is now configured with the LongFi RadSec servers, certificates, Hotspot 2.0 settings, and NAS Identifier.

![](/assets/images/20261005-222749.png)
