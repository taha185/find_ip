import requests
import time

# Display a simple banner
def display_banner():
    print("=" * 50)
    print("     WELCOME TO THE IP INFO LOOKUP TOOL     ")
    print("        Made by Taha 185 - Version 1.0      ")
    print("=" * 50)
    print("Disclaimer: This tool is for informational purposes only.")
    print("Use responsibly and ensure you have permission to query IP addresses.")
    print("=" * 50)

# Display loading or waiting message
def loading_message():
    print("\nFetching IP information... Please wait.")
    time.sleep(1)

def get_ip_info(ip_address):
    url = f"http://ipinfo.io/{ip_address}/json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

        # If the response is successful (200 status code)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching IP info: {e}")
        return None

def main():
    display_banner()  # Display the banner with info and disclaimer
    ip_address = input("Enter the IP address to lookup: ")

    loading_message()  # Show waiting message while fetching info

    ip_info = get_ip_info(ip_address)

    if ip_info:
        print(f"\nIP Address: {ip_info.get('ip', 'N/A')}")
        print(f"City: {ip_info.get('city', 'N/A')}")
        print(f"Region: {ip_info.get('region', 'N/A')}")
        print(f"Country: {ip_info.get('country', 'N/A')}")
        print(f"Location: {ip_info.get('loc', 'N/A')}")
        print(f"Organization: {ip_info.get('org', 'N/A')}")
        print(f"Timezone: {ip_info.get('timezone', 'N/A')}")
    else:
        print("Failed to retrieve IP information.")

if __name__ == "__main__":
    main()

