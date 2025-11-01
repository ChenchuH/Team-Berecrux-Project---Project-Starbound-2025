import subprocess
import re

def get_local_ip_address():
    ip_pattern = r'IPv4 Address[.\s]*:\s*(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    scan_result=subprocess.check_output(['ipconfig'], text=True)
    matching=re.search(ip_pattern,scan_result)
    #re.search(pattern, string)
    return matching.group(1)

if __name__ == "__main__":
    get_local_ip_address()