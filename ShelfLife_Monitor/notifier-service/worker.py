import time

def run_notifier():
    while True:
        print("Notifier Service: Checking for items near expiry...")
        time.sleep(10)

if __name__ == "__main__":
    run_notifier()
