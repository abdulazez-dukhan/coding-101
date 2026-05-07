import argparse

# YOUR FINAL PIPELINE HERE
parser = argparse.ArgumentParser()

parser.add_argument("--book", type=int)
parser.add_argument("--phase", choices=["ingestion", "chunk"])
parser.add_argument("--force", action="store_true")

args = parser.parse_args() # args=["--force", "--phase", "ingestion", "--book", "123"]

print(args.book)