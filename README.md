# Modern Disk Usage (MDU)

## Overview

**Modern Disk Usage (MDU)** is a Python-based utility designed to provide a modern, visually appealing, and user-friendly alternative to the traditional `du` command. MDU leverages the `rich` library to deliver a rich terminal experience, offering features such as progress bars, tables, and panels to display disk usage information in a clear and organized manner. It is a lightweight, easy-to-use tool that supports both directory and file analysis, making it suitable for a wide range of users, from system administrators to developers.

MDU is designed to simplify disk usage analysis by presenting data in a human-readable format, with support for large directories and files. It is highly customizable and can be run on any system with Python 3 installed.

## Features

### Modern Terminal Interface
MDU uses the `rich` library to create a visually appealing terminal interface. The output includes tables, progress bars, and panels, making it easier to interpret disk usage data compared to traditional command-line tools.

### Directory and File Analysis
MDU can analyze both directories and files. It recursively calculates the size of directories and displays the results in a structured table. For files, it directly reports their size.

### Human-Readable Sizes
File and directory sizes are automatically converted into human-readable formats (e.g., KB, MB, GB, TB) for easier interpretation.

### Progress Tracking
When analyzing large directories, MDU displays a progress bar to provide real-time feedback on the calculation process. This is particularly useful for directories with a large number of files and subdirectories.

### Flexible Input
MDU accepts both directory and file paths as command-line arguments. If no arguments are provided, it analyzes the current working directory by default.

### Summary Panel
At the end of the analysis, MDU displays a summary panel that shows the total disk usage across all analyzed paths.

## Installation

MDU is a single Python script, making installation straightforward. Follow these steps to get started:

1. **Download the Script**:
   Use `wget` to download the script directly from the repository:
   ```bash
   wget https://raw.githubusercontent.com/linuxfanboy4/mdu/refs/heads/main/mdu.py
   ```

2. **Run the Script**:
   Execute the script using Python 3:
   ```bash
   python3 mdu.py
   ```

## Usage

### Basic Usage
To analyze the disk usage of the current directory, simply run:
```bash
python3 mdu.py
```

### Analyzing Specific Paths
You can specify one or more directories or files as arguments. For example:
```bash
python3 mdu.py /path/to/directory /path/to/file
```

### Example Output
When you run MDU, you will see an output similar to the following:
```
Directory/File Sizes
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━┓
┃ Path                                                               ┃ Size     ┃ Type    ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━┩
│ /path/to/directory                                                 │ 1.2 GB   │ [bold]Directory
│ /path/to/file.txt                                                  │ 150.5 KB │ [bold]File
└────────────────────────────────────────────────────────────────────┴──────────┴─────────┘
Total Size: 1.35 GB
```

## Requirements

MDU requires the following to run:
- **Python 3.x**: The script is written in Python 3 and requires a compatible version of Python to execute.
- **`rich` Library**: MDU uses the `rich` library for its terminal interface. You can install it using pip:
  ```bash
  pip install rich
  ```

## License

MDU is licensed under the **MIT License**. This means you are free to use, modify, and distribute the software as long as you include the original copyright notice and license terms. The MIT License is permissive and allows for both personal and commercial use.

## Contributing

Contributions to MDU are welcome! If you would like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and ensure the code is well-documented.
4. Submit a pull request with a detailed description of your changes.

Please ensure your contributions align with the project's goals and coding standards.
