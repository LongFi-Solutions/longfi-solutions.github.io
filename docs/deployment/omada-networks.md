---
title: Omada Networks by TP-Link
---

# **LongFi Connect - Omada Networks by TP-Link Passpoint Implementation Guide**

For support please contact: [networks@longfisolutions.com](emailto:networks@longfisolutions.com)

##

## **Prerequisites**

### 

### Network Requirements:

- The NAS ID and RadSec certificates obtained during your site Onboarding & Activation
- A guest VLAN with the appropriate network segmentation, security, traffic shaping, and firewall policies for your requirements.
- The guest VLAN needs a large DHCP pool with a short lease time. Passpoint clients can automatically discover and join a network, and there will be many more "transient client" connections than a normal guest wifi network.

### **Omada Official Documentation:**

[How to Configure Hotspot 2.0 Wi-Fi on Omada Controller](https://support.omadanetworks.com/cac/document/110379/)

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
