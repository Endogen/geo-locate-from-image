#!/usr/bin/env python3

import sys
import os
import exifread
import folium

def dms_to_dd(dms):
    """Convert degrees, minutes, seconds to decimal degrees."""
    degrees = float(dms[0])
    minutes = float(dms[1])
    seconds = float(dms[2])
    return degrees + (minutes / 60.0) + (seconds / 3600.0)

def extract_gps_coords(image_path):
    """Extract GPS coordinates from image EXIF data."""
    with open(image_path, 'rb') as f:
        tags = exifread.process_file(f)

    lat_key = 'GPS GPSLatitude'
    lat_ref_key = 'GPS GPSLatitudeRef'
    lon_key = 'GPS GPSLongitude'
    lon_ref_key = 'GPS GPSLongitudeRef'

    if all(k in tags for k in [lat_key, lon_key, lat_ref_key, lon_ref_key]):
        lat = dms_to_dd(tags[lat_key].values)
        lon = dms_to_dd(tags[lon_key].values)

        if tags[lat_ref_key].printable != 'N':
            lat = -lat
        if tags[lon_ref_key].printable != 'E':
            lon = -lon

        return lat, lon
    else:
        return None

def plot_map(lat, lon, output_file='map.html'):
    """Plot the GPS coordinates on a map and save to HTML."""
    m = folium.Map(location=[lat, lon], zoom_start=15)
    folium.Marker([lat, lon], popup='Photo Location').add_to(m)
    m.save(output_file)
    print(f"Map saved to {output_file}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract_gps.py <image_file>")
        sys.exit(1)

    image_path = sys.argv[1]

    if not os.path.isfile(image_path):
        print(f"File not found: {image_path}")
        sys.exit(1)

    coords = extract_gps_coords(image_path)
    if coords:
        lat, lon = coords
        print(f"Latitude: {lat}, Longitude: {lon}")
        plot_map(lat, lon)
    else:
        print("No GPS data found in the image.")

if __name__ == '__main__':
    main()

