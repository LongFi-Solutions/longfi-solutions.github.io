---
title: Overview
---

# Overview

This page will give a technical overview on how to prepare, configure, understand, and operate networks for Passpoint, Carrier Offload, and OpenRoaming.  For a general intro to access layer roaming technologies, please visit:

**LongFi Solutions - LongFi Connect Overview:**

[https://www.longfisolutions.com/connect/](https://www.longfisolutions.com/connect/)

**Wi-Fi Alliance - Wi-Fi® certified Passpoint® Overview:**

[https://www.wi-fi.org/access](https://www.wi-fi.org/access)

**Wireless Broadband Alliance - OpenRoaming:**

[https://wballiance.com/openroaming/](https://wballiance.com/openroaming/)

## Passpoint

Wi-Fi CERTIFIED Passpoint® (also known as Hotspot 2.0) is a Wi-Fi Alliance standard that enables seamless, secure, and automatic authentication to public Wi-Fi networks.  It eliminates manual login, captive portals, and password entry, providing cellular-like roaming for Wi-Fi. 

***

### Minimum Requirements

In order to enable Passpoint, Carrier Offload, or OpenRoaming, your Wi-Fi equipment (and controller software) must support:

- Passpoint (Hotspot 2.0, 802.11u)
- WPA2-Enterprise (802.1X) with RADIUS (WPA3 recommended)
- RadSec (RADIUS over TLS and TCP)

If your equipment does not support RadSec natively, there are alternative solutions.  Please see the RadSec section in the Docs.  

***

### Technical Architecture

Simplified, there are 3 main components to a Passpoint network:

- A guest network segment
- A RADIUS profile
- A Wi-Fi SSID with a Hotspot profile

Getting deeper, Passpoint relies on the [802.11u](https://en.wikipedia.org/wiki/IEEE_802.11u) amendment to the 802.11 standard, providing wireless clients with a streamlined mechanism to discover and authenticate to non-home networks.  The 802.11u beacon is a Wi-Fi management frame that includes inter-networking elements, allowing APs to broadcast support for cellular-like, automatic network discovery and connection.  These beacons allow devices to identify provider networks, venue types, and roaming capabilities before associating, eliminating manual login procedures, and convergence between technologies and identity providers.

### Security Architecture

Passpoint uses enterprise-grade encryption for over-the-air connections, significantly enhancing safety over open guest networks.
