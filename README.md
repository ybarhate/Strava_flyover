# Strava_flyover
A Python-based tool to transform Strava activity data into cinematic 3D flyover animations. Features automated GPS/elevation extraction via Strava API, interactive 2D route previews, and dynamic 3D camera paths using Plotly and Streamlit. Perfect for visualizing cycling, running, or hiking routes in a professional, high-fidelity format.
# 🚴 Strava 3D Flyover Project

A cinematic visualization tool that turns your Strava activities into dynamic 3D flyovers. This project automates the journey from a Strava link to a high-fidelity interactive map with elevation profiles and drone-style camera movements.

## ✨ Features
* **Link Unfolder:** Automatically resolves mobile `strava.app.link` URLs to full activity IDs.
* **High-Res Data Extraction:** Pulls raw GPS (lat/long) and altitude streams for smooth path rendering.
* **2D Animated Preview:** Interactive map to trace your route frame-by-frame.
* **3D Cinematic Flyover:** A dark-themed 3D landscape visualization with automated camera panning to simulate a drone following your path.

## 🛠️ Built With
* [Python 3.10+](https://www.python.org/)
* [stravalib](https://github.com/stravalib/stravalib) - Strava API interaction
* [Plotly](https://plotly.com/python/) - 3D Graphing and animation
* [Pandas](https://pandas.pydata.org/) - Data manipulation
* [Streamlit](https://streamlit.io/) - Web interface

## 🚀 Getting Started

### 1. Prerequisites
You will need a Strava API **Access Token**. You can get one by creating an app at [strava.com/settings/api](https://www.strava.com/settings/api).

### 2. Installation
Clone the repository and install dependencies:
```bash
git clone [https://github.com/YOUR_USERNAME/strava-3d-flyover.git](https://github.com/YOUR_USERNAME/strava-3d-flyover.git)
cd strava-3d-flyover
pip install -r requirements.txt
3. Usage
Run the Streamlit application:

Bash
streamlit run app.py
