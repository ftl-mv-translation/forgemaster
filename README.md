# Forgemaster needs to be rezipped before committing
Forgemaster is zipped with an "exotic" zip. If you do not use the rezip process, you will see the following symptoms in translated packages
- Duplicate files, one being original English and one being translated.
- Empty files that are supposed to be directories.

This is because writelist(dict of paths for all package components) contains backslashes in string (should be only forward slash) or directory (should be only file).

## Apply rezip
Once you have downloaded the original forgemaster, run rezip.py with the path of forgemaster as argument.

`python rezip.py <forgemaster path>`.

Then you can commit to forgemaster-en and mvloc will handle it correctly.