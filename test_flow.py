import os
import sys

def test_flow_func():
  cur_dir = os.getcwd()
  assert(cur_dir == "/root/test")
