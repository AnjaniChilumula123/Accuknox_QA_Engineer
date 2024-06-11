#!/bin/bash

CPU_THRESHOLD=80
MEMORY_THRESHOLD=80
DISK_THRESHOLD=80
LOG_FILE="/path/to/system_health.log"

# Function to log messages
log_message() {
    local MESSAGE=$1
    echo "$(date): $MESSAGE" | tee -a "$LOG_FILE"
}

# Function to check CPU usage
check_cpu() {
    CPU_USAGE=$(top -bn1 | grep "Cpu(s)" | awk '{print $2 + $4}')
    CPU_USAGE=${CPU_USAGE%.*}
    echo "Current CPU usage: $CPU_USAGE%"  
    if [ "$CPU_USAGE" -gt "$CPU_THRESHOLD" ]; then
        log_message "Warning: High CPU usage detected: $CPU_USAGE%"
    fi
}

# Function to check memory usage
check_memory() {
    MEMORY_USAGE=$(free | grep Mem | awk '{print $3/$2 * 100.0}')
    MEMORY_USAGE=${MEMORY_USAGE%.*}
    echo "Current memory usage: $MEMORY_USAGE%"  
    if [ "$MEMORY_USAGE" -gt "$MEMORY_THRESHOLD" ]; then
        log_message "Warning: High memory usage detected: $MEMORY_USAGE%"
    fi
}

# Function to check disk usage
check_disk() {
    DISK_USAGE=$(df / | grep / | awk '{print $5}' | sed 's/%//g')
    echo "Current disk usage: $DISK_USAGE%"  
    if [ "$DISK_USAGE" -gt "$DISK_THRESHOLD" ]; then
        log_message "Warning: High disk usage detected: $DISK_USAGE%"
    fi
}

# Function to check running processes
check_processes() {
    RUNNING_PROCESSES=$(ps aux | wc -l)
    echo "Running processes: $RUNNING_PROCESSES"
}

check_cpu
check_memory
check_disk
check_processes
