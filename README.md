# Modern Disk Usage (MDU)

## Overview

**Modern Disk Usage (MDU)** is a modern, Python-based alternative to the traditional `du` command. It provides a visually appealing and user-friendly way to analyze disk usage for directories and files. Built with the `rich` library, MDU offers a rich terminal experience with progress bars, tables, and panels to display disk usage information in a clear and organized manner.

MDU is designed to be lightweight, easy to use, and highly customizable. It supports both directory and file analysis, and it can be run on any system with Python 3 installed.

## Features

- **Modern Terminal Interface**: Utilizes the `rich` library to provide a visually appealing output with tables, progress bars, and panels.
- **Directory and File Analysis**: Calculates the size of directories and files, displaying the results in a structured table.
- **Human-Readable Sizes**: Converts file sizes into human-readable formats (e.g., KB, MB, GB, TB).
- **Progress Tracking**: Displays a progress bar while calculating sizes for large directories.
- **Flexible Input**: Accepts both directory and file paths as command-line arguments. If no arguments are provided, it analyzes the current directory.
- **Summary Panel**: Displays a summary of the total disk usage at the end of the analysis.

---

## Installation

To install and use MDU, follow these steps:

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
You can specify one or more directories or files as arguments:
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

- Python 3.x
- `rich` library (install via `pip install rich`)

## License

MDU is licensed under the **MIT License**. You are free to use, modify, and distribute this software as per the terms of the license.

## Contributing

Contributions are welcome! If you'd like to contribute to MDU, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

## Support

For issues, feature requests, or questions, please open an issue on the [GitHub repository](https://github.com/linuxfanboy4/mdu).

## Author

MDU is developed and maintained by [linuxfanboy4](https://github.com/linuxfanboy4).
