import sys
import os

def process_file(input_file_path):
    """
    Reads a string from a file, repeats it three times,
    and saves the output to a new file.
    """
    output_dir = "Z_output_files"
    os.makedirs(output_dir, exist_ok=True)

    try:
        with open(input_file_path, 'r') as f:
            content = f.read().strip()
    except FileNotFoundError:
        print(f"Error: The input file {input_file_path} was not found.")
        sys.exit(1)

    output_string = (content + ' ') * 3
    output_file_name = f"processed_{os.path.basename(input_file_path)}"
    output_file_path = os.path.join(output_dir, output_file_name)

    with open(output_file_path, 'w') as f:
        f.write(output_string)

    print(f"File processed successfully. Output saved to {output_file_path}")
    return output_file_path

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python simple_processor.py <input_file_path>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    process_file(input_path)

