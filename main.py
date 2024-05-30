import re
class MarkdownParser:
    def __init__(self, markdown_text):
        self.markdown_text = markdown_text
        self.html_lines = []
    def parse_headers(self, line):
        match = re.match(r'^(#{1,6})\s+(.*)', line)
        if match:
            header_level = len(match.group(1))
            content = match.group(2)
            return f'<h{header_level}>{content}</h{header_level}>'
        return None
    def parse_paragraph(self, line):
        if re.search(r'<[^>]+>', line):
            return line
        return f'<p>{line}</p>'
    def parse_bold(self, text):
        return re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    def parse_italic(self, text):
        return re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    def parse_links(self, text):
        return re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)
    def parse_list_items(self):
        html = []
        in_list = False
        for line in self.html_lines:
            if re.match(r'^\s*-\s+(.*)', line):
                if not in_list:
                    html.append('<ul>')
                    in_list = True
                html.append(f'<li>{line.strip()[2:]}</li>')
            else:
                if in_list:
                    html.append('</ul>')
                    in_list = False
                html.append(self.parse_paragraph(line))
        if in_list:
            html.append('</ul>')
        self.html_lines = html
    def convert_to_html(self):
        lines = self.markdown_text.split('\n')

        for line in lines:
            header_html = self.parse_headers(line)
            if header_html:
                self.html_lines.append(header_html)
            else:
                line = self.parse_bold(line)
                line = self.parse_italic(line)
                line = self.parse_links(line)
                self.html_lines.append(line)
        self.parse_list_items()
        return '\n'.join(self.html_lines)
class MarkdownConverter:
    def __init__(self, input_file, output_file, title="Markdown to HTML"):
        self.input_file = input_file
        self.output_file = output_file
        self.title = title
    def read_markdown_file(self):
        with open(self.input_file, 'r', encoding='utf-8') as f:
            return f.read()
    def write_html_file(self, html_content):
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
    def convert(self):
        markdown_text = self.read_markdown_file()
        parser = MarkdownParser(markdown_text)
        body_content = parser.convert_to_html()
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }}
        ul {{
            list-style-type: disc;
            margin: 0;
            padding: 0;
            padding-left: 20px;
        }}
        li {{
            margin-bottom: 10px;
        }}
    </style>
</head>
<body>
{body_content}
</body>
</html>"""

        self.write_html_file(html_content)
        print(f"Conversion complete. HTML written to {self.output_file}")
converter = MarkdownConverter('example.md', 'example.html')
converter.convert()
