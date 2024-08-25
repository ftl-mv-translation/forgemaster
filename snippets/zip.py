import sys
import shutil

assert len(sys.argv) == 3
shutil.make_archive(sys.argv[1], 'zip', sys.argv[2])