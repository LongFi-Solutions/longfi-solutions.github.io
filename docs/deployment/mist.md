---
title: Juniper Mist Passpoint Conversion Guide
---

# Juniper Mist Passpoint Conversion Guide

For support please contact: [support@longfisolutions.com](mailto:support@longfisolutions.com)

***

## Prerequisites

LongFi Connect configuration requires the Passpoint protocol.  Please ensure your Mist system is running the latest firmware, your AP models support Passpoint/Hotspot 2.0, and you have basic traffic routing working with existing SSID(s) and VLANs.

!!! note
    Before you can activate Passpoint in your Mist Organization, you will first need to register your site, provide a NAS ID, and obtain certificates.  Please review the **RadSec with Mist** section of this guide before proceeding with SSID and RADIUS configuration.

**You will also need:**

1. The NAS ID and RadSec certificates obtained during your site Onboarding & Activation
2. A guest VLAN with the appropriate network segmentation, security, traffic shaping, and firewall policies for your requirements.
3. The guest VLAN needs a large DHCP pool with a short lease time.  Passpoint clients can automatically discover and join a network, and there will be many more "transient client" connections than a normal guest wifi network.

***

## High Level Steps

1. Submit NAS ID, Obtain RadSec Certificates
2. Upload Certificates to Mist Organization
3. Configure the Passpoint Wi-Fi SSID
4. Build Hotspot 2.0 Profile
5. Configure RADIUS for the Passpoint Wi-Fi SSID

***

## RadSec with Mist

LongFi now supports a hosted RadSec authentication model for Mist networks.  This allows Mist partners to connect to the LongFi network without hosting their own proxy or VPN, while maintaining carrier-grade security and data accuracy.

For more information on configuring Mist for RadSec, see:

[https://www.mist.com/documentation/radsec/](https://www.mist.com/documentation/radsec/)

***

## Upload Certificates

You will be provided with a unique certificate bundle containing 3 certificate files:

- longficonnect.ca.pem
- example.cert.pem
- example.key.pem

Open each file in a text editor, you will need to copy and paste the text of the certificates into Mist

From the Juniper Mist dashboard go to **Organization > Settings**

**(image here)**

- Under **RadSec Certificates** choose **Add a RadSec certificate**
- Open the **ca.pem** certificate in a text editor
- You will notice more than one certificate in the **longficonnect.ca.pem** file in the text editor.  You will need to add them one at a time into Mist.
- Copy the first certificate all the way from -----BEGIN CERTIFICATE----- to -----END CERTIFICATE----- into the **RadSec Certificate** window in Mist
- Click **Add**
- Click **Add a RadSec certificate** again and repeat this process for all certificates in the ca.pem file
- Under **AP RadSec Certificate** click **Add AP RadSec certificate**
- Open the **key.pem** certificate in a text editor
- Copy and paste the text from the key.pem certificate file into the **Private Key** window in Mist
- Open the **cert.pem** certificate in a text editor
- Copy and paste the text from the key.pem certificate file into the **Signed Certificate** window in Mist
- Click **Save** to save the **AP RadSec Certificate**
