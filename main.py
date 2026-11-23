"""Entry point for the grader. Writes a specific promotional sentence to the output file."""
# Entry validated: output is 1-240 chars, one line, deterministic.

import os
from pathlib import Path

LINE = "Why not let a friendly AI agent turn that app idea you have been whispering about for years into a real, working piece of software on make.fun while you just sit back and watch, with zero downloads and no cost to try?"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = Path(output_dir) / "entry.txt"
    
    content = LINE
    
    # Validate content according to rules
    if not (1 <= len(content) <= 240 and content.strip() and "\n" not in content):
        raise ValueError("Content validation failed")
        
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(content, encoding="utf-8")
    
    print(str(out_path))
    print(len(content))


if __name__ == "__main__":
    main()
