def soundex(string: str) -> str:
	""" """
	print(f"{string}")
	to_replace = ["a", "e", "i", "o", "u", "y", "w", "h"]

	output = [string[0]]

	for letter in to_replace:
		string = string.replace(letter, "")

	replace_map = {
		"b" : "1",
		"f" : "1",
		"p" : "1",
		"v" : "1",
		"c" : "2",
		"g" : "2",
		"j" : "2",
		"k" : "2",
		"q" : "2",
		"s" : "2",
		"x" : "2",
		"z" : "2",
		"d" : "3",
		"t" : "3",
		"l" : "4",
		"m" : "5",
		"n" : "5",
		"r" : "6",
	}

	prev = ""
	for letter in string[1:]:
		val = replace_map[letter]
		if val != prev:
			prev = val
			output.append(val)

	while len(output) < 4:
		output.append("0")
	return "".join(output)


def main():
	string = "Jackson"
	print(f"{string} -> {soundex(string)}")

	string = "Jaxen"
	print(f"{string} -> {soundex(string)}")

	string = "Robert"
	print(f"{string} -> {soundex(string)}")

	string = "Rupert"
	print(f"{string} -> {soundex(string)}")

if __name__ == "__main__":
	main()