import sys
import csv

class Node:
    def __init__(self, symbol=None, frequency=0):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"{self.symbol}, {self.frequency}"

nodes = []

def recursive_search(node, current_code, codes):
    if node is None:
        return

    if node.symbol is not None:
        codes[node.symbol] = current_code

    recursive_search(node.left, current_code+"0", codes)
    recursive_search(node.right, current_code+"1", codes)


def encode(source_filename, output_filename, table_filename):
    with open(source_filename, "r") as f:
        text = f.read()

    # Create a dictionary with letter as key and frequency as value
    freqs = {}
    for char in text:
        if char in freqs.keys():
            freqs[char] += 1
        else:
            freqs[char] = 1

    for char in freqs:
        nodes.append(Node(char, freqs[char]))

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.frequency)
        left = nodes.pop(0)
        right = nodes.pop(0)
        
        parent = Node(frequency=left.frequency+right.frequency)
        parent.left = left
        parent.right = right

        nodes.append(parent)

    codes = {}
    recursive_search(nodes[0], "", codes)
    data = ""
    for char in text:
        data += str(codes.get(char))

    real_length = len(data)

    padding = 8 - (len(data) % 8)
    if padding != 8:
        data += '0' * padding

    byte_data = bytes(int(data[i:i+8], 2) for i in range(0, len(data), 8))

    with open(output_filename, "wb") as f:
        f.write(real_length.to_bytes(4, 'big'))
        f.write(byte_data)

    with open(table_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for char, code in codes.items():
            display_char = repr(char)
            writer.writerow([display_char, code])

def main():
    if len(sys.argv) != 4:
        print("Usage: python encode.py source.txt output.bin table.csv")
        sys.exit(1)

    source, output, table = sys.argv[1], sys.argv[2], sys.argv[3]

    encode(source, output, table)
    print("Done encoding")

if __name__ == "__main__":
    main()
