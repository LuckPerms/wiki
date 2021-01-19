import sys
import os
import mistune
import json

# create a markdown parser instance
parser = mistune.create_markdown(
	escape=False,
	renderer='ast',
	plugins=['table'],
)


class Section:
	"""Represents a named section within a file"""

	def __init__(self, name):
		self.name = name
		self.lines = []

	def append(self, line):
		"""Appends a line to this section"""
		self.lines.append(line)

	def _export_lines(self):
		"""Exports the lines in this section to an array"""
		out = []
		for line in self.lines:
			for sub_line in line.split('\n'):
				if len(sub_line) != 0:
					out.append(sub_line)
		return out

	def submit(self, arr):
		"""Appends a dict representing this section to the given array, if it is non-empty"""
		lines = self._export_lines()
		if len(lines) != 0:
			arr.append({'name': self.name, 'lines': lines})


def ast_to_text(nodes):
	"""Converts an array of markdown ast nodes to a string.

	:param nodes: an array of ast nodes
	:return: a string
	"""
	return ''.join(_ast_to_text(nodes))


def _ast_to_text(nodes, acc=None, newline=False):
	"""Converts an array of markdown ast nodes to an array of text.
	This text can then be joined together to form a single string.

	:param nodes: an array of AST nodes
	:param acc: the accumulator array
	:param newline: if a newline should be appended to the output after each node in the input is processed
	:return: an array of strings
	"""
	if acc is None:
		acc = []

	for child in nodes:
		child_type = child['type']

		if 'text' in child and child_type not in ('inline_html', 'block_code', 'block_html'):
			acc.append(child['text'])

		if child_type == 'newline':
			acc.append('\n')

		if 'children' in child:
			# if the type is any one of the following, then indicate that newlines
			# should be inserted after each child
			nl = child_type in ('list', 'table_row', 'table_head')
			# call recursively
			_ast_to_text(child['children'], acc, nl)

		if newline:
			acc.append('\n')

	return acc


def get_tag(used_tags, tag):
	if tag in used_tags:
		i = 2
		while (tag + '-' + str(i)) in used_tags:
			i += 1
		tag = tag + '-' + str(i)
	used_tags.add(tag)
	return tag


def parse(content):
	"""Parses a markdown file to plain text separated into sections.

	:param content: the input string
	:return: an array of parsed sections containing lines of plain text
	"""
	nodes = parser(content)

	sections = []
	used_tags = set()
	current_section = Section('')
	
	for node in nodes:
		if node['type'] == 'heading':
			# if the node is a heading - push the current section, then replace current_section
			current_section.submit(sections)

			title = ast_to_text(node['children'])
			current_section = Section(get_tag(used_tags, title))
		else:
			# otherwise, just append to the current section
			current_section.append(ast_to_text([node]))

	current_section.submit(sections)
	return sections


def parse_all(directory):
	"""Parses all markdown files in the given directory.

	:param directory: the directory to search
	:return: a dict of the files searched mapped to the result of parsing them
	"""
	files = sorted([file for file in os.listdir(directory) if file.endswith(".md") and not file == "_Sidebar.md"])

	index = {}
	for file in files:
		with open(directory + file) as f:
			index[file[:-3]] = parse(f.read())
	return index


def get_id(file, section):
	if len(section) == 0:
		return file
	else:
		return file + '#' + section


def export(directory):
	"""Exports the result of parsing all markdown files in the given directory.

	:param directory: the directory to search
	:return: an array of results to be imported into lunr
	"""
	parsed = parse_all(directory)

	out = {}
	for filename, sections in parsed.items():
		for section in sections:
			out[get_id(filename, section['name'])] = '\n'.join(section['lines'])
	return out


if __name__ == '__main__':
	d = '.'
	if len(sys.argv) >= 2:
		d = sys.argv[1]

	print(json.dumps(export(d), indent=2))
