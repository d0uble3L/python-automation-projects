import psutil
import time
import csv
import argparse
from datetime import datetime

def log_metrics(output_file, interval, file_format, duration):
    end_time = time.time() + duration
    while time.time() < end_time:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cpu_usage = psutil.cpu_percent(interval=interval)
        memory_info = psutil.virtual_memory()
        memory_usage = memory_info.percent
        disk_info = psutil.disk_usage('/')
        disk_usage = disk_info.percent

        if file_format == 'csv':
            with open(output_file, 'a', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerow([timestamp, cpu_usage, memory_usage, disk_usage])
        else:
            with open(output_file, 'a') as txtfile:
                txtfile.write(f'{timestamp}, CPU: {cpu_usage}%, Memory: {memory_usage}%, Disk: {disk_usage}%\n')

        time.sleep(interval)  # Adjust sleep time to account for interval

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='System Health Monitoring Script')
    parser.add_argument('--interval', type=float, default=1.0, help='Logging interval in seconds')
    parser.add_argument('--output', type=str, default='metrics.txt', help='Output file name')
    parser.add_argument('--duration', type=int, default=10, help='Duration for monitoring in seconds')
    args = parser.parse_args()

    file_format = 'csv' if args.output.endswith('.csv') else 'txt'

    # Write header for CSV file
    if file_format == 'csv':
        with open(args.output, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(['timestamp', 'cpu_usage', 'memory_usage', 'disk_usage'])
    
    log_metrics(args.output, args.interval, file_format, args.duration)


