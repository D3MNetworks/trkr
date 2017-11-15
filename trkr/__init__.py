import sys

from trkr.run import main as run
from trkr.setup import main as setup

def main():
  if len(sys.argv) > 1:
    method = globals().get(sys.argv[1])
    if not method:
      print('Unsupported command. Available commands are `setup` and `run`')
    else:
      method()
  else:
    run()
