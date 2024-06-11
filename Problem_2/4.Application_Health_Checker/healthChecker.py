import requests
import time

def check_uptime(url):

    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return "UP", response.status_code, "The application is responding with status code 200 (OK)."
        else:
            return "DOWN", response.status_code, f"The application is responding with status code {response.status_code}."
    except requests.exceptions.Timeout:
        return "DOWN", None, "The request timed out."
    except requests.exceptions.ConnectionError:
        return "DOWN", None, "There was a connection error."
    except requests.exceptions.RequestException as e:
        return "DOWN", None, f"An error occurred: {str(e)}"

def main():

    url = "https://www.google.com"  # Replace this with the URL of your application
    #url = "http://127.0.0.1:5000/status"
    print(f"Checking uptime for {url}... Press Ctrl+C to stop.")

    try:
        while True:
            # Call the check_uptime function and store the result
            status, status_code, reason = check_uptime(url)
            
            # Print the status of the application along with the reason and status code
            if status_code:
                print(f"Status: {status} (HTTP Status Code: {status_code})")
            else:
                print(f"Status: {status}")
            print(f"Reason: {reason}")
            
            # Wait for a specified interval before checking again
            time.sleep(10)  # Check every 10 seconds
    except KeyboardInterrupt:
        print("Uptime check stopped by user.")

if __name__ == "__main__":
    main()
