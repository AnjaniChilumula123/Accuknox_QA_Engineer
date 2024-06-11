import re
from collections import Counter

def parse_log_file(log_file_path):
    with open(log_file_path, 'r') as file:
        log_lines = file.readlines()
    return log_lines

def analyze_log(log_lines):
    # Regular Expressions for log patterns
    ip_pattern = re.compile(r'(\d{1,3}\.){3}\d{1,3}')
    status_pattern = re.compile(r'\s(\d{3})\s')
    page_pattern = re.compile(r'\"[A-Z]+\s(.*?)\sHTTP')

    ip_counter = Counter()
    page_counter = Counter()
    status_counter = Counter()


    for line in log_lines:
        ip_match = ip_pattern.search(line)
        status_match = status_pattern.search(line)
        page_match = page_pattern.search(line)

        if ip_match:
            ip_counter[ip_match.group()] += 1
        if status_match:
            status_counter[status_match.group(1)] += 1
        if page_match:
            page_counter[page_match.group(1)] += 1

    return ip_counter, status_counter, page_counter


def print_report(ip_counter, status_counter, page_counter):
    print("Log File Analysis Report")
    print("========================")
    print("\nNumber of 404 errors: ", status_counter.get('404', 0))
    
    print("\nMost requested pages:")
    for page, count in page_counter.most_common(10):
        print(f"{page}: {count} requests")
    
    print("\nIP addresses with the most requests:")
    for ip, count in ip_counter.most_common(10):
        print(f"{ip}: {count} requests")


def main():
    log_file_path = "sample_log.log"  # Use the generated sample log file
    log_lines = parse_log_file(log_file_path)
    ip_counter, status_counter, page_counter = analyze_log(log_lines)
    print_report(ip_counter, status_counter, page_counter)

if __name__ == "__main__":
    main()
