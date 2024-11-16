import re

def clean_html_file(input_file: str, output_file: str = 'cleaned.txt'):
    with open(input_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    clean_text = re.sub(r'<[^>]+>', '', html_content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(clean_text)

clean_html_file('draft.html')