import numpy as np

n = 10
m = 5
v = 0.01
N = 1000

# fundamental function of model, compute probability of move to new square
def Pmove(Nfrom, Nto, Bmap):
  return v * (Nfrom - Nto) * H(Nfrom - Nto)

bearmaxinit=2
# return list of tuples of initial bear locations
def initialize():
  def flatten(l):
    if not isinstance(l, list):
      return [l]
    elif l == []:
      return []
    else:
      return flatten(l[0]) + flatten(l[1:])
  return flatten([[[(i,j) for num in range(np.random.random_integers(bearmaxinit+1)-1)] for j in range(m)] for i in range(n)])

def process(bears, k):
  print k
  print bears

def main():
  # get initial bear locations
  bears = initialize()

  # initialize bear map
  Bmap = np.zeros([n,m], 'i')
  for b in bears:
    Bmap[b] += 1

  R = []
  for k in range(N):
    R.append(0)
    for bi in range(len(bears)):
      Pu = Pd = Pl = Pr = 0
      if bears[bi][0]>0:
        Pu = Pmove(Bmap[bears[bi]], Bmap[ bears[bi][0] - 1, bears[bi][1] ], Bmap)
      if bears[bi][0]<m-1:
        Pd = Pmove(Bmap[bears[bi]], Bmap[ bears[bi][0] + 1, bears[bi][1] ], Bmap)
      if bears[bi][1]>0:
        Pl = Pmove(Bmap[bears[bi]], Bmap[ bears[bi][0], bears[bi][1] - 1 ], Bmap)
      if bears[bi][1]<n-1:
        Pr = Pmove(Bmap[bears[bi]], Bmap[ bears[bi][0], bears[bi][1] + 1 ], Bmap)

      R[k] += Pl + Pr + Pu + Pd

      move = choose([Pu, Pd, Pl, Pr])

      assert Pu > 0 or move != 0
      assert Pd > 0 or move != 1
      assert Pl > 0 or move != 2
      assert Pr > 0 or move != 3

      if move == 0:
        Bmap[bears[bi]] -= 1
        bears[bi] = (bears[bi][0] - 1, bears[bi][1])
        Bmap[bears[bi]] += 1
      elif move == 1:
        Bmap[bears[bi]] -= 1
        bears[bi] = (bears[bi][0] + 1, bears[bi][1])
        Bmap[bears[bi]] += 1
      elif move == 2:
        Bmap[bears[bi]] -= 1
        bears[bi] = (bears[bi][0], bears[bi][1] - 1)
        Bmap[bears[bi]] += 1
      elif move == 3:
        Bmap[bears[bi]] -= 1
        bears[bi] = (bears[bi][0], bears[bi][1] + 1)
        Bmap[bears[bi]] += 1

    process(bears, k)

  return R


# Utility functions below

# Heaviside function
def H(x):
  if x >= 0:
    return 1
  return 0

# pre: reduce(add, Plist) <= 1
def choose(Plist):
  if Plist == []:
    return -1
  choice = np.random.uniform()
  for i in range(len(Plist)):
    if choice < Plist[i]:
      return i
    choice -= Plist[i]
  return -1

def prettyprint(bears):
  for i in range(m):
    pass


if __name__ == "__main__":
  main()
