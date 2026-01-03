import re
unique_ip = set()
ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
http_pattern = r"\d{3}$"
ip_lst = []
def summarize_unique_ip():
    with open("server_log.txt", "r") as f:
        with open('log_summary.txt', 'w') as s:
            s.write("Unique IP Addresses:\n")
            logs = f.readlines()
            ip_lst=[]
            ip_set = set()
            for line in logs:
                ip_lst.extend(re.findall(ip_pattern, line))
            if ip_lst:
                ip_set = set(ip_lst)
            for ip in ip_set:
                count = 0
                for i in ip_lst:
                    if i == ip:
                        count += 1
                s.write(f"{ip} ")
                s.write(f"     :  {count} \n")
    print("server Log summarized")

def summerize_http_status():
    with open("server_log.txt", "r") as f:
        with open('log_summary.txt', 'a') as s:
            s.write("HTTP Status Codes:\n")
            logs = f.readlines()
            http_lst=[]
            for line in logs:
                http_lst.extend(re.findall(http_pattern, line))
            http_set = set(http_lst)
            for code in http_set:
                count = 0
                for i in http_lst:
                    if i == code:
                        count += 1
                s.write(f"{code} : {count} \n")
    print("server Log summarized")
summarize_unique_ip()
summerize_http_status()
