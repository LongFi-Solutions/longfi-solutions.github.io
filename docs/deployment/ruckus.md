---
title: Ruckus One Configuration
---

# Ruckus One Passpoint Conversion Guide

!!! note "Coming Soon"
    Step by Step guide with Screenshots coming soon.  For now this guide covers the basic settings.  Please contact us for server IP addresses, shared secrets, and carrier activation info

***

For support please contact: [support@longfisolutions.com](mailto:support@longfisolutions.com)

***

## **High Level Steps:**

1. Configure RADIUS Profile
2. Configure Wi-Fi Operator Profile
3. Configure Identity Provider Profile
4. Configure Wi-Fi Network

***

### **Configure RADIUS Profile**

First, we will configure the RADIUS Profile used to authenticate Passpoint clients to the LongFi Connect AAA Servers based on their SIM identity.  

- From the left side menu in the R1 dashboard, go to **Network Control > Service Catalog**
- Search the Service Catalog for **RADIUS Server**
- Click **Add** to add the **RADIUS Server** to your **My Services** dashboard
- From the left side menu in the R1 dashboard, go to **Network Control > My Services**
- Click on **RADIUS Server** to open the RADIUS Server dashboard
- From the RADIUS Server dashboard, click **Add RADIUS Server** in the top right corner
- From the **Add RADIUS Server** screen, set the **Profile Name** to **LongFi RADIUS Authentication**
- For **Type** select **Authentication RADIUS Server**
- For **Server Address Type** select **IP Address**
- Under **Primary Server** set the **IP Address** to **34.174.99.2**
- Set the **Port** to **1812**
- Set the **Shared Secret** to the secret provided in your onboarding and activation emails
- \*Please note: the shared secret link will expire after one click, please be ready to save the shared secret to your secure password keeper before you click on the link.
- Click **Add** to save the new RADIUS Authentication Server
- From the **RADIUS Server** screen, click **Add RADIUS Server** again to add an accounting server 
- From the **Add RADIUS Server** screen, set the **Profile Name** to **LongFi RADIUS Accounting**
- For **Type** select **Accounting RADIUS Server**
- For **Server Address Type** select **IP Address**
- Under **Primary Server** set the **IP Address** to **34.174.99.2**
- Set the **Port** to **1813**
- Set the **Shared Secret** to the secret provided in your onboarding and activation emails
- \*Please note: the shared secret link will expire after one click, please be ready to save the shared secret to your secure password keeper before you click on the link.
- Hit **Add** to save the new RADIUS Accounting Server

***

### **Configure Wi-Fi Operator Profile**

Next, we will configure the Wi-Fi Operator Profile

- From the left side menu in the R1 dashboard, go to **Network Control > Service Catalog**
- Search the Service Catalog for **Wi-Fi Operator**
- Click **Add** to add **Wi-Fi Operator** to your **My Services** dashboard
- From the left side menu in the R1 dashboard, go to **Network Control > My Services**
- Click on **Wi-Fi Operator** to open the Wi-Fi Operator dashboard
- From the **Wi-Fi Operator** dashboard click **Add Wi-Fi Operator**
- On the next screen set the **Profile Name** to **LongFi Wi-Fi Operator**
- Under **Domain** enter the following domains (one domain per line):
    - [longfisolutions.com](http://longfisolutions.com)
    - [freedomfi.com](http://freedomfi.com)
- Under **Operator Friendly Name** set the **Language** to **English**
- Set the **Friendly Name** to **LONGFISOLUTIONS:US**
- At the bottom of the screen click **Add** to add the new operator profile

***

### **Configure Identity Provider Profile**

Next, we will configure the Identity Provider Profile.  Some of the settings for this section of the configuration do not require activation approval and will be provided in this guide.  Some of the settings for the IDP configuration require activation approval, and will be provided in your onboarding and activation emails.  These will include NAI Realms, PLMN IDs (3gpp, MCC, MNC), and EAP settings.  Please have that information ready, you will add the Realms and PLMNs from your activation email after adding the realms, PLMN IDs, and Roaming Consortium OIs (RCOIs) shown in this guide.

#### Create the Identity Provider Profile:

- From the left side menu in the R1 dashboard, go to **Network Control > Service Catalog**
- Search the Service Catalog for **Identity Provider**
- Click **Add** to add **Identity Provider** to your **My Services** dashboard
- From the left side menu in the R1 dashboard, go to **Network Control > My Services**
- Click on **Identity Provider** to open the Identity Provider dashboard
- From the **Identity Provider** dashboard, select **Hotspot 2.0** (next to SAML) to open the Hotspot 2.0 IDP list
- From the **Identity Provider > Hotspot 2.0** screen, click the **Add HS2.0 IdP** in the top right hand corner
- On the next screen under **Network Identifier** set the **Profile Name** to **LongFi IDP**

#### Configure Identity Provider NAI Realms:

- From the same **Add Identity Provider** screen, under **NAI Realm** click on **Add Realm**
- From the **Add Realm** window set the **Realm Name** to **longfisolutions.com**
- Under **EAP Methods** click **Add EAP Method**
- From the **EAP Method** pull down menu, select **EAP-TLS**
- Click **Add another Auth** 
- From the **Auth Type** pull down menu select **Credential**
- From the **SubType** pull down menu select **Certificate**
- Click **Add** in the bottom right hand corner of the EAP window
- From the **Add Realm** window, check the box at the bottom to **Add another Realm**
- Click the **Add** button in the bottom right corner to add the new realm
- You will see the same **Add Realm** screen again
- The next two realms will have the exact same settings (EAP-TLS, Credential > Certificate) with a different realm name
- From the **Add Realm** window set the **Realm Name** to **freedomfi.com**
- Under **EAP Methods** click **Add EAP Method**
- From the **EAP Method** pull down menu, select **EAP-TLS**
- Click **Add another Auth** 
- From the **Auth Type** pull down menu select **Credential**
- From the **SubType** pull down menu select **Certificate**
- Click **Add** in the bottom right hand corner of the EAP window
- From the **Add Realm** window, check the box at the bottom to **Add another Realm**
- Click the **Add** button in the bottom right corner to add the new realm
- You will see the same **Add Realm** screen again
- From the **Add Realm** window set the **Realm Name** to **hellohelium.com**
- Under **EAP Methods** click **Add EAP Method**
- From the **EAP Method** pull down menu, select **EAP-TLS**
- Click **Add another Auth** 
- From the **Auth Type** pull down menu select **Credential**
- From the **SubType** pull down menu select **Certificate**
- Click **Add** in the bottom right hand corner of the EAP window
- From the **Add Realm** window, check the box at the bottom to **Add another Realm**
- Click the **Add** button in the bottom right corner to add the new realm
- You will see the same **Add Realm** screen again
- Now you can enter the additional NAI Realms provided in your onboarding and activation email.  If you have not yet been approved for multiple carriers, you may not be provided additional realms yet and you can proceed to the PLMN steps.
- The additional NAI Realms will (almost) always have the EAP Method set to **EAP-AKA Authentication** and no submethods.  Be careful to use **EAP-AKA Authentication** and not **EAP-AKA’**
- Follow the same steps as above to add the additional NAI Realms using the specified EAP methods and click **Add** when you are done

#### Configure Identity Provider PLMN IDs:

- From the same **Add Identity Provider** screen, scroll down to **PLMN** and click **Add PLMN**
- The Carrier **PLMN** IDs will be provided in your onboarding and activation emails
- Each PLMN will have an MCC number and an MNC number
- Copy and paste the MCC numbers into the **MCC** box
- Copy and paste the MNC numbers into the **MNC** box
- Check the box at the bottom for **Add another PLMN** and click **Add**
- Repeat this process until you have added all PLMNs that are approved for activation at your site.  There will normally be 4 PLMN MCC/MNC lines

#### Configure Roaming Consortium OIs (RCOIs):

- From the same **Add Identity Provider** screen, scroll down to **Roaming Consortium OI** and click **Add OI**
- From the **Add Roaming Consortium OI** set the **OI name** to **Orion**
- Under **Organization ID** select **5 hex**
- Enter the following RCOI into the 5 hex windows 2 characters at a time **F4F5E8F5F4**
- Click **Add another OI** at the bottom of the window
- Click **Add** to add another OI
- From the **Add Roaming Consortium OI** set the **OI name** to **Uplink**
- Under **Organization ID** select **5 hex**
- Enter the following RCOI into the 5 hex windows 2 characters at a time **2A2F830000**
- Click **Add** to add the Uplink OI
- If you want to add OpenRoaming to your network, repeat this process using the OpenRoaming RCOIs (inquire by email for more information)

#### Configure AAA Settings:

- Once you have added all Realms, PLMNs, and RCOIs, at the bottom of the screen click **Next** to proceed to **AAA Settings**
- From the **AAA Settings** window, under **Authentication Server** select the **LongFi RADIUS Authentication** server we created earlier
- Click the button to enable **Accounting Service**
- Under **Accounting Server** select the **LongFi RADIUS Accounting** server we created earlier
- From the bottom of the screen click the **Next** button to review the **Summary** of the **Add Identity Provider** configuration
- From the bottom of the screen click **Add** to add the new Identity Provider

***

### **Configure the Wi-Fi Network**

Next we will configure the Wi-Fi Network.  Please note that this guide only covers settings specific to Passpoint/Hotspot 2.0.  For any settings such as roaming protocols, Wi-Fi channels, radio transmit power, etc, please consult our Best Practices guide for general recommendations and consideration.  And please follow the requirements of your organization, vendor recommendations, and industry best practices based on your unique environment.

- From the R1 main dashboard, in the left menu bar go to **Wi-Fi > Wi-Fi Networks List**
- In the top right corner click **Add Wi-Fi Network**
- In the **Create New Network** screen, under **Network Details > Network Name**, set the name to **LongFi Passpoint**
- You may use a different SSID name if you like, the SSID name does not matter in Passpoint/Hotspot 2.0, clients look for their SIM identity in the Wi-Fi beacon
- Under **Network Type** select **Hotspot 2.0 Access**
- At the bottom of the screen hit **Next**
- Under **Hotspot 2.0 Settings > Security Protocol** select **WPA2** to support the most possible clients
- If you have 6GHz capable APs, you must select **WPA3** as WPA3 is mandatory in 6 GHz
- LongFi recommends enabling 6 GHz where capable, and choosing WPA3.  We find that almost all Passpoint capable clients can now support WPA3 Enterprise with a mixed 5+6 GHz SSID with no issues
- We do not recommend enabling 2.4 GHz on Passpoint Wi-Fi
- Under **Wi-Fi Operator** select the **LongFi Wi-Fi Operator** profile we created earlier in the Network Control Services
- Under **Identity Provider** select the **LongFi IDP** identity provider profile we created earlier in the Network Control Services
- At the bottom middle of the main window, click **Show more settings**
- Under **VLAN > VLAN ID** you can set your access VLAN for the Passpoint SSID
- Under the **Network Control** enable **Client Isolation**
- Under the **Networking** tab scroll down to **RADIUS Options**
- Under **RADIUS Options > NAS ID** select **User-defined** from the drop down menu
- Copy and paste the NAS ID you provided to register and activate your site.  This is usually a MAC address.  You can find your NAS ID in the onboarding and activation emails.  **\*Important: see notes below for instructions on deploying the Wi-Fi Network to multiple sites and setting site-unique NAS IDs**
- At the bottom of the screen click **Next**
- On the **Venues** screen click the **Activated** button to activate the Passpoint Wi-Fi Network at your specified Venue
- At the bottom of the screen click **Apply/Save/Next** to save the new Passpoint Wi-Fi Network
- If the Wi-Fi network has been applied to a Venue, AP Groups, and APs and is broadcasting, you may now test Passpoint Wi-Fi with compatible SIM based clients

***

Congratulations, you have successfully activated LongFi Connect Passpoint on your Ruckus One Network!

!!! note "The NAS ID must be unique for every site"
    You are able to deploy a Wi-Fi Network to multiple sites/venues in R1.  If you are deploying the Wi-Fi Network configuration to multiple sites, you can set the site-unique NAS ID for each Venue.  To do this go to **Venues** on the left menu bar, select the Venue you want to activate, and click **Configure.**  Go to **Wi-Fi Configuration > Networking** and scroll down to **RADIUS Service**.  Enable the option **Override the RADIUS options in active networks**.  Under **NAS ID** select **User-defined** from the drop down menu.  You may now copy paste the NAS ID for your site into the **Custom NAS ID** box and click **Save** at the bottom of the page
