from zipfile import ZipFile
from pathlib import Path
from mvlocscript.fstools import glob_posix
from sys import argv
from shutil import rmtree

def write_directories_into_zip(zipf, target_directories):
    writelist = {}
    for pathbase in target_directories:
        pathbase = Path(pathbase)
        writelist.update({
            path: pathbase / path
            for path in glob_posix('**', root_dir=pathbase)
        })
    testlist = {str(key): str(value) for key, value in writelist.items()}
    for arcname, path in writelist.items():
        zipf.write(path, arcname=arcname)

if not argv[1]:
    raise ValueError

path = repr(argv[1])
with ZipFile(path) as zipf:
    zipf.extractall('./tmpfiles')
with ZipFile('./rezipped_' + str(Path(path).name), 'w') as zipf:
    write_directories_into_zip(zipf, ['./tmpfiles'])
rmtree('./tmpfiles')