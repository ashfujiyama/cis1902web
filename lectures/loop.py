# prints odd integers less than x
def loop(x):
  """
  this is a multi-line comment.
  Can be used for Docstrings
  """
  for i in range(x):
    if i % 2 != 0:
      print(i)

def main():
  x = 11
  loop(x)

if __name__ == "__main__":
  main()