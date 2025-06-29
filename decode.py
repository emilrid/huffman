import sys
import csv

def decode(source_filename, table_filename, output_filename):
    with open(source_filename, "rb") as f:
        real_length_bytes = f.read(4)
        real_length = int.from_bytes(real_length_bytes, 'big')
        byte_data = f.read()
        text = "".join(f"{byte:08b}" for byte in byte_data)[:real_length]

    with open(table_filename, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        decoded_table = {}
        for row in reader:
            char = eval(row[0])  # safely interpret special characters like '\n' or ' '
            code = row[1]
            decoded_table[str(code)] = char

    decoded_text = ""

    buffer = ''
    for bit in text:
        buffer += bit
        if buffer in decoded_table:
            decoded_text += decoded_table[buffer]
            buffer = ''  # reset buffer for next character

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write("".join(decoded_text))

def main():
    if len(sys.argv) != 4:
        print("Usage: python encode.py input.bin table.csv output.txt")
        sys.exit(1)

    input, table, output_txt = sys.argv[1], sys.argv[2], sys.argv[3]

    decode(input, table, output_txt)
    print("Decoding done")

if __name__ == "__main__":
    main()
