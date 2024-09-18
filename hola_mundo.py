import os

def main():
  nombre = os.getenv("USERNAME")
  print(f"!hola, {nombre}")
if __name__ == "__main__":
  main()
