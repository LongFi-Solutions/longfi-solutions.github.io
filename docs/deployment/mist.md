---
title: Juniper Mist Passpoint Conversion Guide
---

# Juniper Mist Passpoint Conversion Guide

For support please contact: [support@longfisolutions.com](mailto:support@longfisolutions.com)

***

## Prerequisites

LongFi Connect configuration requires the Passpoint protocol.  Please ensure your Mist system is running the latest firmware, your AP models support Passpoint/Hotspot 2.0, and you have basic traffic routing working with existing SSID(s) and VLANs.

!!! note
    Before you can activate Passpoint in your Mist Organization, you will first need to complete the **RadSec with Mist** section of this guide, and share your Mist CA with LongFi engineers (see below).

**You will also need:**

1. The NAS ID and RadSec certificates obtained during your site Onboarding & Activation
2. A guest VLAN with the appropriate network segmentation, security, traffic shaping, and firewall policies for your requirements.
3. The guest VLAN needs a large DHCP pool with a short lease time.  Passpoint clients can automatically discover and join a network, and there will be many more "transient client" connections than a normal guest wifi network.

***

## High Level Steps

1. Submit NAS ID, Obtain RadSec Certificates, Share Mist CA
2. Upload Certificates to Mist Organization
3. Configure the Passpoint Wi-Fi SSID
4. Build Hotspot 2.0 Profile
5. Configure RADIUS for the Passpoint Wi-Fi SSID
6. 

***

## RadSec with Mist

LongFi now supports a hosted RadSec authentication model for Mist networks.  This allows Mistpartners to connect to the LongFi network without hosting their own proxy or VPN, while maintaining carrier-grade security and data accuracy.

For more information on configuring Mist for RadSec, see:

[](https://documentation.meraki.com/Wireless/Design_and_Configure/Configuration_Guides/Encryption_and_Authentication/MR_RadSec)

***

### How It Works

**1. Mist APs → LongFi Connect AAA Servers**

- Each Mist org downloads its CA certificate and shares it with LongFi engineers
- Each Mist org uploads LongFi provided certificates to Mist organization
- Shared certificates establish secure RadSec TLS tunnel via TCP on port 2083
- Mist org securely transports SIM client RADIUS messages through TCP and TLS

**2. LongFi Connect AAA Servers → Carrier Networks**

- LongFi establishes secure RadSec tunnels to Carrier Networks using Carrier certificates
- Passpoint Client AAA messages are routed to Carrier Realms
- Carrier Authenticated users are allowed to join Mist org Wi-Fi via EAP and 802.1X

**3. Offload, Authentication, & Accounting**

- Authentication: NAS_ID + certificate CN must match LongFi’s records
- Accounting: Offloaded Data maps to LongFi Partners via NAS_ID.

***

### Customer Setup

- From the main dashboard in Meraki, go to **Organization > Certificates**
- Click on **RADSEC**
- Click on **Upload CA certificate**
- Upload the **LongFi Connect CA certificates** provided in your onboarding and activation emails
- Under **RadSec AP Certificates** click on **Download CA**
- Share your newly downloaded **Meraki CA** with your LongFi Connect onboarding contact

**\*Please Note:** Meraki generates CA certificates at the Organization level.  If you are managing multiple sites from a single Organization, we only need one Meraki CA.  If you are an MSP managing multiple sites in multiple Meraki Organizations, we will need a Meraki CA certificate from each organization.  

Please allow 2-3 days for us to upload your Meraki CA certificates to the LongFi Connect servers.  Once your site has been approved for activation, follow the remainder of this guide to implement Passpoint on your Meraki networks.
