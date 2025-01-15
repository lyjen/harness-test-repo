import os

def main():
    name = os.getenv("NAME", "World")
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()
