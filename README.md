<img width="1024" height="1024" alt="Copilot_20260713_040333" src="https://github.com/user-attachments/assets/09e260db-22f1-4f7c-9c3f-5dc2d7177ba6" />


# 🌐 Shiny Website To EXE Converter

A simple Python application that converts a website into a Windows desktop application.

## Features

- 🌍 Convert an online website using its URL
- 📁 Convert a local HTML website
- 🖥️ Choose a custom app name
- 📂 Select an output folder
- ⚡ Build a standalone Windows EXE

## Requirements

- Python 3.10+
- PySide6
- PyInstaller

Install dependencies:

```bash
pip install PySide6 pyinstaller
```

## Run

```bash
python main.py
```

## Build

```bash
pyinstaller --onefile --windowed main.py
```

The executable will be created in the `dist` folder.

## Project Structure

```
Website-To-Exe/
│
├── main.py
├── converter.py
├── gui.py
├── resources/
│   ├── icon.ico
│   └── logo.png
├── output/
├── requirements.txt
├── LICENSE
└── README.md
```

## Interface

The application includes:

- Online Website tab
- Local Website tab
- App Name
- Website URL
- Output Folder
- Build EXE button

## License

MIT License

## Author

**Shiny Studios**
