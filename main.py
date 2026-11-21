"""Write the judge-text poem to the configured output directory."""

import os

ENTRY_TEXT = """The kettle clicked off. I let it stay quiet.
Hands on the counter, still shaped by the work.
A streetlight turns the rain to slow gold.
Nothing asks me to be useful.
The world moves, and I am allowed to watch.
Rest is not the absence of the task - it is the task, done perfectly."""


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
