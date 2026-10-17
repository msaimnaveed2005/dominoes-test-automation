"""Run the dominoes command-line game with ``python -m dominoes``."""

from pathlib import Path
import runpy
import sys


def main():
    script = Path(__file__).resolve().parent.parent / 'bin' / 'dominoes'
    sys.argv[0] = str(script)
    runpy.run_path(str(script), run_name='__main__')


if __name__ == '__main__':
    main()
