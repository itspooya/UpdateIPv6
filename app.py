import requests
import os
import time


def set_env() -> tuple:
    api_key = os.environ.get('API_KEY')
    username = os.environ.get('USERNAME')
    tunnel_id = os.environ.get('TUNNEL_ID')
    if not all((api_key, username, tunnel_id)):
        raise Exception('Missing environment variables')
    return api_key, username, tunnel_id


def get_current_ip() -> str:
    """Return the current IP address of the machine running the script."""
    return requests.get('https://api.ipify.org').text


def update_tunnel_broker_ip(tunnel_id: str, api_key: str, username: str) -> bool:
    """Update the IP address in the tunnel broker."""
    result = requests.get(f'https://{username}:{api_key}@ipv4.tunnelbroker.net/nic/update?hostname={tunnel_id}')
    return result.status_code == 200


if __name__ == '__main__':
    api_key, username, tunnel_id = set_env()
    current_ip = get_current_ip()

    while True:
        time.sleep(15)
        new_ip = get_current_ip()
        if new_ip != current_ip:
            if update_tunnel_broker_ip(tunnel_id, api_key, username):
                current_ip = new_ip
                print(f'IP updated to {current_ip}')
            else:
                raise Exception('Failed to update IP address')
