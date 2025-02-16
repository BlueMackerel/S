import sys
from typing import Dict, List, Optional
from pathlib import Path

class DustCompiler:
    """A compiler that converts text to numeric bytecode and vice versa."""
    
    def __init__(self):
        # Character to number mapping
        self.char_to_num: Dict[str, int] = {
            # Uppercase letters
            **{chr(i): i-64 for i in range(65, 91)},  # A-Z: 1-26
            # Lowercase letters
            **{chr(i): i-96+26 for i in range(97, 123)},  # a-z: 27-52
            # Numbers
            **{str(i): i+52 for i in range(1, 10)},  # 1-9: 53-61
            "0": 0,
            # Special characters
            **{
                "!": -1, "@": -2, "#": -3, "$": -4, "%": -5,
                "^": -6, "&": -7, "*": -8, "(": -9, ")": -10,
                "-": -11, "_": -12, "+": -13, "=": -14, "`": -15,
                "~": -16, "[": -17, "]": -18, "{": -19, "}": -20,
                "\\": -21, ";": -22, ":": -23, "'": -24, '"': -25,
                "<": -26, ">": -27, "/": -28, "?": -29,
                " ": -100, ",": -101, ".": -102,
                "\n": "\n"
            }
        }
        # Create reverse mapping
        self.num_to_char: Dict[str, str] = {
            str(v): k for k, v in self.char_to_num.items() if v != "\n"
        }
        self.num_to_char["\n"] = "\n"

    def to_bytecode(self, text: str) -> str:
        """Convert text to bytecode representation."""
        result: List[str] = []
        for char in text:
            if char in self.char_to_num:
                value = self.char_to_num[char]
                if value != "\n":
                    result.extend([str(value), " "])
                else:
                    result.append(value)
        return "".join(result).rstrip()

    def from_bytecode(self, bytecode: str) -> str:
        """Convert bytecode back to text."""
        result: List[str] = []
        for num in bytecode.split():
            if num in self.num_to_char:
                result.append(self.num_to_char[num])
            else:
                result.append(" ")
        return "".join(result)

    def compile_file(self, input_path: Path) -> Optional[str]:
        """Compile a source file to bytecode."""
        try:
            if not input_path.exists():
                raise FileNotFoundError(f"File not found: {input_path}")

            # Read source file
            with open(input_path, "r", encoding="utf-8") as f:
                source = f.read()

            # Create output file with .sasm extension
            output_path = input_path.with_suffix(".sasm")
            
            # Convert and write each line
            with open(output_path, "w", encoding="utf-8") as f:
                for line in source.splitlines():
                    bytecode = self.to_bytecode(line)
                    f.write(f"{bytecode}\n")

            return str(output_path)

        except Exception as e:
            print(f"Error compiling {input_path}: {str(e)}")
            return None

def main():
    """Main entry point for the Dust compiler."""
    # Check command line arguments
    if len(sys.argv) != 2:
        print("Usage: python dust.py <input_file>")
        sys.exit(1)

    # Initialize compiler
    compiler = DustCompiler()
    
    # Get input file path
    input_path = Path(sys.argv[1])
    
    # Compile the file
    output_path = compiler.compile_file(input_path)
    
    if output_path:
        print(f"Successfully compiled to {output_path}")
    else:
        print("Compilation failed")
        sys.exit(1)

if __name__ == "__main__":
    main()