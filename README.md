# Huffman coding Python implementation

This project implements Huffman encoding and decoding in Python. It allows you to compress and decompress text files using Huffman coding.

### Example:
```bash
python3 encode.py example.txt output/output.bin output/table.csv
python3 decode.py output/output.bin output/table.csv decoded.txt
```
or you can try:
```bash
python3 encode.py README.md output/output.bin output/table.csv
python3 decode.py output/output.bin output/table.csv decoded.md
```

### Preferred usage:
```bash
python3 encode.py source.txt output/output.bin output/table.csv
python3 decode.py output/output.bin output/table.csv decoded.txt
```
