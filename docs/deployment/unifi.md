---
title: UniFi Passpoint Conversion Guide
---

# UniFi Passpoint Conversion Guide

For support please contact: networks@longfisolutions.com

***

### Prerequisites

LongFi Connect configuration requires the Passpoint protocol. Please ensure your Ubiquiti network is using UniFi Network Controller version 8.4.54 or higher and AP firmware version 6.6.77 or AP firmware version 7.0.66 or higher, depending on hardware release track.  You can verify that your APs support **Passpoint (Hotspot 2.0)** and **RADIUS over TLS (RadSec)** at [https://techspecs.ui.com/unifi/wifi](https://techspecs.ui.com/unifi/wifi)

##### You will also need:

1. The NAS ID and RadSec certificates obtained during your site Onboarding & Activation
2. A guest VLAN with the appropriate network segmentation, security, traffic shaping, and firewall policies for your requirements.
3. The guest VLAN needs a large DHCP pool with a short lease time.  Passpoint clients can automatically discover and join a network, and there will be many more "transient client" connections than a normal guest wifi network.

***

### High Level Steps

1. Submit NAS ID, Obtain RadSec Certificates
2. Configure UniFi Network Controller
    1. Configure RADIUS Profile
    2. Configure Passpoint Wi-Fi

***

#### Submit NAS ID, Obtain RadSec Certificates

Every Passpoint network requires a unique Network Access Server Identifier (NAS ID).  We normally use the MAC address of the controller, gateway, or a single AP on the network.

Log into your UniFi network.  Navigate to UniFi Devices, choose your Network Controller, Gateway, or AP, and copy the MAC Address.

![](/assets/images/UniFi%20NAS%20ID%20get%20MAC-1.png){ .img-md }

Submit this MAC address during your site Onboarding & Activation, and return to this guide after the network is onboarded and RadSec certificates have been delivered.

***

#### Configure UniFi Network Controller

After retrieving certificates, configuring the network controller for Passpoint is a two-part process. First, create the RADIUS profile, then apply the profile to a newly created WiFi SSID called 'LongFi Passpoint'.

#### Create a RADIUS Profile

Configure a TLS connection to LongFi Connect AAA servers, which performs Authentication, Authorization, and Accounting for the end customers. Enabling RADIUS communication over TLS (RadSec) increases the level of security for authentication that is carried out across the cloud network.

In the sidebar, choose **Settings > Networks > scroll down > RADIUS Servers** then click **Create New**:

![](/assets/images/2%20-%20Create%20a%20RADIUS%20Profile.png){ .img-md }

For the profile name enter **LongFi RadSec**.

#### Configure RADIUS properties:

- Under Radius Settings, check the TLS box.
    - Press Upload next to Client Certificate, choose the path to the file containing the extension .cert, for example your-site.cert.pem
    - Press Upload next to Private Key, choose the path to the file containing the extension .key, for example your-site.key.pem
    - Keep Private Key Password empty
    - Press Upload next to CA Certificate, choose the path to the file containing the extension .ca, for example longfi-ca-chain.ca.pem
    - \*Note: these names and extensions may differ slightly based on your operating system (ie. longfi.cer.pem)

[IMAGE HERE]

- Specify **Authentication Servers**:
    - Enter IP Address: **136.107.123.32** Port: **2083** Shared Secret: **radsec**. Click Add.
    - Enter IP Address: **34.174.6.104** Port: **2083** Shared Secret: **radsec**. Click Add.
- Check the Accounting Servers checkbox. RADIUS Accounting Server settings will appear. (\*Note: in some versions of UniFi, you may have to click **Add** to save the RADIUS Profile and click to edit the profile again before you can enable Accounting Servers.
- Specify the following Accounting Servers (same as above):
