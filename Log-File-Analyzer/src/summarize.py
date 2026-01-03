import re
unique_ip = set()
ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
ip_lst = {}
with open("server_log.txt", "r") as f:
    logs = f.readlines()
    for line in logs[1:]:
        ip_lst = re.findall(ip_pattern, line)
        if ip_lst:
            print(ip_lst)
        
        


