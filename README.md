This repository contains files and scripts needed to run tests on some
open-weight LLMs. You can run the tests yourself on your favorite Linux
system by following these steps:

- Install python 3 on your system by following the Linux distribution
  specific instructions
  [here.](https://linuxconfig.org/python-introduction-and-installation-guide)

- Install `ollama` by following the instructions available
  [here.](https://docs.ollama.com/linux)

- Once `ollama` is installed, type the following commands in a shell
  window to install the required open-weight LLMs. Make sure that your
  system has sufficient disk space and has at least 32 GB of main
  memory.

  `ollama pull mathstral:7b`

  `ollama pull medgemma:4b-it-bf16`

  `ollama pull gemma4:12b`

  `ollama pull qwen3:14b`

- Download this repository from github by typing the following command
  from a shell window:

      git clone https://github.com/masokan/open-weight-llm-expt.git

  It is assumed that you have `git` installed on the system.

- Assuming that you cloned the repository in the current directory,
  following are some scripts and python source files in the repository.

  **`open-weight-llm-expt/src/script/runModel.sh:`** This is a wrapper
  script for `ollama` to run a locally installed model given the prompt
  and other arguments. The prompt can be specified as a command line
  argument or passed in standard input. Other arguments can be file
  names if relevant. For example for `medgemma` you may want to pass an
  image file name to the LLM. This script also prints the elapsed time
  for the LLM to come up with the response. The output from the model
  can be redirected to a file.

  **`open-weight-llm-expt/test/MathQuestions.txt:`** Each line of this
  file contains a math question used for testing the LLMs.

  **`open-weight-llm-expt/src/main/python/symbolic_math.py:`** A python
  program that invokes `sympy` functions to solve math problems. Note
  that `sympy` can do only symbolic computations. It cannot prove any
  theorem.

  **`open-weight-llm-expt/src/main/python/llm_func_call.py:`** A python
  program that exposes some math functions to an LLM which is invoked
  programatically using `ollama` python library.

  **`open-weight-llm-expt/test/runPythonMathTests.sh:`** This script
  creates the appropriate python environment and runs the math tests
  using `symbolic_math.py.` The output of the test is saved in the file
  `open-weight-llm-expt/test/output/math/python-output.txt.`

  **`open-weight-llm-expt/test/runLLMMathTests.sh:`** This script runs
  the math tests by invoking `runModel.sh` repeatedly for each question
  in `MathQuestions.txt.` The output from the LLM is captured in a
  separate file for each question. The output file name is derived from
  question number, model name, and timestamp. Output files created from
  different runs are populated in the directory
  `open-weight-llm-expt/test/output/math.`

  **`open-weight-llm-expt/test/runLLMFunctionCallTests.sh:`** This
  script is very similar to `runLLMMathTests.sh` except that it creates
  the appropriate python environment and runs the math tests by invoking
  `llm_func_call.py` repeatedly for each question in
  `MathQuestions.txt.`

- The questions for `medgemma` were picked from
  [here.](https://www.missouriacp.org/uploads/6/9/1/3/69139257/acpmo_mksap_mcqs_sept2023_pk_ir_final.pdf)
  You can copy each question to a file (*e.g.,* `q1.txt`) and save any
  image associated with the question to another file (*e.g.,* `q1.jpg.`)
  You can then invoke `runModel.sh` script as:

      open-weight-llm-expt/src/script/runModel.sh medgemma:4b-it-bf16 q1.jpg < q1.txt > a1.txt

  The file `a1.txt` contains the response from `medgemma.` Outputs
  generated on my Laptop from running the model for all the questions
  are available in the directory
  `open-weight-llm-expt/test/output/medical.`

The code is licensed under [Creative Commons Attribution-ShareAlike 4.0
International License.](https://creativecommons.org/licenses/by-sa/4.0))
