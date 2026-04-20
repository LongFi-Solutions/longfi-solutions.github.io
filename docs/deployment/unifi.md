---
title: UniFi Passpoint Conversion Guide
---

# UniFi Passpoint Conversion Guide

For support please contact: networks@longfisolutions.com

***

### Prerequisites

LongFi Connect configuration requires the Passpoint protocol. Please ensure your Ubiquiti network is using UniFi Network Controller version 8.4.54 or higher and AP firmware version 6.6.77 or AP firmware version 7.0.66 or higher, depending on hardware release track.  

You will also need:

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

### Submit NAS ID, Obtain RadSec Certificates
