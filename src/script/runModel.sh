#!/bin/bash
printTimeTaken() {
  startTime="$1"
  endTime="$2"
  startSec=`date -d "$startTime" "+%s"`
  endSec=`date -d "$endTime" "+%s"`

  bc <<EOT
  diff = $endSec - $startSec
  minutes = diff / 60
  secs = minutes * 60
  secs = diff - secs
  print "Elapsed time: ", minutes, " min. ", secs, " sec.\n"
EOT
}

if [ $# -ge 1 ]
then
    model="$1"
    shift
else
    {
      echo "Usage: $0 <model name> [<other arguments>]"
      echo "where <model name> can be one of:"
      ollama ls|sed -e '1d'|awk '{print $1}'
      echo "The prompt to the model can be one of the other arguments or"
      echo "it can be passed in stdin"
    } 1>&2
    exit 1
fi
echo "Model: $model"
echo
echo "Prompt: $@"
echo
startTime="`date`"

# Work around a bug in ollama (https://github.com/ollama/ollama/pull/17112)
if [ -t 1 ] # Output goes to terminal
then
  ollama run "$model" "$@"
else # Output goes to a file; remove unnecessary text
  ollama run "$model" "$@" |
     sed -e 's/\([ [:punct:]]\)[^ ]*[\x1B][^ ]*$/\1/' -e 's/ $//'
fi
endTime="`date`"
printTimeTaken "$startTime" "$endTime"
