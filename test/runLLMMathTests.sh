#!/bin/bash
testDir="`dirname $0`"
testDir="`cd $testDir; pwd`"
topDir="`dirname $testDir`"
scriptDir="$topDir/src/script"
pythonSrcDir="$topDir/src/main/python"
outputDir="$testDir/output/math"

if [ $# -ge 2 ]
then
  questionsFile="$1"
  shift
  models="$@"
else
  echo "Usage: $0 <questionsFile> model1 [model2 model3 ...]" 1>&2
  exit 1
fi

timeStamp=`date "+%Y%m%d%H%M%S"`

cd "$testDir"
# Create python virtual environment and install required packages
rm -rf llmtestenv
python3 -m venv llmtestenv
. ./llmtestenv/bin/activate
pip3 install -r "$pythonSrcDir/requirements-llm-func-test.txt"

n=1
while read question
do
   for model in $models
   do
      outputFile="$outputDir/q${n}-${model}-${timeStamp}.md"
      $scriptDir/runModel.sh "$model" "$question" </dev/null >"$outputFile" 2>/dev/null
      # For mathstral, convert math output to latex
      case $model in
        mathstral*) sed -e 's/\\\[/$/' -e 's/\\\]/$/' -e 's/\\(/$/' -e 's/\\)/$/' "$outputFile" >$$.md
                    mv $$.md "$outputFile"
                   ;;
        *) ;;
      esac
      # Run llm function calling test; skip it for mathstral model
      case $model in
        mathstral*) ;;
        *)
           outputFile="$outputDir/q${n}-${model}-func-call-${timeStamp}.md"
           python3 "$pythonSrcDir/llm_func_call.py" "$model" "$question" >"$outputFile" 2>&1
           ;;
      esac
   done
   n=`expr $n + 1`
done <"$questionsFile"
rm -rf llmtestenv
