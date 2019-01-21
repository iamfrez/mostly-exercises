with open("max-difference.py") as fp:        # Change x.py
  for i, line in enumerate(fp):
    if "\xe2" in line:
      print i, repr(line)
