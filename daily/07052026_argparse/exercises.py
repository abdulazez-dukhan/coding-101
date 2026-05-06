import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--phase")

args = parser.parse_args(args=["--phase", "chunk"])

print(args)
print("phase =", args.phase)
