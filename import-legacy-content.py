#!/usr/bin/env python3
"""
Import legacy Hugo content and update frontmatter for the new site
"""
import os
import re
from pathlib import Path
from datetime import datetime

def parse_frontmatter(content):
    """Extract frontmatter and body from markdown content"""
    # Match YAML frontmatter between --- markers
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)
    
    if match:
        frontmatter = match.group(1)
        body = match.group(2)
        return frontmatter, body
    return None, content

def parse_yaml_field(frontmatter, field):
    """Extract a field value from YAML frontmatter"""
    pattern = rf'^{field}:\s*(.+)$'
    match = re.search(pattern, frontmatter, re.MULTILINE)
    if match:
        value = match.group(1).strip()
        # Remove quotes if present
        value = value.strip('"\'')
        return value
    return None

def parse_yaml_list(frontmatter, field):
    """Extract a list field from YAML frontmatter"""
    # Try bracket notation first: tags: [tag1, tag2]
    pattern = rf'^{field}:\s*\[(.*?)\]'
    match = re.search(pattern, frontmatter, re.MULTILINE)
    if match:
        items = match.group(1).split(',')
        return [item.strip().strip('"\'') for item in items if item.strip()]
    
    # Try multi-line notation: tags:\n  - tag1\n  - tag2
    pattern = rf'^{field}:\s*\n((?:  - .+\n?)+)'
    match = re.search(pattern, frontmatter, re.MULTILINE)
    if match:
        lines = match.group(1).strip().split('\n')
        return [line.strip().lstrip('- ').strip('"\'') for line in lines]
    
    return []

def create_new_frontmatter(title, date, tags, canonical_url=None):
    """Create Hugo frontmatter in TOML format"""
    frontmatter = f"""+++
title = "{title}"
date = {date}
draft = false
tags = {tags}
categories = ["Technical"]"""
    
    if canonical_url:
        frontmatter += f'\ncanonicalUrl = "{canonical_url}"'
    
    frontmatter += "\n+++"
    return frontmatter

def process_file(source_path, dest_dir):
    """Process a single markdown file"""
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        frontmatter, body = parse_frontmatter(content)
        
        if not frontmatter:
            print(f"  ⚠️  No frontmatter found in {source_path.name}")
            return False
        
        # Extract fields
        title = parse_yaml_field(frontmatter, 'title')
        date_str = parse_yaml_field(frontmatter, 'date')
        tags = parse_yaml_list(frontmatter, 'tags')
        canonical_url = parse_yaml_field(frontmatter, 'canonicalUrl')
        
        if not title or not date_str:
            print(f"  ⚠️  Missing title or date in {source_path.name}")
            return False
        
        # Format tags for TOML
        if tags:
            tags_str = '["' + '", "'.join(tags) + '"]'
        else:
            tags_str = '[]'
        
        # Create new frontmatter
        new_frontmatter = create_new_frontmatter(title, date_str, tags_str, canonical_url)
        
        # Combine new frontmatter with body
        new_content = new_frontmatter + "\n\n" + body.strip() + "\n"
        
        # Write to destination
        dest_path = dest_dir / source_path.name
        with open(dest_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        return True
        
    except Exception as e:
        print(f"  ❌ Error processing {source_path.name}: {e}")
        return False

def main():
    """Main import function"""
    source_dir = Path('legacy-content')
    dest_dir = Path('content/blog')
    
    if not source_dir.exists():
        print(f"❌ Source directory '{source_dir}' not found")
        return
    
    if not dest_dir.exists():
        print(f"❌ Destination directory '{dest_dir}' not found")
        return
    
    # Get all markdown files
    md_files = list(source_dir.glob('*.md'))
    
    if not md_files:
        print(f"❌ No markdown files found in '{source_dir}'")
        return
    
    print(f"📚 Found {len(md_files)} markdown files to import")
    print(f"📂 Importing from: {source_dir}")
    print(f"📂 Importing to: {dest_dir}")
    print()
    
    success_count = 0
    
    for md_file in md_files:
        print(f"Processing: {md_file.name}")
        if process_file(md_file, dest_dir):
            success_count += 1
            print(f"  ✅ Imported successfully")
        print()
    
    print(f"\n{'='*60}")
    print(f"✨ Import complete!")
    print(f"   Successfully imported: {success_count}/{len(md_files)} files")
    print(f"{'='*60}")

if __name__ == '__main__':
    main()
