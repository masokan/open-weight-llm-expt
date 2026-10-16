This directory contains files with answers for the math questions from
different LLMs. Following are the questions and the summary of the
findings:

- Q1: What is the derivative of the function \$\$f(x) =
  \\sqrt{\\sin(x)} + \\sqrt{\\ln(x)}\$\$ ?

  This is just a warm-up question to check the capabilities of the LLMs.
  All LLMs answered this correctly. `mathstral` took the least time and
  `qwen` the most time to answer. When `qwen` was given the help of an
  external function call, it cut down the time significantly. On
  multiple runs, `gemma` and `mathstral` answered consistently. In one
  run `qwen` answered correctly but in another run, it tried to verify
  the result numerically, got confused, and gave an absurd final answer.
  With function calls though `qwen` arrived at the answer quickly and
  correctly. `gemma` did not even attempt to call the function even when
  one was offered.

- Q2: What is the antiderivative of the function \$\$f(x) = \\frac{1}{2}
  \\left\[ \\frac{\\cos(x)}{\\sqrt{\\sin(x)}} +
  \\frac{1}{x\\sqrt{\\ln(x)}} \\right\]\$\$ ?

  Again, `gemma` and `mathstral` consistently came up with the correct
  answer. `qwen` took varying amount of time to answer. It did not
  attempt use the external function even when offered one.

- Q3: What is the antiderivative of the function \$\$f(x) =
  \\sqrt{\\sin(x)} + \\sqrt{\\ln(x)}\$\$ ?

  In this case, the expected answer is that the antiderivative does not
  exist. `gemma` rightly suggested that only numerical integration is
  possible. When supplied with an external function, it verified that
  antiderivative does not exist. `mathstral` came up with different
  incorrect answers on repeated runs. `qwen` spent a lot time to
  conclude that antiderivative does not exist. When external function
  was offered, it passed the argument incorrectly causing a crash.

- Q4: Solve the differential equation: \$\$x\^2 \\frac{d\^2y}{dx\^2} + x
  \\frac{dy}{dx} = 49y\$\$

  In this case, an external function was not offered since it was
  difficult to define the function interface to pass the differential
  equation. `gemma` and `qwen` consistently came up with the correct
  answer. `mathstral` came up with incorrect answers multiple times.

- Q5:Find all factors of the expression \$\$x\^{99} + y\^{99}\$\$

  This is a difficult question to answer by the LLMs. The answers were
  either incomplete or incorrect for all the LLMs. When an external
  python function that uses `sympy` was provided, `gemma` and `qwen`
  resorted to invoke it to come up with the answer.

- Q6: Prove that when two numbers of the form \$\$a\^2 + 3b\^2\$\$ are
  multiplied, the result is of the same form.

  This question was lifted from a math competition exam. Amazingly, all
  the LLMs came up with the correct proof. `gemma` and `qwen` even
  identified a generic form of the fact as [Brahmagupta--Fibonacci
  identity.](https://en.wikipedia.org/wiki/Brahmagupta%E2%80%93Fibonacci_identity)
