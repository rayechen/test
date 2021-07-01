import os
import sys
import pytest
import ppltest

def test_x():
  i = 1
  assert 1 == i*2/2

def test_ppl():
  result = ppltest.ppl_build_with_jenkins()
  assert result['exec_ok']
  
  result = ppltest.ppltest_x86_with_jenkins()
  assert result['exec_ok']
  assert 0 == result['testcase_result']['failed']
  
  result = ppltest.ppltest_cuda_with_jenkins()
  assert result['exec_ok']
  assert 0 == result['testcase_result']['failed']
  
