import sys

def remove_blank_lines(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    with open(file_path, 'w') as file:
        for line in lines:
            if line.strip():
                file.write(line)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide at least one .txt file as an argument.")
    else:
        for file_path in sys.argv[1:]:
            if file_path.endswith('.txt'):
                remove_blank_lines(file_path)
                print(f"Processed {file_path}")
            else:
                print(f"{file_path} is not a .txt file.")
