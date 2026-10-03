# -*- coding: utf-8 -*-
import os
import re
import json

def count_chinese_chars(text):
    clean_text = re.sub(r'<[^>]+>', '', text)
    clean_text = re.sub(r'---.*?---', '', clean_text, flags=re.S)
    clean_text = re.sub(r'\[(.*?)\]\(.*?\)', r'\1', clean_text)
    clean_text = re.sub(r'http[s]?://\S+', '', clean_text)
    zh_chars = re.findall(r'[\u4e00-\u9fa5]', clean_text)
    return len(zh_chars)

print("Starting full update...")
