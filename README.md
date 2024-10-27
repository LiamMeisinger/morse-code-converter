Liam Meisinger's Morse Code Converter
Description
This is a command-line program that converts any text into Morse code and vice versa. Inspired by the fun of creating 
something for “secret spy missions,” it encodes and decodes messages for easy practice with encoding concepts in Python.

Motivation
I created this project to strengthen my Python skills and to showcase a simple yet functional project on GitHub. 
It’s a beginner-friendly application demonstrating text encoding and decoding, which can also be a handy tool for 
anyone curious about Morse code.

Features
Encode Text to Morse Code: Converts regular text into Morse code.
Decode Morse Code to Text: Converts Morse code back to readable text.
Handles Unknown Characters: Ignores or skips characters that don’t have a Morse equivalent.

Installation
Clone the repository:
    
Ensure Python is installed. This project was developed with Python 3.x.

Install any dependencies (if applicable). Currently, no external libraries are required.

Usage
To run the program, open a terminal and navigate to the project directory. Then, run:
    python morse_converter.py

Example:

Encoding:
Input: HELLO WORLD
Output: .... . .-.. .-.. --- .-- --- .-. .-.. -..
Decoding:
Input: .... . .-.. .-.. ---
Output: HELLO
Simply enter E to encode or D to decode, following the prompts. To exit, type T.

Future Improvements
Adding a web interface for easier usage.
Adding some sounds for the morse code output.
Adding file input/output for bulk encoding or decoding.
