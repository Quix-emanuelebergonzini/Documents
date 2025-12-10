# -*- coding: utf-8 -*-

import sys
import argparse


def escape_unicode_specials(text):
	result = ''
	for char in text:
		if ord(char) > 127:
			result += '\\u{:04x}'.format(ord(char))
		else:
			result += char
	return result


def split_text(text, max_lines=8, max_line_length=60):
	words = text.split()
	lines = []
	current_line = ''

	for word in words:
		if len(current_line + ' ' + word) <= max_line_length:
			current_line += (' ' if current_line else '') + word
		else:
			lines.append(current_line)
			current_line = word
			if len(lines) == max_lines - 1:
				break
	lines.append(current_line)
	return lines


def main():
	parser = argparse.ArgumentParser(description="Convert special characters to Unicode escape and split into lines.")
	parser.add_argument("text", nargs='?', help="Testo da convertire", default=None)
	parser.add_argument("-m", "--max-lines", type=int, default=8, help="Numero massimo di righe (default: 8)")
	args = parser.parse_args()

	if args.text:
		input_text = args.text
	else:
		input_text = input("Inserisci il testo da convertire: ")

	escaped_text = escape_unicode_specials(input_text)
	lines = split_text(escaped_text, max_lines=args.max_lines)

	print("\nTesto con caratteri speciali in escape Unicode diviso in massimo {} righe:".format(args.max_lines))
	for i, line in enumerate(lines, 1):
		print(f"Riga {i}: {line}")


if __name__ == "__main__":
	main()
