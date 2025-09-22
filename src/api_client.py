import requests


def get_public_ip():
    try:
        response = requests.get("https://api.ipify.org")
        response.raise_for_status()  # Raise an exception for bad status codes
        public_ip = response.text
        return public_ip
    except requests.exceptions.RequestException as e:
        print(f"Error getting public IP: {e}")
        return None


def get_location(ip):
    url = f"https://freeipapi.com/api/json/{ip}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return {
        "country": data["countryName"],
        "region": data["regionName"],
        "city": data["cityName"]
    }
