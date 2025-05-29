import sys
import os

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

import main

import constants

main.FILE_NAME = os.path.dirname(sys.argv[0]) + f"/{constants.FILE_NAME}"

main.main()