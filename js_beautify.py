# !/usr/bin/env python3
import sys
import jsbeautifier

def main():
    if len(sys.argv) < 2:
        print("Usage: python beautify_js.py <input_file> [output_file]")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    # Read the input JavaScript file
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            js_code = f.read()
    except Exception as e:
        print(f"Error reading file '{input_file}': {e}")
        sys.exit(1)
    # Set beautifier options (customize as needed)
    opts = jsbeautifier.default_options()
    opts.indent_size = 4  # Adjust indent size (default is 4 spaces)
    # Beautify the JavaScript code
    beautified_code = jsbeautifier.beautify(js_code, opts)
    # Output the beautified code either to a file or stdout
    if output_file:
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(beautified_code)
            print(f"Beautified JavaScript saved to '{output_file}'")
        except Exception as e:
            print(f"Error writing to file '{output_file}': {e}")
            sys.exit(1)
    else:
        print(beautified_code)

if __name__ == "__main__":
    main()