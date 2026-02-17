import re
import requests
from stravalib import Client

def get_activity_data(url, token):
    # 1. Automate mobile link unfolding
    if "strava.app.link" in url:
        url = requests.get(url, allow_redirects=True).url
    
    # 2. Extract ID
    match = re.search(r"activities/(\d+)", url)
    if not match:
        raise ValueError("Could not find Activity ID in URL.")
    
    activity_id = match.group(1)
    client = Client(access_token=token)
    
    # 3. Download GPS and Elevation streams
    streams = client.get_activity_streams(
        activity_id, 
        types=["latlng", "altitude"], 
        resolution="high"
    )
    
    if "latlng" not in streams:
        raise ValueError("No GPS data found. Check privacy settings!")
        
    return streams["latlng"].data, streams["altitude"].data