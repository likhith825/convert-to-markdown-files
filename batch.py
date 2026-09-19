from pathlib import Path
import sys
import tkinter as tk
from tkinter import filedialog, messagebox
from markitdown import MarkItDown


def select_and_convert():
    # Hide the main Tkinter root window
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    # 1. Select one or multiple files dynamically
    file_paths = filedialog.askopenfilenames(
        title="Select one or more files to convert",
        filetypes=[
            (
                "Supported Documents",
                "*.pdf *.docx *.xlsx *.pptx *.html *.csv *.json *.xml *.txt",
            ),
            ("PDF Files", "*.pdf"),
            ("Word Documents", "*.docx"),
            ("Excel Spreadsheets", "*.xlsx"),
            ("PowerPoint Presentations", "*.pptx"),
            ("All Files", "*.*"),
        ],
    )

    if not file_paths:
        print("No files selected. Exiting.")
        return

    # 2. Select the destination directory
    output_dir = filedialog.askdirectory(
        title="Select output folder for Markdown files"
    )

    if not output_dir:
        print("No output folder selected. Exiting.")
        return

    dest_folder = Path(output_dir)
    dest_folder.mkdir(parents=True, exist_ok=True)

    # Initialize MarkItDown engine
    md = MarkItDown()

    total_files = len(file_paths)
    successful = 0

    print(f"\nConverting {total_files} file(s) into: {dest_folder}\n" + "-" * 50)

    for idx, path_str in enumerate(file_paths, 1):
        input_file = Path(path_str)
        output_file = dest_folder / f"{input_file.stem}.md"

        try:
            print(f"[{idx}/{total_files}] Processing: {input_file.name}...")
            result = md.convert(str(input_file))

            # Write the converted markdown text
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(result.text_content)

            successful += 1
            print(f"       -> Saved: {output_file.name}")
        except Exception as e:
            print(f"       -> Error converting {input_file.name}: {e}")

    # Summary notification
    print("-" * 50)
    print(
        f"Completed: {successful}/{total_files} files successfully converted."
    )
    messagebox.showinfo(
        "Conversion Complete",
        f"Converted {successful} of {total_files} file(s).\nSaved to:\n{dest_folder}",
    )


if __name__ == "__main__":
    select_and_convert()