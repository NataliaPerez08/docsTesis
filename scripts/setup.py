import subprocess


def create_virtual_interface(interface_name, ip_address, netmask):
    try:
        # Create a virtual interface
        subprocess.run(
            ["ip", "link", "add", "dev", interface_name, "type", "wireguard"]
        )

        # Set the IP address and netmask for the virtual interface
        subprocess.run(
            ["ip", "address", "add", f"{ip_address}/{netmask}", "dev", interface_name]
        )

        # Bring the virtual interface up
        subprocess.run(["ip", "link", "set", "dev", interface_name, "up"])

        print(
            f"Virtual interface {interface_name} created successfully with IP {ip_address}/{netmask}"
        )
    except Exception as e:
        print(f"Error creating virtual interface: {e}")


def load_wireguard_config(interface_name, config_file):
    try:
        # Load the WireGuard configuration from the config file
        subprocess.run(
            [
                "wg",
                "setconf",
                interface_name,
                config_file,
            ]
        )
    except Exception as e:
        print(f"Error loading WireGuard config: {e}")


# Example usage
create_virtual_interface("wg0", "192.168.2.2", "24")
load_wireguard_config("wg0", "../llaves/myarch.conf")
