#!/usr/bin/python3

import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# Get the path of the main repository by moving up one level
main_repo_path = os.path.abspath(os.path.join(current_dir, '..'))

sys.path.append(main_repo_path)

print(main_repo_path)

print(sys.path)