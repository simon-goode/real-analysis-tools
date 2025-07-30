import re
import sys
from typing import List, Union

'''Extract LaTeX expressions from Markdown content.'''

def extract_latex_from_markdown(md_content: str, include_inline: bool = True) -> List[str]:
    # inline: $...$
    inline = re.findall(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', md_content, re.DOTALL) if include_inline else []
    # display: $$...$$
    display = re.findall(r'\$\$(.+?)\$\$', md_content, re.DOTALL)
    # blocks: \[ ... \]
    block = re.findall(r'\\\[(.+?)\\\]', md_content, re.DOTALL)
    # environments: \begin{...}...\end{...}
    env = re.findall(r'\\begin\{([a-zA-Z*]+)\}(.+?)\\end\{\1\}', md_content, re.DOTALL)
    env = [f"\\begin{{{name}}}{body}\\end{{{name}}}" for name, body in env]
    return inline + display + block + env

def extract_latex(filepath_or_md: Union[str, None], include_inline: bool = True) -> List[str]:
    if filepath_or_md is None:
        return []
    try:
        # try to open as file
        with open(filepath_or_md, 'r', encoding='utf-8') as f:
            md_content = f.read()
    except (FileNotFoundError, OSError):
        # treat as markdown string
        print(f"Warning: Could not open file {filepath_or_md}. Treating as markdown string.", file=sys.stderr)
        md_content = filepath_or_md
    return extract_latex_from_markdown(md_content, include_inline)

if __name__ == "__main__":
    print(extract_latex("testdata/test.md"))