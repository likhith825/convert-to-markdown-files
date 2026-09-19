# Convert to Markdown Files

A simple Python desktop utility that converts multiple documents into
Markdown (`.md`) files using Microsoft's `MarkItDown` library.

The application provides a graphical file picker using Tkinter, allowing
you to select one or multiple files and choose where the converted Markdown
files should be saved.

## Features

- Select one or multiple files at once
- Choose an output folder using a graphical interface
- Convert files to Markdown automatically
- Save each converted file with a `.md` extension
- Display conversion progress in the terminal
- Show a completion notification
- Continue processing other files if one file fails

## Supported File Types

The file picker supports:

- PDF (`.pdf`)
- Word Documents (`.docx`)
- Excel Spreadsheets (`.xlsx`)
- PowerPoint Presentations (`.pptx`)
- HTML (`.html`)
- CSV (`.csv`)
- JSON (`.json`)
- XML (`.xml`)
- Text files (`.txt`)

The actual formats that can be successfully converted depend on the
capabilities of the `MarkItDown` library.

---

# Download

There are two ways to download the project.

## Option 1: Download from GitHub

Open the project repository:

https://github.com/likhith825/convert-to-markdown-files

On the GitHub page:

1. Click the green **Code** button.
2. Click **Download ZIP**.
3. Extract the downloaded ZIP file.
4. Open the extracted project folder.

You should see:

```text
convert-to-markdown-files/
│
├── batch.py
└── README.md
