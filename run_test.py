import os
import argparse

parser = argparse.ArgumentParser(description='manual to this script')
parser.add_argument('--github_run_id', type=str, default = None)
parser.add_argument('--github_run_number', type=str, default=None)
parser.add_argument('--sha', type=str, default=None)
args = parser.parse_args()
print(args.github_run_id, type(args.github_run_id))
print(args.github_run_number, type(args.github_run_number))
print(args.sha, type(args.sha))

