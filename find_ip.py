import requests

def get_ip_info(ip_address):
    url = f"http://ipinfo.io/{ip_address}/json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    ip_address = input("Enter the IP address to lookup: ")
    ip_info = get_ip_info(ip_address)

    if ip_info:
        print(f"IP Address: {ip_info.get('ip', 'N/A')}")
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
