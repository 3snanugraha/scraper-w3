from urllib.request import urlopen as get
from bs4 import BeautifulSoup
import os
import re

b_url = 'https://www.w3schools.com/html/'
n_url = 'html_intro.asp'
s_url = 'html_exam.asp'

page_count = 0

if not os.path.exists('data'):
    os.makedirs('data')

def clean_text(text):
    # Remove multiple newlines and spaces
    text = re.sub(r'\n\s*\n', '\n\n', text.strip())
    return text

def html_to_markdown(element):
    md_content = []
    
    for tag in element.find_all(['h1', 'h2', 'h3', 'p', 'ul', 'li', 'code', 'div']):
        if tag.name == 'h1':
            md_content.append(f'# {tag.text.strip()}\n')
        elif tag.name == 'h2':
            md_content.append(f'\n## {tag.text.strip()}\n')
        elif tag.name == 'h3':
            md_content.append(f'\n### {tag.text.strip()}\n')
        elif tag.name == 'p':
            md_content.append(f'\n{tag.text.strip()}\n')
        elif tag.name == 'ul':
            md_content.append('\n')
            for li in tag.find_all('li'):
                md_content.append(f'- {li.text.strip()}\n')
        elif tag.name == 'code':
            md_content.append(f'`{tag.text.strip()}`')
        elif 'w3-example' in tag.get('class', []):
            if tag.find('div', class_='w3-code'):
                code = tag.find('div', class_='w3-code')
                md_content.append(f'\n```python\n{code.text.strip()}\n```\n')

    return '\n'.join(md_content)

def start(base_url, next_url, stop_url):
    global page_count
    print('Getting url..')
    full_url = base_url + next_url
    print(f'Looking into {full_url}')
    html_doc = get(full_url)

    print(f'Cleaning page..')
    soup = BeautifulSoup(html_doc.read(), 'html.parser')

    print(f'Looking for important data..')
    heading = soup.find('h1')
    header = heading.text.strip()

    nav = soup.find('div', {'class': 'w3-clear nextprev'})
    url_save = []
    for nav in nav.findAll('a'):
        url_save.append(nav.get("href"))

    main_content = soup.find('div', {'id': 'main'})

    # Remove unwanted elements
    for div in main_content.find_all(['div'], {'class': ['w3-clear nextprev', 'w3-example']}):
        if 'w3-example' not in div.get('class', []):
            div.decompose()
    
    if main_content.find('div', {'id': 'mainLeaderboard'}):
        main_content.find('div', {'id': 'mainLeaderboard'}).decompose()

    # Convert to markdown
    markdown_content = html_to_markdown(main_content)
    
    page_count += 1
    
    print('Writing to file..')
    filename = f"data/{page_count}_{header.replace(' ', '_')}.md"

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(clean_text(markdown_content))

    print(f'{header} page saved.\nNumber of saved page: {page_count}\n')

    if url_save[1] != stop_url:
        start(base_url, url_save[1], stop_url)

    return page_count

start(b_url, n_url, s_url)
