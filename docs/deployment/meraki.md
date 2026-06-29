---
title: Meraki Passpoint Conversion Guide
---

# Meraki Passpoint Conversion Guide

For support please contact: [networks@longfisolutions.com](mailto:networks@longfisolutions.com)

***

## Prerequisites

LongFi Connect configuration requires the Passpoint protocol.  Please ensure your Meraki system is running version 14.0 or later, your AP models support Passpoint/Hotspot 2.0, and you have basic traffic routing working with existing SSID(s).

**You will also need:**

1. The NAS ID and RadSec certificates obtained during your site Onboarding & Activation
2. A guest VLAN with the appropriate network segmentation, security, traffic shaping, and firewall policies for your requirements.
3. The guest VLAN needs a large DHCP pool with a short lease time.  Passpoint clients can automatically discover and join a network, and there will be many more "transient client" connections than a normal guest wifi network.

***

## RadSec with Meraki

LongFi now supports a hosted RadSec authentication model for Cisco Meraki networks.  This allows Meraki partners to connect to the LongFi network without hosting their own proxy or VPN, while maintaining carrier-grade security and data accuracy.

***

### How It Works

**1. Meraki Controller → LongFi Connect AAA Servers**

- Each Meraki org downloads its CA certificate and shares it with LongFi engineers
- Each Meraki org uploads LongFi provided CA certificate to Meraki organization
- Shared certificates establish secure RadSec TLS tunnel via TCP on port 2083
- Meraki org securely transports SIM client RADIUS messages through TCP and TLS

**2. LongFi Connect AAA Servers → Carrier Networks**
