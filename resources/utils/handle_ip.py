import ipaddress
import subprocess


def change_ip(mode, name="", ip="", mask="", gateway="", diag_window=""):
    command = ""
    try:
        if mode == "static":
            command = "netsh interface ip set address " + name + \
                " static " + ip + " " + mask + " " + gateway
            # Check for valid IP address
            ipaddress.ip_address(ip)
            ipaddress.ip_address(mask)
            ipaddress.ip_address(gateway)

        elif mode == "dhcp":
            command = "netsh interface ip set address " + name + " dhcp"

        subprocess.run(command)

    except ValueError:
        diag_window.show()


def get_network_adapter_data(data):
    match data:
        case "name":
            find_start = "Ethernet adapter "
            find_end = ":"
        case "ip":
            find_start = "IPv4 Address. . . . . . . . . . . : "
            find_end = " "
        case "mask":
            find_start = "Subnet Mask . . . . . . . . . . . : "
            find_end = " "
        case "gateway":
            find_start = "Default Gateway . . . . . . . . . : "
            find_end = " "
        case "all":
            pass

    command = "ipconfig"
    completed_process = (subprocess.run(command, capture_output=True))
    string = str(completed_process.stdout).replace(
        "\\n", " ").replace("\\r", " ")
    adapter_list = []
    x = True
    while x == True:
        start = string.find(find_start) + len(find_start)
        end = string.find(find_end, start)

        if string.find(find_start) == -1:
            x = False
        else:
            adapter_list.append(string[start:end])
            string = string[end:]
    return (adapter_list)
