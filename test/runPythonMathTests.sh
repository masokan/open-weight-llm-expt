#!/bin/bash
testDir="`dirname $0`"
testDir="`cd $testDir; pwd`"
topDir="`dirname $testDir`"
pythonSrcDir="$topDir/src/main/python"
outputDir="$testDir/output/math"

cd "$testDir"
# Create python virtual environment and install required packages
rm -rf pythontestenv
python3 -m venv pythontestenv
. ./pythontestenv/bin/activate
pip3 install -r "$pythonSrcDir/requirements-sym-math.txt"

python3 "$pythonSrcDir/symbolic_math.py" >"$outputDir/python-output.txt"
rm -rf pythontestenv
