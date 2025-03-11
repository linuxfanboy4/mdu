import os
import sys
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.panel import Panel
from rich.columns import Columns
from rich.markdown import Markdown
from rich.align import Align
from rich.syntax import Syntax

console = Console()

def get_size(path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            filepath = os.path.join(dirpath, filename)
            total_size += os.path.getsize(filepath)
    return total_size

def convert_size(size_bytes):
    for x in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024.0:
            return "%3.1f %s" % (size_bytes, x)
        size_bytes /= 1024.0
    return "%3.1f %s" % (size_bytes, 'PB')

def show_directory_size(paths):
    total_size = 0
    table = Table(title="Directory/File Sizes", box="ROUND", show_header=True, header_style="bold white on blue", width=60)
    table.add_column("Path", justify="left", style="cyan", no_wrap=True)
    table.add_column("Size", justify="right", style="magenta")
    table.add_column("Type", justify="center", style="green")

    with Progress() as progress:
        task = progress.add_task("[cyan]Calculating sizes...", total=len(paths))
        
        for path in paths:
            progress.update(task, advance=1)
            if os.path.isdir(path):
                size = get_size(path)
                total_size += size
                table.add_row(path, convert_size(size), "[bold]Directory")
            elif os.path.isfile(path):
                size = os.path.getsize(path)
                total_size += size
                table.add_row(path, convert_size(size), "[bold]File")

    console.print(table)
    return total_size

def show_summary(total_size):
    console.print(Panel(f"Total Size: {convert_size(total_size)}", style="bold green"))

def main():
    if len(sys.argv) == 1:
        paths = [f for f in os.listdir() if os.path.isdir(f) or os.path.isfile(f)]
        total_size = show_directory_size(paths)
    else:
        paths = sys.argv[1:]
        total_size = show_directory_size(paths)

    show_summary(total_size)

if __name__ == "__main__":
    main()
