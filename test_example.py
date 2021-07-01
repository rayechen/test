import os
import sys
import pytest
import ppltest

def test_x():
  i = 1
  assert 1 == i*2/2

def test_build_ppl():
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
  
