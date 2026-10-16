def print_elapsed_time(before_nano: int, after_nano: int):
  elapsedMilliSec = (after_nano - before_nano)//1000000;
  if (elapsedMilliSec < 1000):
    elapsedMin = 0
    elapsedSec = 0
  else:
    elapsedSec = elapsedMilliSec//1000
    elapsedMilliSec = elapsedMilliSec - elapsedSec*1000
    if (elapsedSec < 60):
      elapsedMin = 0
    else:
      elapsedMin = elapsedSec//60
      elapsedSec = elapsedSec - elapsedMin*60
  print(f'Elapsed time: {elapsedMin} min. {elapsedSec} sec. {elapsedMilliSec} millisec.')
  print()
