import os
import sys
import pytest
import ppltest

def test_x():
  i = 1
  assert 1 == i*2/2

def test_build_ppl(github_sha, github_run_id, github_run_number):
  print(github_sha)
  print(github_run_id)
  print(github_run_number)
  print('sleeping 50s...'
  import time
  time.sleep(50)
  exec_ok = ppltest.ppl_build_with_jenkins()
  assert exec_ok
  
def test_ppl_x86():
  result = ppltest.ppltest_x86_with_jenkins()
  assert result['exec_ok']
  assert 'SUCCESS' == result['testcases_result']['result_status']
  assert 0 == result['testcases_result']['failed']
  
def test_ppl_cuda():
  result = ppltest.ppltest_cuda_with_jenkins()
  assert result['exec_ok']
  assert 'SUCCESS' == result['testcases_result']['result_status']
  assert 0 == result['testcases_result']['failed']
  
