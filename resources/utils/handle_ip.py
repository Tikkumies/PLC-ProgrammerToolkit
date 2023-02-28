import ipaddress
import subprocess

class IpFunctions:
    @staticmethod
    def change_ip(mode, name="", ip="", mask="", gateway="", diag_window=""):
        command = ""
        try:
            if mode == "static":
                command = "netsh interface ip set address " + name + \
                    " static " + ip + " " + mask + " " + gateway
                print(command)
                # Check for valid IP address
                ipaddress.ip_address(ip)
                ipaddress.ip_address(mask)
                ipaddress.ip_address(gateway)

            elif mode == "dhcp":
                command = "netsh interface ip set address " + name + " dhcp"

            subprocess.run(command)

        except ValueError:
            diag_window.show()

    @staticmethod
    def get_text_from_command_line():
        command = "ipconfig"
        completed_process = (subprocess.run(command, capture_output=True))
        string = str(completed_process.stdout).replace(
            "\\n", " ").replace("\\r", " ")
        return string
    
    @staticmethod
    def get_network_adapter_data(data_to_search, string):
        match data_to_search:
            case "name":
                start = "Ethernet adapter "
            case "ip":
                start = "IPv4 Address"
            case "mask":
                start = "Subnet Mask"
            case "gateway":
                start = "Default Gateway"

        adapter_list = []

        while string.find(start) != -1:
            split_start = string.partition(start)
            split_colon = split_start[2].partition(": ")
            adapter_data = split_colon[2].partition(" ")
            if data_to_search == "name":
                adapter_list.append(split_colon[0])
                string = split_colon[2]
            else:
                adapter_list.append(adapter_data[0])
                string = adapter_data[2]
        return (adapter_list)
    
if __name__ == "__main__":
    IpFunctions.get_network_adapter_data("name", IpFunctions.get_text_from_command_line())

