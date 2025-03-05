import subprocess

def fetch_logs():
    try:
        syslog_output = subprocess.getoutput("tail -n 10 /var/log/syslog")
        authlog_output = subprocess.getoutput("tail -n 10 /var/log/auth.log")

        print("\n🔹 /var/log/syslog Logs:")
        print(syslog_output)

        print("\n🔹 /var/log/auth.log Logs:")
        print(authlog_output)
    
    except Exception as e:
        print(f"Error fetching logs: {e}")

if __name__ == "__main__":
    fetch_logs()
