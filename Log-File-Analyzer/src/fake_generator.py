from faker import Faker 

log_levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]

descriptions ={
    "INFO": ["User logged in successfully","Request processed successfully"],
    "WARNING": ["Password attempt limit nearing","Deprecated API used"],
    "ERROR": ["Database connection failed","Invalid input received"],
    "CRITICAL": ["System out of memory","Service crashed unexpectedly"]
    }

def create_fake_logs(n):
    with open("server_log.txt","w",newline="") as f:
        f.write("Date-Time Log-Level Description IP-Address HttpCode\n")
        fake = Faker()
        for i in range(1,n):
            date_time = fake.date_time().strftime("%d-%m-25 %H:%M:%S")
            log_level = fake.random_element(log_levels)
            description = fake.random_element(descriptions[log_level])
            ip_address = fake.ipv4()
            http_code = fake.http_status_code()
            f.write(f"{date_time} {log_level} {description} {ip_address} {http_code}\n")
        print(f"{n} log entries created")
        
create_fake_logs(10)
