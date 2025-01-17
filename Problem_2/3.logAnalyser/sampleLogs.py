# generate_sample_log.py

sample_log = """
127.0.0.1 - - [10/Jun/2024:15:32:01 +0000] "GET /index.html HTTP/1.1" 200 1043
127.0.0.1 - - [10/Jun/2024:15:32:05 +0000] "GET /nonexistent.html HTTP/1.1" 404 345
192.168.1.1 - - [10/Jun/2024:15:32:10 +0000] "POST /form HTTP/1.1" 200 256
192.168.1.1 - - [10/Jun/2024:15:32:15 +0000] "GET /index.html HTTP/1.1" 200 1043
10.0.0.1 - - [10/Jun/2024:15:32:20 +0000] "GET /about.html HTTP/1.1" 200 789
10.0.0.1 - - [10/Jun/2024:15:32:25 +0000] "GET /index.html HTTP/1.1" 200 1043
192.168.1.2 - - [10/Jun/2024:15:32:30 +0000] "GET /contact.html HTTP/1.1" 200 567
10.0.0.2 - - [10/Jun/2024:15:32:35 +0000] "GET /index.html HTTP/1.1" 200 1043
127.0.0.2 - - [10/Jun/2024:15:32:40 +0000] "GET /nonexistent.html HTTP/1.1" 404 345
192.168.1.3 - - [10/Jun/2024:15:32:45 +0000] "GET /index.html HTTP/1.1" 200 1043
"""

with open("sample_log.log", "w") as file:
    file.write(sample_log)
