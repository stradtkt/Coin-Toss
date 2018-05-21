import random

def toss_coin(times):
  output = ""
  heads = 0
  tails = 0
  for x in range(0, times):
    toss = random.randint(0, 100)
    if toss in range(0, 50):
      heads+=1
      output = "Heads"
    elif toss in range(50,100):
      tails+=1
      output = "Tails"
    print("Attempt #{}: Throwing a coin... It's {}! Got {} head(s) so far and {} tail(s) so far".format(x,output,heads,tails))

toss_coin(10)