# -*- coding: utf-8 -*-
import os

OLD_DOMAIN = "jichangnow.com"
NEW_DOMAIN = "tiziview.co"

root_dir = '.'
modified_files = []

for dirpath, dirnames, filenames in os.walk(root_dir):
    if 'public' in dirnames:
        dirnames.remove('public')
    if '.git' in dirnames:
        dirnames.remove('.git')
    for f in filenames:
        if f == 'migrate_domain.py':
            continue
        fp = os.path.join(dirpath, f)
        try:
            with open(fp, 'r', encoding='utf-8') as file:
                content = file.read()
            
            if OLD_DOMAIN in content:
                new_content = content.replace(OLD_DOMAIN, NEW_DOMAIN)
                with open(fp, 'w', encoding='utf-8') as file:
                    file.write(new_content)
                modified_files.append(fp)
        except Exception as e:
            pass

print(f"Migrated {len(modified_files)} files to {NEW_DOMAIN}:")
for mf in modified_files:
    print(f" - {mf}")
