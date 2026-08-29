with open('src/engines/researchgate.py', 'r') as f:
    content = f.read()

# Fix the string literal issue caused by triple quotes replacement
content = content.replace(r'["\'](https://www\.researchgate\.net/profile/[^"\']+/publication/[^"\']+/file/[^"\']+ \.pdf)["\']',
                          r'["\'](https://www\.researchgate\.net/profile/[^"\']+/publication/[^"\']+/file/[^"\']+ \.pdf)["\']')

# Wait, let's just do a targeted regex replace for the line that has issues
import re
# The exact line in error: pdf_matches += re.findall(r'["'](https://www\.researchgate\.net/profile/[^"']+/publication/[^"']+/file/[^"']+ \.pdf)["']', page_source)
# I need to replace ["'] with ["\']
bad_str = r"r'[\"'](https://www\.researchgate\.net/profile/[^\"']+/publication/[^\"']+/file/[^\"']+ \.pdf)[\"']'"
good_str = r"r'[\"\'](https://www\.researchgate\.net/profile/[^\"\']+/publication/[^\"\']+/file/[^\"\']+ \.pdf)[\"\']'"

# Let's just fix it manually using string replace
fixed_content = content.replace("r'[\"'](https://www\.researchgate\.net/profile/[^\"']+/publication/[^\"']+/file/[^\"']+ \.pdf)[\"']'", "r'[\"\\'](https://www\.researchgate\.net/profile/[^\"\\']+/publication/[^\"\\']+/file/[^\"\\']+ \.pdf)[\"\\']'")

with open('src/engines/researchgate.py', 'w') as f:
    f.write(fixed_content)
