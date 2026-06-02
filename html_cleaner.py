from bs4 import BeautifulSoup

# 1. Get the file path from the user
file_name = str(input('Enter The HTML File Name oR Path:- '))

# 2. Read the original raw HTML
with open(file_name, 'r', encoding='utf-8') as file:
    raw_html = file.read()

# 3. Parse and completely wipe the attribute dictionary of every single tag element
soup = BeautifulSoup(raw_html, 'html.parser')
for tag in soup.find_all(True):
    tag.attrs = {}

# 4. Convert the refined DOM back into a string
refined_html = str(soup)

# 5. Overwrite the original file with the clean HTML
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(refined_html)

print(f"\nSuccess! 100% of attributes completely removed. Saved directly to: {file_name}")
