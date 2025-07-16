# Entry point for the FileSystemAnalyser CLI tool.
from src.cli import CLI

if __name__ == '__main__':
    print('Welcome to FileSystemAnalyser')
    CLI().run()