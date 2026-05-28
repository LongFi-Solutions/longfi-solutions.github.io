---
title: Omada Networks by TP-Link
---

# **LongFi Connect - Omada Networks by TP-Link Passpoint Implementation Guide**

For support please contact: [networks@longfisolutions.com](emailto:networks@longfisolutions.com)

***

## **Prerequisites**

### Network Requirements:

- The NAS ID and RadSec certificates obtained during your site Onboarding & Activation
- A guest VLAN with the appropriate network segmentation, security, traffic shaping, and firewall policies for your requirements.
- The guest VLAN needs a large DHCP pool with a short lease time. Passpoint clients can automatically discover and join a network, and there will be many more "transient client" connections than a normal guest wifi network.

### **Omada Official Documentation:**

[How to Configure Hotspot 2.0 Wi-Fi on Omada Controller](https://support.omadanetworks.com/cac/document/110379/)

**_\*Please Note:_**

Depending on your organizational structure and your Omada hardware, software, and firmware versions, you may be able to configure Certificates, the RADIUS profile, and the Passpoint Wi-Fi SSID at the Global level.  This can save you a lot of time by allowing the configs to be applied to multiple sites at once.  The NAS ID must be unique at the site level, but the certificates, RADIUS RadSec profile, and most SSID settings will be the same at every site.  We made this guide using a single Omada AP and controller, with a single site, and the Global configuration options were not available.

### **Supported Hardware & Firmwares (as of May 2026):**

**Controllers**

- OC200 / OC300 / OC400 (hardware) — Passpoint: v5.15+, RadSec: v6.1+
- Omada Software Controller — same version thresholds
- Cloud-Based Controller (CBC) — Passpoint supported; RadSec status unclear, RadSec is not yet available for Built-in RADIUS, RADIUS Proxy, Portal, or SSL-VPN and CBC has additional restrictions Omada Network

**APs — full stack (Passpoint + 802.1X + RadSec)**

**These EAP7xx models are fully adapted to controller v6.2 with RadSec support:**

- EAP720 V1 — firmware 1.3.x (current 1.3.2)
- EAP723 V1/V2 — firmware 1.3.x / 1.5.x
- EAP770 V2 — firmware 1.5.x
- EAP772 V2 — firmware 1.5.x
- EAP772-Outdoor V1 — firmware 1.5.x
- EAP775-Wall V1 — firmware 1.5.x
- EAP787 V1 — firmware 1.5.x
- EAP725-Wall V1 — firmware 1.3.x

**APs — Passpoint + 802.1X only (no RadSec confirmed)**

Omada Controller v5.15.24 supports Hotspot 2.0 but not RadSec, and the EAP6xx generation received v6.1 controller adaptation but RadSec support has not been confirmed in their firmware release notes: Omada Network

- EAP650, EAP650-Wall, EAP650-Outdoor
- EAP653, EAP653 UR
- EAP660 HD
- EAP670, EAP673
- EAP680, EAP683 LR, EAP683 UR
- EAP690E HD
- EAP620 HD, EAP623-Outdoor HD, EAP625-Outdoor HD
- EAP610, EAP610-Outdoor

***

## High Level Steps

1. Submit NAS ID, Obtain RadSec Certificates, complete Prerequisites
2. Configure TP-Link Omada Controller and AP
    a. Configure Certificate Profile
    b. Configure RADIUS Profile
    c. Configure the Passpoint Wi-Fi SSID WLAN

***

## **Configure TP-Link Omada Controller and/or APs**

***

### **Configure a Certificate Profile**

From the Omada Dashboard go to **Configuration > Network Config > Profile > Certificate Profile**

**IMAGE HERE**

Click the button to **+ Add Certificate**

**IMAGE HERE**

- In the **Add Certificate** window, set the **Certificate Name** to **LongFi Connect CA**
- Set the **Certificate Type** to **CA Certificate**
- Set the **Certificate Format** to **X.509(PEM)**
- Click the **Import** button to **Upload Certificate**
- Upload the **LongFi CA** certificate file provided in your onboarding email.  This will usually be called **longfi_connect.ca.pem**
- Click **Apply** to add the CA Certificate

**IMAGE HERE**

Click the button once more to **+ Add Certificate**

- In the Add Certificate window, set the **Certificate Name** to **LongFi Connect Client Certs**
- Set the **Certificate Type** to **Client Certificate**
- Click the **Import** button to upload the **Client Private Key**
- Upload the **key.pem** certificate file provided in your onboarding email.  This will usually be named using your company name such as **mycompany.key.pem**
- Leave the password blank
- Set the **Certificate Format** to **X.509(PEM)**
- Click the **Import** button next to **Upload Certificate** to upload the client certificate
- Upload the **cert.pem** certificate file provided in your onboarding email.  This will usually be named using your company name such as **mycompany.cert.pem**
- Click **Apply** to add the new client certificate and private key

**IMAGE HERE of Client Cert + Key Window**

**IMAGE HERE of finished Certificates Window**

***

### **Configure a RADIUS Profile**

\*Please Note: you may receive an error message saying that one or more devices does not support RadSec.  If you have a Controller or AP model that supports RadSec, you will need to update the firmware before proceeding.  The Omada dashboard may show that your Controller or APs are "Up To Date" or "Latest Version", but that may not be the case.  Visit the firmware page and follow the instructions to get the newest firmware for your devices:

[https://support.omadanetworks.com/us/download/firmware/](https://support.omadanetworks.com/us/download/firmware/)

***

From the Omada Dashboard go to **Configuration > Network Config > Profile > RADIUS Profile**

**IMAGE HERE of main dashboard**

Click the button to **+ Create New RADIUS Profile**

**IMAGE HERE of RADIUS Profile dashboard**

- Name the profile **LongFi Connect RadSec**
- Under **Authentication Server 1**, set the **Authentication Server IP/URL** to **connect.longfisolutions.com**
- Check the **Enable** box to enable **RadSec**
- For the **CA Certificate** select the **LongFi Connect CA** as the **Certificate Profile**
- For the **Client Certificate** select the **LongFi Connect Client Certs** as the **Certificate Profile**
- For the **Authentication Port** enter **2083**
- For the **Authentication Password** enter **radsec**
- Under **Accounting Server** check the box to **Enable** the **RADIUS Accounting** server
- Under **Interim Update** check the box to **Enable** the **Interim Update**
- For the **Interim Update Interval** set the value to **300 Seconds**
- Under **Accounting Server 1** set the **Accounting Server IP/URL** to **connect.longfisolutions.com**
- Check the **Enable** box to enable **RadSec**
- For the **CA Certificate** select the **LongFi Connect CA** as the **Certificate Profile**
- For the **Client Certificate** select the **LongFi Connect Client Certs** as the **Certificate Profile**
- For the **Accounting Port** enter **2083**
- For the **Accounting Password** enter **radsec**

**IMAGE HERE of the finished RADIUS Profile**
