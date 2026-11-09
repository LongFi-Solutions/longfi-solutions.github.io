# LongFi Passpoint + RadSec on FortiGate & FortiAP — Configuration Guide (DRAFT)

> **Status:** Internal draft. Staged in `wlan-configs`. Once lab-validated it will be
> published to longfi-solutions.github.io → docs.longfisolutions.com.

## Overview

This guide configures a FortiGate (firewall + wireless controller) and its managed
FortiAPs to broadcast a LongFi Passpoint (Hotspot 2.0) SSID. Subscriber devices
authenticate automatically with EAP-TLS; the FortiGate carries RADIUS to LongFi
over **RadSec** (RADIUS over TLS, TCP 2083) to `connect.longfisolutions.com`.

**No radsecproxy is required.** Older Fortinet deployments (FortiOS 7.0–7.4)
used a local radsecproxy because FortiOS could only send plain UDP RADIUS for
Wi-Fi. FortiOS 7.6.0 added native RadSec for WPA2/WPA3-Enterprise SSIDs.

## Requirements

| Item | Requirement |
|---|---|
| FortiOS | **7.6.0 or later** (7.6.4+ recommended). 7.4.x supports RadSec for firewall/admin auth only, not Wi-Fi. |
| FortiAP firmware | Supported by your FortiOS release (see Fortinet compatibility matrix) |
| Outbound access | FortiGate → `connect.longfisolutions.com` TCP **2083** |
| DNS | FortiGate must resolve `connect.longfisolutions.com` |
| From LongFi | LongFi CA certificate chain, a site client certificate + private key, and a NAS-ID |

## What is configured where

| Task | GUI | CLI |
|---|:-:|:-:|
| Firmware upgrade | ✅ | |
| Import CA and client certificates | ✅ | |
| RADIUS server (RadSec / TLS options, client cert) | partial | ✅ |
| Hotspot 2.0 / ANQP profiles | | ✅ (CLI only) |
| SSID (VAP) + attach Hotspot 2.0 profile | partial | ✅ |
| SSID addressing, DHCP, firewall policy | ✅ | ✅ |
| Assign SSID to FortiAP profile | ✅ | ✅ |

## Step 1 — Upgrade FortiOS

**System → Firmware & Registration.** Upgrade to FortiOS 7.6.x following Fortinet's
upgrade path tool, then upgrade FortiAPs (**WiFi & Switch Controller → Managed FortiAPs**).

## Step 2 — Import certificates (GUI)

1. **System → Certificates → Create/Import → CA Certificate → File** — import the
   LongFi Root CA (and Intermediate CA, if provided). FortiOS names it `CA_Cert_N`.
2. **System → Certificates → Create/Import → Certificate → Import Certificate** —
   choose **PKCS #12** (or Certificate + key), upload the site certificate LongFi
   provided, and name it `<SITE_ID>`.

> If **Certificates** is missing from the menu, enable it under
> **System → Feature Visibility → Certificates**.

## Step 3 — Configure the RadSec server (CLI)

```
config user radius
    edit "LongFi-RadSec"
        set server "connect.longfisolutions.com"
        set secret radsec
        set radius-port 2083
        set transport-protocol tls
        set ca-cert "<CA_CERT_NAME>"
        set client-cert "<SITE_ID>"
        set server-identity-check enable
        set tls-min-proto-version TLSv1-2
        set nas-id-type custom
        set nas-id "<NAS_ID>"
        set acct-interim-interval 300
        config accounting-server
            edit 1
                set status enable
                set server "connect.longfisolutions.com"
                set secret radsec
                set port 2083
            next
        end
    next
end
```

Test reachability: `execute telnet connect.longfisolutions.com 2083`

## Step 4 — Hotspot 2.0 profiles (CLI)

Paste STEP 2 and STEP 3 from the template. These create:

| Object | Purpose |
|---|---|
| `anqp-roaming-consortium` | Roaming Consortium OIs advertised in beacons |
| `anqp-nai-realm` | Realms `longfisolutions.com`, `freedomfi.com`, `hellohelium.com` — EAP-TLS, certificate |
| `anqp-3gpp-cellular` | AT&T PLMN IDs: 310-410, 310-280, 310-150, 313-100 |
| `anqp-ip-address-type` | IPv4 single-NATed private |
| `anqp-venue-name` / `anqp-venue-url` | Venue info shown on devices |
| `h2qp-operator-name` | Operator friendly name (site-specific) |
| `h2qp-wan-metric` | Backhaul speed |
| `hs-profile` | Combines the above |

## Step 5 — Create the Passpoint SSID

Paste STEP 4 (VAP) and STEP 5 (interface, DHCP, firewall policy) from the template.
Tunnel mode is the default: client traffic returns to the FortiGate and is NATed.
For local-bridge mode, see the comments in the template.

## Step 6 — Broadcast on the FortiAPs

Paste STEP 6, or in the GUI: **WiFi & Switch Controller → FortiAP Profiles → <profile>**,
for Radio 1 and Radio 2 set **SSIDs → Manual** and add the Passpoint SSID
alongside existing SSIDs.

**6 GHz (FortiAP 431G and other 6E models):** WPA2-Enterprise SSIDs don't broadcast
on 6 GHz. To offer Passpoint on 6 GHz, create a second VAP with
`set security wpa3-only-enterprise` and `set pmf enable` using the same
`hotspot20-profile` and `radius-server`, and assign it to radio-3.

## Step 7 — Verify

```
diagnose debug application fnbamd -1
diagnose debug enable
#  connect a Passpoint device; look for "proto: TCP over TLS" and Access-Accept
diagnose debug disable
diagnose debug reset

diagnose wireless-controller wlac -d sta online
```

## Troubleshooting

| Symptom | Check |
|---|---|
| TLS handshake fails | Wrong/missing CA cert; client cert not issued by LongFi CA; system clock wrong (check NTP) |
| "server identity check" errors | Server name must match the cert CN/SAN. Use the FQDN, not an IP. As a last resort `set server-identity-check disable` |
| No TCP connection on 2083 | Upstream firewall/ISP blocking outbound 2083; DNS resolution |
| Device doesn't auto-join | Verify the device has a LongFi Passpoint profile; confirm RCOIs/realms in the hs-profile; confirm SSID is broadcasting (`diagnose wireless-controller wlac -c vap`) |
| Wi-Fi Calling fails | Ensure UDP 500/4500 and ESP aren't blocked on the SSID policy |

## References

- [FortiOS 7.6.0 — Support RADSEC on WPA2/WPA3-Enterprise SSID](https://docs.fortinet.com/document/fortigate/7.6.0/new-features/300051/support-radsec-on-wpa2-wpa3-enterprise-ssid)
- [FortiOS 7.6.4 — Configuring a RADSEC client](https://docs.fortinet.com/document/fortigate/7.6.4/administration-guide/729374/configuring-a-radsec-client)
- [FortiAP 7.6.4 — Hotspot 2.0 ANQP configuration](https://docs.fortinet.com/document/fortiap/7.6.4/fortiwifi-and-fortiap-configuration-guide/657393/hotspot-2-0-anqp-configuration)

https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/Fortinet_Product_Matrix.pdf

https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/Fortinet_Wireless_Product_Matrix.pdf

https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/pdf/fortiswitch-secure-access-series.pdf#page=9

https://www.fortinet.com/content/dam/fortinet/assets/data-sheets/pdf/fortiap-series.pdf#page=4
