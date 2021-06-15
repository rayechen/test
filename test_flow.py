import os
import sys
import pytest

def test_flow_func():
  cur_dir = os.getcwd()
  assert cur_dir == "/root/test"
