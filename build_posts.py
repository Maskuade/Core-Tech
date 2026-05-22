import json
import os
import re
import random
from datetime import datetime


def build_static_site():
    # Verify core layout files are present
    required_files = ['post.html', 'index.html', 'blogs.html', 'experiments.html']
    for file in required_files:
        if not os.path.exists(file):
            print(f"❌ Error: Required core file '{file}' missing from workspace directory!")
            return
            
    with open('post.html', 'r', encoding='utf-8') as template_file:
        post_template = template_file.read()

    # Read data streams natively
    blogs = []
    researches = []
    if os.path.exists('blogs.json'):
        with open('blogs.json', 'r', encoding='utf-8') as f: blogs = json.load(f)
    if os.path.exists('researches.json'):
        with open('researches.json', 'r', encoding='utf-8') as f: researches = json.load(f)

    all_articles = blogs + researches
    current_date = datetime.now().strftime('%Y-%m-%d')
    print(f"🔄 Starting complete site compilation for {len(all_articles)} items...")

    # --- PART A: BUILD STANDALONE HTML ARTICLE PAGES ---
    compiled_count = 0
    for item in all_articles:
        post_id = item.get('id')
        if not post_id: continue

        title = item.get('title', 'Technology Article')
        category = item.get('category', 'TECH').upper()
        article_body_html = item.get('description', '')
        image_data = item.get('img', '')
        output_filename = f"{post_id}.html"

        faq_html = ""
        faq_list = item.get('FAQ', [])
        if faq_list:
            faq_html += '\n\t<div class="faq-box" style="margin-top:4rem;"><h2>Frequently Asked Questions</h2>'
            for faq in faq_list:
                faq_html += f'''
        <details class="faq-item" style="margin: 1rem 0; padding: 1rem; border: 1px solid var(--border); border-radius: 8px;">
            <summary class="faq-question" style="cursor:pointer; font-weight:700;">{faq.get('question')}</summary>
            <div class="faq-answer" style="margin-top:0.5rem;"><p>{faq.get('answer')}</p></div>
        </details>'''
            faq_html += '\n\t</div>'

        article_markup = f'''
        <article class="article-body" style="padding-top: 2rem;">
            <span class="category" style="color: var(--accent); font-weight: 700;">{category}</span>
            <div class="article-meta" style="color:var(--muted); margin-bottom:1rem;">Published by CoreTech • 2026</div>
            <img src="{image_data}" alt="{title}" class="featured-img" style="width:100%; max-height:480px; object-fit:cover; border-radius:12px; margin-bottom:2rem;">
            <div class="article-content-render">
                {article_body_html}
            </div>
            {faq_html}
            <a href="index.html" class="back-link" style="display:inline-block; margin-top:3rem; color:var(--accent); text-decoration:none; font-weight:600;">← Back to Homepage</a>
        </article>
        '''

        container_pattern = r'(<main\s+id=["\']post-container["\']\s*>)[\s\S]*?(<\/main>)'
        fixed_main_block = r'\1' + article_markup + r'\2'
        page_output = re.sub(container_pattern, fixed_main_block, post_template)
        page_output = re.sub(r'<title>.*?<\/title>', f'<title>{title} | CoreTech</title>', page_output)

        with open(output_filename, 'w', encoding='utf-8') as out_file:
            out_file.write(page_output)
        compiled_count += 1
    print(f"   ↳ ✅ Successfully compiled {compiled_count} unique post pages.")

    # --- PART B: AUTOMATE SITEMAP.XML GENERATION ---
    print("🌐 Automating sitemap.xml structure...")
    sitemap_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://sitemaps.org">
    <!-- Core Shell Index Pages -->
    <url><loc>https://coretech.dpdns.org</loc><lastmod>{current_date}</lastmod><priority>1.00</priority></url>
    <url><loc>https://coretech.dpdns.org/blogs.html</loc><lastmod>{current_date}</lastmod><priority>0.80</priority></url>
    <url><loc>https://coretech.dpdns.org/experiments.html</loc><lastmod>{current_date}</lastmod><priority>0.80</priority></url>
    <url><loc>https://coretech.dpdns.org/about.html</loc><lastmod>{current_date}</lastmod><priority>0.50</priority></url>
    <url><loc>https://coretech.dpdns.org/contact.html</loc><lastmod>{current_date}</lastmod><priority>0.50</priority></url>
    <url><loc>https://coretech.dpdns.org/privacy-policy.html</loc><lastmod>{current_date}</lastmod><priority>0.30</priority></url>
    <url><loc>https://coretech.dpdns.org/terms.html</loc><lastmod>{current_date}</lastmod><priority>0.30</priority></url>
    
    <!-- Dynamic Compiled Post Frameworks -->'''

    for item in all_articles:
        post_id = item.get('id')
        if post_id:
            sitemap_xml += f'\n    <url><loc>https://coretech.dpdns.org/{post_id}.html</loc><lastmod>{current_date}</lastmod><priority>0.70</priority></url>'
    sitemap_xml += '\n</urlset>'
    
    with open('sitemap.xml', 'w', encoding='utf-8') as xml_file:
        xml_file.write(sitemap_xml.strip())
    print("   ↳ ✅ sitemap.xml index map successfully synchronized!")

    # --- PART C: AUTOMATE LLMS.TXT COGNITIVE MAPPING ---
    print("🤖 Synthesizing structural llms.txt context profiles...")
    llms_text = f'''# CoreTech
> A technology and software engineering platform rediscovering the curiosity, fun, and wonder of tech—from our childhood dreams to the AI era.

## Core Technology Articles & Experiments'''
    for item in all_articles:
        post_id = item.get('id')
        if post_id:
            desc_clean = re.sub('<[^<]+?>', '', item.get('description', ''))[:140].strip() + '...'
            llms_text += f'\n- [{item.get("title")}](https://coretech.dpdns.org/{post_id}.html): {desc_clean}'
            
    with open('llms.txt', 'w', encoding='utf-8') as txt_file:
        txt_file.write(llms_text.strip())
    print("   ↳ ✅ llms.txt AI dataset synced!")

    # --- HELPER FUNCTION TO COMPILE ARTICLE CARDS ---
    def generate_cards_layout(dataset):
        html_cards = "\n"
        for post in dataset:
            p_title = post.get('title', 'Tech Insight')
            p_category = post.get('category', 'Technology').upper()
            p_desc = re.sub('<[^<]+?>', '', post.get('description', ''))[:165].strip() + '...'
            p_img = post.get('img') if post.get('img') else f"https://picsum.photos{random.randint(1,100)}/600/400"
            p_link = f"{post.get('id')}.html"
            html_cards += f'''
                <div class="article-card">
                    <img src="{p_img}" alt="{p_title}" class="article-img">
                    <div class="article-content">
                        <span style="color: var(--accent); font-size: 0.82rem; font-weight: 700;">{p_category}</span>
                        <h3>{p_title}</h3>
                        <p>{p_desc}</p>
                        <div class="meta">CoreTech • May 2026</div>
                        <a href="{p_link}" style="color: var(--accent); font-weight: 600; text-decoration: none; margin-top: 0.8rem; display: inline-block;">
                            Read Full Article →
                        </a>
                    </div>
                </div>\n'''
        return html_cards

    # --- PART D: HARDCODE INDEX.HTML ---
    print("🏠 Hardcoding homepage feed (index.html)...")
    home_data = [i for i in all_articles if i.get("show-on-homepage") == True]
    with open('index.html', 'r', encoding='utf-8') as f: index_content = f.read()
    updated_index = re.sub(r'(<div\s+class=["\']articles["\']\s+id=["\']latest-articles["\']\s*>)[\s\S]*?(<\/div>)', r'\1' + generate_cards_layout(home_data) + '\t\t\t' + r'\2', index_content)
    with open('index.html', 'w', encoding='utf-8') as f: f.write(updated_index)

    # --- PART E: HARDCODE BLOGS.HTML ---
    print("📰 Hardcoding blogs feed (blogs.html)...")
    with open('blogs.html', 'r', encoding='utf-8') as f: blogs_content = f.read()
    updated_blogs = re.sub(r'(<div\s+[^>]*id=["\']blog-list["\']\s*>)[\s\S]*?(<\/div>)', r'\1' + generate_cards_layout(blogs) + '\t\t\t' + r'\2', blogs_content)
    with open('blogs.html', 'w', encoding='utf-8') as f: f.write(updated_blogs)

    # --- PART F: HARDCODE EXPERIMENTS.HTML ---
    print("🧪 Hardcoding research feed (experiments.html)...")
    with open('experiments.html', 'r', encoding='utf-8') as f: exp_content = f.read()
    # 🎯 Fixed ID pattern to match your exact plural "experiments-list" template element
    updated_exp = re.sub(r'(<div\s+[^>]*id=["\']experiments-list["\']\s*>)[\s\S]*?(<\/div>)', r'\1' + generate_cards_layout(researches) + '\t\t\t' + r'\2', exp_content)
    with open('experiments.html', 'w', encoding='utf-8') as f: f.write(updated_exp)

    print("\n🚀 PLATFORM COMPILATION 100% SUCCESSFUL! STATIC ARCHITECTURE BUILT.")


if __name__ == '__main__':
    build_static_site()
