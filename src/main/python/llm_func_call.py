from latex2sympy2 import latex2sympy
from ollama import chat, ChatResponse
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
import sys
import time

from elapsed_time import print_elapsed_time

def derivative(f: str) -> str:
  """Find the derivative of a function in one variable x.
  """
  """
  Args:
    f: Function in one variable (x) expressed as a string.  The function should
       contain terms in x which are recognized by sympy

  Returns:
    Derivative of the function as a string
  """

  x = symbols('x')
  expr = parse_expr(f, evaluate=False)
  result = diff(expr, x)
  return(f'{result}')

def antiderivative(f: str) -> str:
  """Find the antiderivative of a function in one variable x.
  """
  """
  Args:
    f: Function in one variable (x) expressed as a string.  The function should
       contain terms in x which are recognized by sympy

  Returns:
    Antiderivative of the function as a string
  """
  x = symbols('x')
  expr = parse_expr(f, evaluate=False)
  var = Integral(expr)
  result = var.doit()
  return(f'{result}')

def factorize(exp_str: str) -> str:
  """Find all the factors of an expression in two variables x and y.
  """
  """
  Args:
    exp_str: Latex representation of an expression in two variables x and y as a
             string

  Returns:
    All the factors of the expression as a string
  """
  x, y = symbols('x y')
  expr = latex2sympy(exp_str)
  result = factor(expr)
  return(f'{result}')

def call_model(model: str, prompt: str):
  before = time.clock_gettime_ns(time.CLOCK_REALTIME)
  messages = [{'role': 'user', 'content': prompt}]
  available_functions = {
    'derivative': derivative,
    'antiderivative': antiderivative,
    'factorize': factorize
  }

  while True:
    response: ChatResponse = chat(model=model, messages=messages,
                                  tools=[derivative, antiderivative, factorize],
                                  think=True)
    messages.append(response.message)
    print("Thinking: ", response.message.thinking)
    print()
    print("Content: ", response.message.content)
    print()
    if response.message.tool_calls:
      for call in response.message.tool_calls:
        if call.function.name in available_functions:
          print(f"Calling {call.function.name} with arguments {call.function.arguments}")
          result = available_functions[call.function.name](**call.function.arguments)
          print(f"Result: {result}")
          print()
          # add the tool result to the messages
          messages.append({'role': 'tool', 'tool_name': call.function.name, 'content': str(result)})
    else:
      # end the loop when there are no more tool calls
      break
  # continue the loop with the updated messages
  after = time.clock_gettime_ns(time.CLOCK_REALTIME)
  print_elapsed_time(before, after)

if __name__ == '__main__' and len(sys.argv) == 3:
  call_model(sys.argv[1], sys.argv[2])
else:
  print(f'Usage: {sys.argv[0]} <model_name> <math_question>')
  sys.exit(1)
