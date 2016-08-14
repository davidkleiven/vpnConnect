# Setup
* Install the openconnect (as root):
  ```bash
  apt-get install network-manager-openconnect
  ```

* Install the vpnc-scripts
  ```bash
  apt-get install vpnc-scripts
  ```

* Run the config script
  ```bash
  python config.py --command=<path to exec> --script=<vpnc-script> --adress=<vpn.address> --out=<outfile.sh>
  ```

# VPN
The VPN connection address to NTNU is *https://sslvpn.ntnu.no*.

# Example of paths
On my computer (debian 8) the command is located at */usr/sbin/openconnect*. 
The vpnc script is located at */usr/share/vpnc-scripts/vpnc-script*.

Hence to configure:
```bash
python config.py --command=/usr/sbin/openconnect --script=/usr/share/vpnc-scripts/vpnc --address=https://sslvpn.ntnu.no --out=vpnntnu.sh
```

Using the example above one can connect via vpn by running (as root)
```bash
bash vpnntnu.sh
```
