import os
import argparse

def print_params():
  parser = argparse.ArgumentParser(description='manual to this script')
  parser.add_argument('--github_run_id', type=str, default = None)
  parser.add_argument('--github_run_number', type=str, default=None)
  parser.add_argument('--sha', type=str, default=None)
  args = parser.parse_args()
  print(args.github_run_id, type(args.github_run_id))
  print(args.github_run_number, type(args.github_run_number))
  print(args.sha, type(args.sha))

# print('sleeping 50s...')
# import time
# time.sleep(50)
# import sys
# sys.exit(-1)

if __name__ == "__main__":
  print_params()
  return -1
