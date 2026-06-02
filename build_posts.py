import json
import os
import re
import random
import hashlib
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Set, Optional


class StaticSiteGenerator:
    """Professional static site generator with proper file management"""
    
    def __init__(self):
        self.site_url = "https://coretech.dpdns.org"
        self.required_templates = ['post.html', 'index.html', 'blogs.html', 'experiments.html']
        # ADD THESE - Static pages to NEVER delete
        self.static_pages = [
            'about.html', 'contact.html', 'privacy-policy.html', 'terms.html',
            'news.html', '404.html', 'style.css', 'ms-icon-310x310.png'
        ]
        self.generated_posts: Set[str] = set()
        
    def run(self) -> bool:
        """Main execution method"""
        print("\n" + "="*50)
        print("🚀 CORETECH STATIC SITE GENERATOR v2.0")
        print("="*50 + "\n")
        
        # Validate templates exist
        if not self._validate_templates():
            return False
            
        # Load data
        blogs = self._load_json('blogs.json')
        researches = self._load_json('researches.json')
        all_articles = blogs + researches
        
        print(f"📦 Loaded {len(blogs)} blogs, {len(researches)} experiments")
        print(f"📄 Total articles: {len(all_articles)}\n")
        
        # Generate individual post pages
        print("🔨 Generating individual post pages...")
        for article in all_articles:
            self._generate_post_page(article)
        
        # Update main listing pages
        print("\n📝 Updating listing pages...")
        self._update_listing_page('index.html', 'latest-articles',
                                [a for a in all_articles if a.get('show-on-homepage', False)])
        self._update_listing_page('blogs.html', 'blog-list', blogs)
        self._update_listing_page('experiments.html', 'experiments-list', researches)
        
        # Generate sitemap
        self._generate_sitemap(all_articles)
        
        # Clean up any orphaned files (PRESERVING static pages)
        self._cleanup_orphaned_posts(all_articles)
        
        print("\n" + "="*50)
        print("✅ BUILD COMPLETE!")
        print(f"   📊 Generated {len(self.generated_posts)} post pages")
        print("   🏠 Updated: index.html, blogs.html, experiments.html")
        print("   🗺️  Generated: sitemap.xml")
        print("   🔒 Preserved static pages: about, contact, privacy, terms")
        print("="*50 + "\n")
        
        return True
    
    def _validate_templates(self) -> bool:
        """Ensure all required template files exist"""
        missing = [f for f in self.required_templates if not os.path.exists(f)]
        if missing:
            print(f"❌ Missing required templates: {', '.join(missing)}")
            return False
        return True
    
    def _load_json(self, filename: str) -> List[Dict]:
        """Load JSON data with error handling"""
        if not os.path.exists(filename):
            print(f"⚠️  {filename} not found, using empty list")
            return []
        
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Ensure all items have required fields
                for item in data:
                    if 'id' not in item:
                        item['id'] = self._generate_slug(item.get('title', 'untitled'))
                return data
        except json.JSONDecodeError as e:
            print(f"❌ Error parsing {filename}: {e}")
            return []
    
    def _generate_slug(self, title: str) -> str:
        """Generate URL-friendly slug from title"""
        slug = title.lower()
        slug = re.sub(r'[^a-z0-9]+', '-', slug)
        slug = slug.strip('-')
        return slug
    
    def _get_existing_ids(self, content: str, container_id: str) -> Set[str]:
        """Extract existing article IDs from HTML container"""
        # Find the container div
        pattern = rf'<div[^>]*id=["\']?{container_id}["\']?[^>]*>'
        match = re.search(pattern, content)
        if not match:
            return set()
        
        start_pos = match.end()
        # Find the closing div (handling nested divs)
        depth = 1
        pos = start_pos
        while depth > 0 and pos < len(content):
            if content[pos:pos + 6] == '<div':
                depth += 1
                pos += 6
            elif content[pos:pos + 7] == '</div>':
                depth -= 1
                pos += 7
            else:
                pos += 1
        
        container_content = content[start_pos:pos - 7]  # -7 for </div>
        
        # Extract IDs from href attributes
        links = re.findall(r'href=["\']([^"\']*\.html)["\']', container_content)
        ids = {link.replace('.html', '') for link in links 
               if not link.startswith('http') and link.endswith('.html')}
        
        return ids

    def _render_card(self, post: Dict) -> str:
        """Generate HTML card for an article (NO SCHEMA - keep it clean)"""
        post_id = post.get('id', self._generate_slug(post.get('title', '')))
        title = post.get('title', 'Tech Insight')
        category = post.get('category', 'TECH').upper()

        # Clean description
        desc_raw = post.get('description', '')
        desc = re.sub(r'<[^>]+>', '', desc_raw)[:160]
        if len(desc) >= 157:
            desc += '...'

        img = post.get('img', '')
        link = f"{post_id}.html"

        return f'''            <div class="article-card">
                    <img src="{img}" alt="{title}" class="article-img" loading="lazy">
                    <div class="article-content">
                        <span class="article-category" style="color: var(--accent); font-size: 0.82rem; font-weight: 700;">{category}</span>
                        <h3>{self._escape_html(title)}</h3>
                        <p>{self._escape_html(desc)}</p>
                        <div class="meta">CoreTech • {datetime.now().strftime('%B %Y')}</div>
                        <a href="{link}" class="read-more">Read Full Article →</a>
                    </div>
                </div>
    '''
    
    def _escape_html(self, text: str) -> str:
        """Basic HTML escaping"""
        if not text:
            return ""
        return str(text).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

    def _update_listing_page(self, filename: str, container_id: str, articles: List[Dict]) -> None:
        """COMPLETELY WIPE container and REGENERATE from JSON"""
        print(f"   📄 Processing {filename}...")
    
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    
        # Generate fresh cards from JSON
        cards_html = []
        for article in articles:
            cards_html.append(self._render_card(article))
        new_content = '\n'.join(cards_html) if cards_html else ''
    
        # Find the container using string search (NO REGEX!)
        start_marker = f'<div class="articles" id="{container_id}">'
        end_marker = '</div>'
    
        start_pos = content.find(start_marker)
        if start_pos == -1:
            print(f"      ❌ Container '{container_id}' not found in {filename}")
            return
    
        # Find the matching closing tag (count nested divs)
        depth = 1
        pos = start_pos + len(start_marker)
        while depth > 0 and pos < len(content):
            if content[pos:pos + 5] == '<div ' or content[pos:pos + 4] == '<div>':
                depth += 1
                pos += 4
            elif content[pos:pos + 6] == '</div>':
                depth -= 1
                pos += 6
            else:
                pos += 1
    
        end_pos = pos - 6  # Position of the closing </div>
    
        # Build the new container with fresh content
        new_container = f'{start_marker}\n{new_content}\n        {end_marker}'
        updated = content[:start_pos] + new_container + content[end_pos:]
    
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(updated)
    
        print(f"      ✅ Wiped and regenerated {filename} with {len(cards_html)} cards")

    def _generate_faq_section(self, article: Dict) -> str:
        """Generate FAQ section from article data"""
        # Try different possible field names
        faqs = article.get('FAQ') or article.get('faqs') or article.get('faq')

        # Check if faqs exists and is a non-empty list
        if not faqs or not isinstance(faqs, list) or len(faqs) == 0:
            return ''

        faq_items_html = []
        for faq in faqs:
            question = faq.get('question', '')
            answer = faq.get('answer', '')
            if question and answer:
                faq_items_html.append(f'''
                <div class="faq-item">
                    <div class="faq-question">
                        <span>{self._escape_html(question)}</span>
                        <span class="faq-icon">▼</span>
                    </div>
                    <div class="faq-answer">
                        <p>{self._escape_html(answer)}</p>
                    </div>
                </div>
                ''')

        if not faq_items_html:
            return ''

        return f'''
        <div class="faq-section">
            <h2>Frequently Asked Questions</h2>
            <div class="faq-container">
                {''.join(faq_items_html)}
            </div>
        </div>
    '''

    def _generate_post_page(self, article: Dict) -> None:
        """Generate individual post HTML file from template"""
        post_id = article.get('id')
        if not post_id:
            post_id = self._generate_slug(article.get('title', ''))
            article['id'] = post_id
        
        output_file = f"{post_id}.html"
        
        if output_file in self.generated_posts:
            return
        with open('post.html', 'r', encoding='utf-8') as f:
            template = f.read()
        
        # Prepare content
        title = article.get('title', 'Tech Deep Dive')
        category = article.get('category', 'Technology')
        description = article.get('description', '')
        meta_desc = article.get('meta_desc', 'Description Is Not Available')
        content_body = article.get('content', description)
        img = article.get('featured_img') or article.get('img')
        
        # If image is missing OR is base64 data (which breaks on post pages), use fallback
        # if not img:
            # img = f"https://picsum.photos/id/{random.randint(100, 400)}/1200/600"
        # elif img.startswith('data:image'):
        #     # Base64 images don't work well on post pages
        #     # Use consistent image based on post_id
        #     hash_val = abs(hash(post_id)) % 300 + 100
        #     img = f"https://picsum.photos/id/{hash_val}/1200/600"
        
        # Replace template placeholders
        html = template
        # Meta tags
        html = html.replace('<title>CoreTech | Loading Deep Dive...</title>',
                        f'<title>{self._escape_html(title)}</title>')
        
        # Update meta description
        meta_desc = re.sub(
            r'<meta name="description" content="[^"]*"',
            f'<meta name="description" content="{self._escape_html(meta_desc)}"',
            html
        )
        if meta_desc != html:
            html = meta_desc
        
        # Update canonical URL
        html = re.sub(
            r'<link rel="canonical" href="[^"]*"',
            f'<link rel="canonical" href="{self.site_url}/{output_file}"',
            html
        )
        # Generate FAQ section (add this line BEFORE the content_html)
        faq_html = self._generate_faq_section(article)
        
        # Update content area
        content_html = f'''
        <main id="post-container">
            <span class="category">{self._escape_html(category)}</span>
            <div class="article-meta">
                Published: {datetime.now().strftime('%B %d, %Y')} • CoreTech
            </div>
            <img title="{self._escape_html(title)}" src="{img}" alt="{self._escape_html(title)}" class="featured-img" loading="eager">
            <div class="article-body article-content-render">
                {content_body}
            </div>
            {faq_html}
        </main>
    '''
        
        # Find and replace main content
        main_pattern = r'<main id="post-container">[\s\S]*?</main>'
        html = re.sub(main_pattern, content_html, html)
        
        # Write file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        self.generated_posts.add(output_file)
        print(f"      📝 Generated: {output_file}")

    def _generate_sitemap(self, articles: List[Dict]) -> None:
        """Generate sitemap.xml"""
        print("   🗺️  Generating sitemap.xml...")
        
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        sitemap = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>{self.site_url}/</loc>
        <lastmod>{current_date}</lastmod>
        <priority>1.00</priority>
    </url>
    <url>
        <loc>{self.site_url}/blogs.html</loc>
        <lastmod>{current_date}</lastmod>
        <priority>0.90</priority>
    </url>
    <url>
        <loc>{self.site_url}/experiments.html</loc>
        <lastmod>{current_date}</lastmod>
        <priority>0.90</priority>
    </url>
'''
        
        # Add static pages to sitemap
        static_urls = [
            ('about.html', 0.70),
            ('contact.html', 0.70),
            ('privacy-policy.html', 0.50),
            ('terms.html', 0.50),
        ]
        
        for page, priority in static_urls:
            if os.path.exists(page):
                sitemap += f'''    <url>
        <loc>{self.site_url}/{page}</loc>
        <lastmod>{current_date}</lastmod>
        <priority>{priority}</priority>
    </url>
'''
        
        for article in articles:
            post_id = article.get('id')
            if post_id:
                sitemap += f'''    <url>
        <loc>{self.site_url}/{post_id}.html</loc>
        <lastmod>{current_date}</lastmod>
        <priority>0.75</priority>
    </url>
'''
        
        sitemap += '</urlset>'
        
        with open('sitemap.xml', 'w', encoding='utf-8') as f:
            f.write(sitemap)
        
        print("      ✅ Sitemap generated")
    
    def _cleanup_orphaned_posts(self, articles: List[Dict]) -> None:
        """Remove post files that are no longer referenced in JSON - BUT NEVER delete static pages!"""
        print("   🧹 Cleaning up orphaned posts...")
        
        active_ids = {article.get('id') for article in articles if article.get('id')}
        
        # Files that should NEVER be deleted (static pages + templates)
        protected_files = set(self.required_templates + self.static_pages)
        
        orphaned = []
        
        for file in Path('.').glob('*.html'):
            # Skip protected files
            if file.name in protected_files:
                continue
            
            # Check if it's a generated post
            post_id = file.stem
            
            # Only delete if it's NOT a static page and NOT in active IDs
            if post_id not in active_ids:
                try:
                    file.unlink()
                    orphaned.append(file.name)
                except Exception as e:
                    print(f"      ⚠️  Could not delete {file.name}: {e}")
        
        if orphaned:
            print(f"      🗑️  Removed {len(orphaned)} orphaned posts: {', '.join(orphaned[:5])}")
            if len(orphaned) > 5:
                print(f"         ... and {len(orphaned) - 5} more")
        else:
            print("      ✅ No orphaned files found")


def build_static_site():
    """Entry point for the static site generator"""
    generator = StaticSiteGenerator()
    success = generator.run()
    
    if not success:
        print("\n❌ Build failed. Please check the errors above.")
        return False
    
    return True


if __name__ == '__main__':
    build_static_site()
