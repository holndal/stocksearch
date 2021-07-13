# https://nordvpn.com/ja/download/linux/
# wget https://repo.nordvpn.com/deb/nordvpn/debian/pool/main/nordvpn-release_1.0.0_all.deb?_ga=2.8046192.378988174.1626136669-1745960148.1626136669
# sudo apt-get install {/path/to/}nordvpn-release_1.0.0_all.deb
# sudo apt-get update
# sudo apt-get install nordvpn
# sudo usermod -aG nordvpn $USER
# sudo reboot
# nordvpn login
# https://github.com/kboghe/NordVPN-switcher
# pip3 install nordvpn-switcher

from nordvpn_switcher import initialize_VPN,rotate_VPN,terminate_VPN

def first():
    settings=initialize_VPN(area_input=["jp"], skip_settings=1)
    return settings

def notfirst(settings):
    rotate_VPN(settings, google_check=0)

if __name__ == "__main__":
    settings=first
    import time
    while(1):
        time.sleep(60*30)
        notfirst(settings)
