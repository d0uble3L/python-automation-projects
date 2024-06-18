# System Health Monitoring

The `system-health-monitoring.py` script monitors system health and performance metrics such as CPU usage, memory usage, and disk space. It logs these metrics to a text file or CSV file.

## Features

- Monitors CPU usage, memory usage, and disk space.
- Logs metrics to a text file or CSV file.
- Configurable logging intervals.

## Prerequisites

- Python 3.x
- `psutil` library

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/d0uble3L/python-automation-projects.git
    ```

2. Navigate to the project directory:

    ```sh
    cd python-automation-projects
    ```

3. Navigate to the `system-health-monitoring` directory:

    ```sh
    cd system-health-monitoring
    ```

4. Install the required dependencies:

    ```sh
    pip install psutil

    #OR 

    pip3 install psutil
    ```

## Usage

1. Open a terminal and navigate to the directory where the script is located.

2. Run the script with the desired logging interval (in seconds) and the output file format (txt or csv):

    ```sh
    python3 system-health-monitoring.py --interval 10 --output metrics.csv
    ```

3. The script will start monitoring the system and log the metrics at the specified interval to the output file.

## Example

Running the script:

```sh
python3 system-health-monitoring.py --output metrics.csv
```

### Basic Usage

```sh
#Log system health metrics every 1 second to a CSV file for 10 seconds (default duration):
python3 system-health-monitoring.py --interval 1 --output metrics.csv

# Custom Duration: Log system health metrics every 2 seconds to a text file for 30 seconds:
python3 system-health-monitoring.py --interval 2 --output metrics.txt --duration 30

#High Frequency Logging: Log system health metrics every 0.5 seconds to a CSV file for 10 seconds:
python3 system-health-monitoring.py --interval 0.5 --output high_freq_metrics.csv

#Long Duration Monitoring: Log system health metrics every 5 seconds to a text file for 5 minutes (300 seconds):
python3 system-health-monitoring.py --interval 5 --output long_duration_metrics.txt --duration 300

#Mixed Usage: Log system health metrics every 1 second to a CSV file for 10 seconds, then switch to logging to a text file for another 10 seconds:
python3 system-health-monitoring.py --interval 1 --output metrics.csv --duration 10
python3 system-health-monitoring.py --interval 1 --output metrics.txt --duration 10
```
