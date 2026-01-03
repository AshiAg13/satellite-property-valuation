"""
data_fetcher.py

Downloads satellite images using latitude and longitude
via Mapbox Static Images API.

Intended to be run on Google Colab.
"""

import os
import requests
import pandas as pd
from tqdm import tqdm

# Configuration

MAPBOX_TOKEN =" KEY here "  
IMAGE_SIZE = "224x224"
ZOOM_LEVEL = 18

DATA_PATH = "data/processed/train_clean.csv"
IMAGE_DIR = "data/satellite_images"

os.makedirs(IMAGE_DIR, exist_ok=True)

# Load data

df = pd.read_csv(DATA_PATH)

# Image download function

def fetch_satellite_image(lat, lon, save_path):
    # NOTE: Mapbox expects longitude FIRST, then latitude
    url = (
        "https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/"
        f"{lon},{lat},{ZOOM_LEVEL}/{IMAGE_SIZE}"
        f"?access_token={MAPBOX_TOKEN}"
    )

    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
    else:
        print(f"Failed for location: {lat}, {lon}")


# Download loop (safe + resumable)

for idx, row in tqdm(df.iterrows(), total=len(df)):
    img_path = os.path.join(IMAGE_DIR, f"{idx}.png")

    if os.path.exists(img_path):
        continue

    fetch_satellite_image(row["lat"], row["long"], img_path)

print("Satellite image download complete.")
