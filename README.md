IP Updater

This project is a script for updating the IP address of a tunnel broker.
Requirements

To run this script, you need to have the following software installed:

    Python 3.x
    pip

Additionally, you will need to install the required packages, which are listed in the requirements.txt file. You can install these packages by running the following command in the terminal or command prompt:

```bash
pip install -r requirements.txt
```

## Configuration

Before running the script, you need to set the following environment variables:

- `API_KEY`: The API key for the tunnel broker.
- `USERNAME`: The username for the tunnel broker.
- `TUNNEL_ID`: The tunnel ID for the tunnel broker.

## Running the script

To run the script, simply execute the following command in the terminal or command prompt:

```bash
python updater.py
```

The script will then run indefinitely, checking the IP address of the machine every 15 seconds and updating the IP address of the tunnel broker if it has changed.

## Bash Script

Alternatively, you can use the bash script instead of running the python code. To do so, follow these steps:

Make the bash script executable by running the following command in the terminal:
    
```bash
chmod +x update_tunnel_broker_ip.sh
```
Set the environment variables by running the following command in the terminal:
```bash
export API_KEY='YOUR_API_KEY'
export USERNAME='YOUR_USERNAME'
export TUNNEL_ID='YOUR_TUNNEL_ID'
```
Run the bash script by running the following command in the terminal:
```bash
./update_ip.bash
```