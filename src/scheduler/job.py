from reports.generate_report import generate_mis
import schedule
import time

print("Scheduler started...")   # 👈 add this

generate_mis()  # 👈 immediate run for testing

schedule.every().day.at("10:00").do(generate_mis)

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("Scheduler stopped by user.")

