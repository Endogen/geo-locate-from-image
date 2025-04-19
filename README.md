## 📍 geo-locate-from-image

A simple command-line Python tool to extract GPS coordinates from image metadata (EXIF) and plot them on an interactive map using [Folium](https://python-visualization.github.io/folium/).

Perfect for visualizing where a photo was taken — whether you're analyzing field data or solving a mystery like the USAID image example.

> 🧠 **Inspired by**:  
> [How to Extract GPS Coordinates from a Photo: The USAID Mystery](https://www.marsja.se/how-to-extract-gps-coordinates-from-a-photo-the-usaid-mystery/)  
> by Erik Marsja

---

### ✨ Features

- Extracts GPS coordinates (latitude and longitude) from EXIF data
- Converts DMS (Degrees, Minutes, Seconds) to decimal
- Plots the location on an interactive HTML map
- Lightweight and easy to use

---

### 📦 Requirements

- Python 3.11 or later
- Poetry (for dependency management)

---

### 🛠 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/geo-locate-from-image.git
cd geo-locate-from-image
```

2. **Install dependencies using Poetry:**

```bash
poetry install
```

> If you don't have Poetry, install it from [python-poetry.org](https://python-poetry.org/docs/#installation)

---

### 🚀 Usage

Run the tool with an image file path:

```bash
poetry run python extract_gps.py path/to/your/photo.jpg
```

If GPS data is present, the script will:
- Print the extracted latitude and longitude to the console
- Generate a file named `map.html` displaying the location

---

### 🧪 Example Output

```bash
Latitude: 38.8895, Longitude: -77.0352
Map saved to map.html
```

Open `map.html` in your browser to view the map.

---

### 🗂 Project Structure

```
geo-locate-from-image/
├── extract_gps.py       # Main script
├── pyproject.toml       # Poetry project metadata
├── poetry.lock          # Locked dependencies
└── README.md            # This file
```
