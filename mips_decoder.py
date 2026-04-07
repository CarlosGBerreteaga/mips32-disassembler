import sys
from pathlib import Path


# Let this launcher import modules from the local code folder.
PROJECT_DIR = Path(__file__).resolve().parent
CODE_DIR = PROJECT_DIR / "code"
sys.path.insert(0, str(CODE_DIR))

from main import main


if __name__ == "__main__":
    main()
