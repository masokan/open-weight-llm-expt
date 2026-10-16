#!/bin/bash
testDir="`dirname $0`"
testDir="`cd $testDir; pwd`"
topDir="`dirname $testDir`"
pythonSrcDir="$topDir/src/main/python"
outputDir="$testDir/output/math"

if [ $# -ge 2 ]
then
  questionsFile="$1"
  shift
  models="$@"
else
  echo "Usage: $0 <questionsFile> model1 [model2 model3 ...]" 1>&2
  echo "The model should support function calls" 1>&2
  exit 1
fi

timeStamp=`date "+%Y%m%d%H%M%S"`

cd "$testDir"
rm -rf pythontestenv
python3 -m venv pythontestenv
. ./pythontestenv/bin/activate
pip3 install -r "$pythonSrcDir/requirements.txt"

python3 tools_calling.py >tools_calling.log

n=1
while read question
do
   for model in $models
   do
      outputFile="$outputDir/q${n}-${model}-function-call-${timeStamp}.md"
      python3 "$pythonSrcDir/llm_function_calling.py"  "$model" "$question" >"$outputFile" 2>&1

   done
   n=`expr $n + 1`
done <"$questionsFile"

# Remove python environment
rm -rf pythontestenv
