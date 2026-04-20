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

[IMAGE HERE]

Submit this MAC address during your site Onboarding & Activation, and return to this guide after the network is onboarded and RadSec certificates have been delivered.

***

#### Configure UniFi Network Controller

After retrieving certificates, configuring the network controller for Passpoint is a two-part process. First, create the RADIUS profile, then apply the profile to a newly created WiFi SSID called 'LongFi Passpoint'.

#### Create a RADIUS Profile

Configure a TLS connection to LongFi Connect AAA servers, which performs Authentication, Authorization, and Accounting for the end customers. Enabling RADIUS communication over TLS (RadSec) increases the level of security for authentication that is carried out across the cloud network.

In the sidebar, choose Settings, then Profiles, then RADIUS, then click **Create New**:

[IMAGE HERE]

For the profile name enter **LongFi RadSec**.
