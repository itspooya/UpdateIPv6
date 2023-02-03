#!/bin/bash

current_ip=$(curl -s https://api.ipify.org)
api_key=$API_KEY
username=$USERNAME
tunnel_id=$TUNNEL_ID

if [ -z "$api_key" ] || [ -z "$username" ] || [ -z "$tunnel_id" ]; then
  echo "Missing environment variables"
  exit 1
fi

while true; do
  sleep 15
  new_ip=$(curl -s https://api.ipify.org)
  if [ "$current_ip" != "$new_ip" ]; then
    result=$(curl -s -u "$username:$api_key" "https://ipv4.tunnelbroker.net/nic/update?hostname=$tunnel_id")
    if [ "$result" == "good $new_ip" ] || [ "$result" == "nochg $new_ip" ]; then
      current_ip=$new_ip
      echo "IP updated to $current_ip"
    else
      echo "Failed to update ip"
      exit 1
    fi
  fi
done
