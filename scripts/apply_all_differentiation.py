# -*- coding: utf-8 -*-
import os
import re
import json
from differentiate_data import (
    CATEGORY_INTERLINKS,
    AIRPORT_REVIEW_INTERLINKS,
    AIRPORT_TOP4_LEADINS,
    AIRPORT_SECTION3_LEADINS
)

def update_article_interlinks():
    # 1. Update 14 airport reviews
    for fname, interlink_text in AIRPORT_REVIEW_INTERLINKS.items():
        fpath = os.path.join("content/categories/airport-reviews", fname)
        if not os.path.exists(fpath):
            continue
        with open(fpath, "r", encoding="utf-8") as fp:
            txt = fp.read()
        
        # Replace interlink block (everything starting from ## 🔗)
        if "## 🔗" in txt:
            parts = txt.split("## 🔗")
            new_txt = parts[0].rstrip() + "\n\n" + interlink_text.strip() + "\n"
        else:
            new_txt = txt.rstrip() + "\n\n" + interlink_text.strip() + "\n"
        
        # Replace Top 4 leadin
        top4_leadin = AIRPORT_TOP4_LEADINS.get(fname)
        if top4_leadin and "## 🏆 2026 核心机场推荐榜单（固定精选前四）" in new_txt:
            # find pattern
            pat = r"(## 🏆 2026 核心机场推荐榜单（固定精选前四）\n\n)[^\n<]+"
            repl = r"\g<1>" + top4_leadin
            new_txt = re.sub(pat, repl, new_txt)
        
        # Replace Section 3 leadin
        sec3_leadin = AIRPORT_SECTION3_LEADINS.get(fname)
        if sec3_leadin and "### 三、 本文高点击率与标题核心搜索词速查" in new_txt:
            pat = r"(### 三、 本文高点击率与标题核心搜索词速查\n\n)[^\n-]+"
            repl = r"\g<1>" + sec3_leadin
            new_txt = re.sub(pat, repl, new_txt)
        
        with open(fpath, "w", encoding="utf-8") as fp:
            fp.write(new_txt)
    print("Updated 14 airport review interlinks & leadins successfully.")

    # 2. Update 38 tutorial and FAQ articles
    categories = ["windows", "mac", "ios", "android", "faq"]
    for cat in categories:
        cat_dir = os.path.join("content/categories", cat)
        interlink_text = CATEGORY_INTERLINKS[cat]
        for f in sorted(os.listdir(cat_dir)):
            if f.startswith("_") or not f.endswith(".md"):
                continue
            fpath = os.path.join(cat_dir, f)
            with open(fpath, "r", encoding="utf-8") as fp:
                txt = fp.read()
            
            if "## 🔗" in txt:
                parts = txt.split("## 🔗")
                new_txt = parts[0].rstrip() + "\n\n" + interlink_text.strip() + "\n"
            else:
                new_txt = txt.rstrip() + "\n\n" + interlink_text.strip() + "\n"
            
            with open(fpath, "w", encoding="utf-8") as fp:
                fp.write(new_txt)
    print("Updated 38 tutorial/FAQ interlinks successfully.")

    # 3. Update rankings article interlink
    rankings_path = "content/categories/airport-reviews/2026-airport-recommendation-rankings.md"
    if os.path.exists(rankings_path):
        with open(rankings_path, "r", encoding="utf-8") as fp:
            rtxt = fp.read()
        rankings_interlink = """## 🔗 推荐互链与全平台科学上网教程索引

- **桌面端推荐**：[Windows Clash Verge Rev 保姆级配置教程](/categories/windows/clash-verge-rev-windows-tutorial/) 与 [Mac Mihomo Party 客户端完整指南](/categories/mac/mihomo-party-mac-complete-guide/)。
- **移动端推荐**：[iOS Shadowrocket 小火箭配置教程](/categories/ios/shadowrocket-us-account-download-config/) 与 [Android Clash Meta 极速上手](/categories/android/clash-meta-for-android-tutorial/)。
- **全部机场测评**：[2026 全网 27 家机场独立测评与测速名录](/providers/)。"""
        if "## 🔗" in rtxt:
            parts = rtxt.split("## 🔗")
            new_rtxt = parts[0].rstrip() + "\n\n" + rankings_interlink.strip() + "\n"
            with open(rankings_path, "w", encoding="utf-8") as fp:
                fp.write(new_rtxt)
        print("Updated rankings article interlinks successfully.")

if __name__ == "__main__":
    update_article_interlinks()
