from faker import Faker
from faker.providers import BaseProvider
class LogProvider(BaseProvider):
    def LogLevel(self):
        levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]
        return self.random_element(levels) 
    def description(self):
        desc = ["User logged in successfully","Request processed successfully",
                "Password attempt limit nearing","Deprecated API used",
                "Database connection failed","Invalid input received",
                "System out of memory","Service crashed unexpectedly"]
        return self.random_element(desc)
    def http_code(self):
        codes = ["200","201","400","401","403","404","500","502","503"]
        return self.random_element(codes)
fake = Faker()
fake.add_provider(LogProvider)


def create_fake_logs(n):
    with open("server_log.txt","w",newline="") as f:
        # f.write("Date-Time Log-Level Description IP-Address HttpCode\n")
        for i in range(n):
            date_time = fake.date_time().strftime("%d-%m-25 %H:%M:%S")
            log_level = fake.LogLevel()
            description = fake.description()
            ip_address = fake.ipv4()
            http_code = fake.http_code()
            f.write(f"{date_time} {log_level} {description} {ip_address} {http_code}\n")
        print(f"{n} log entries created")
        
create_fake_logs(20)
