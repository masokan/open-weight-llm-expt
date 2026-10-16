from sympy import *
from sympy.printing.latex import print_latex
import time

from elapsed_time import print_elapsed_time

def print_result(result):
  print(f'Result: {result}')
  print('Result in latex: ', end='')
  print_latex(result)

def test_derivative():
  print('Testing differentiation...')
  before = time.clock_gettime_ns(time.CLOCK_REALTIME)
  x = symbols('x')
  result = diff(sqrt(log(x)) + sqrt(sin(x)), x)
  print_result(result)
  after = time.clock_gettime_ns(time.CLOCK_REALTIME)
  print_elapsed_time(before, after)

def test_antiderivative_simple():
  print('Computing indefinite integral...')
  before = time.clock_gettime_ns(time.CLOCK_REALTIME)
  x = symbols('x')
  var = Integral((cos(x)/sqrt(sin(x)) + 1/(x*sqrt(log(x))))/2)
  result = var.doit()
  print_result(result)
  after = time.clock_gettime_ns(time.CLOCK_REALTIME)
  print_elapsed_time(before, after)

def test_antiderivative_complicated():
  print('Computing indefinite integral that does not exist...')
  before = time.clock_gettime_ns(time.CLOCK_REALTIME)
  x = symbols('x')
  var = Integral(sqrt(sin(x)) + sqrt(log(x)))
  result = var.doit()
  if (result == var):
    print(f'Indefinite {var} does not exist!')
  else:
    print_result(result)
  after = time.clock_gettime_ns(time.CLOCK_REALTIME)
  print_elapsed_time(before, after)

def test_diff_eq():
  print('Solving differential equation...')
  before = time.clock_gettime_ns(time.CLOCK_REALTIME)
  x = symbols('x')
  f = symbols('f', cls=Function)
  eq = Eq(x*x*f(x).diff(x, x) + x*f(x).diff(x), 49*f(x))
  result = dsolve(eq, f(x))
  print_result(result)
  after = time.clock_gettime_ns(time.CLOCK_REALTIME)
  print_elapsed_time(before, after)

def test_factorization():
  print('Factorizing algebraic expression...')
  before = time.clock_gettime_ns(time.CLOCK_REALTIME)
  x, y = symbols('x y')
  result = factor(x**99 + y**99)
  print_result(result)
  after = time.clock_gettime_ns(time.CLOCK_REALTIME)
  print_elapsed_time(before, after)

test_derivative()
test_antiderivative_simple()
test_antiderivative_complicated()
test_diff_eq()
test_factorization()
