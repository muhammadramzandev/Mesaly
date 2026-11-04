#!/usr/bin/env python3
"""MESALY site generator. Edit SITE below, then run: python3 build.py  (regenerates all .html, sitemap.xml, robots.txt)"""
import os, json, html
ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = 'https://www.mesaly.com'   # <- change to your real domain
TAG = 'Building Digital Solutions. Empowering Businesses.'
def w(n, t): open(os.path.join(ROOT, n), 'w', encoding='utf-8').write(t)
def E(s): return html.escape(s, quote=True)

# ---------- logo (M mark only) ----------
src = os.path.join(ROOT, 'logo-original.png')
if os.path.exists(src):
    from PIL import Image, ImageDraw, ImageFont
    c = Image.open(src).convert('RGB').crop((53, 22, 311, 156))
    c = c.resize((c.width * 3, c.height * 3), Image.LANCZOS).convert('RGBA'); px = c.load()
    for y in range(c.height):
        for x in range(c.width):
            r, g, b, _ = px[x, y]; m = min(r, g, b)
            px[x, y] = (r, g, b, 0 if m >= 228 else 255 if m <= 185 else int(255 * (228 - m) / 43))
    c = c.crop(c.split()[3].getbbox()); c.save(os.path.join(ROOT, 'logo.png'))
    s = 128; f = Image.new('RGBA', (s, s), (0, 0, 0, 0)); t = c.resize((112, int(112 * c.height / c.width)), Image.LANCZOS)
    f.paste(t, (8, (s - t.height) // 2), t); f.save(os.path.join(ROOT, 'favicon.png'))
    og = Image.new('RGB', (1200, 630), '#f6f8ff'); t = c.resize((420, int(420 * c.height / c.width)), Image.LANCZOS)
    og.paste(t, (90, (630 - t.height) // 2), t); d = ImageDraw.Draw(og)
    try: F1 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 96); F2 = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 32)
    except Exception: F1 = F2 = ImageFont.load_default()
    d.text((560, 230), 'MESALY', font=F1, fill='#0a1230'); d.text((560, 350), 'Web Design • Software Solutions', font=F2, fill='#2563ff')
    og.save(os.path.join(ROOT, 'og-image.png'))

# ---------- data ----------
I = dict(globe='M12 2a10 10 0 100 20 10 10 0 000-20zM2 12h20M12 2c3 3 3 17 0 20M12 2c-3 3-3 17 0 20', code='M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16',
 cloud='M7 18a4 4 0 010-8 5 5 0 019.6-1A4.5 4.5 0 0117 18z', chart='M4 20V10M10 20V4M16 20v-7M22 20H2', store='M3 9l2-5h14l2 5M4 9v11h16V9M9 20v-6h6v6',
 phone='M7 2h10a1 1 0 011 1v18a1 1 0 01-1 1H7a1 1 0 01-1-1V3a1 1 0 011-1zM11 18h2', monitor='M3 4h18v12H3zM8 20h8M12 16v4', cart='M3 4h2l2.4 11h10l2-8H6M9 20h.01M17 20h.01',
 bot='M5 8h14v10H5zM12 4v4M9 13h.01M15 13h.01M2 12v2M22 12v2', plug='M9 2v5M15 2v5M6 7h12v4a6 6 0 01-12 0zM12 17v5', pen='M4 20l4-1 11-11-3-3L5 16zM14 6l3 3',
 db='M4 6c0-2 16-2 16 0v12c0 2-16 2-16 0zM4 12c0 2 16 2 16 0', gear='M12 8a4 4 0 100 8 4 4 0 000-8zM12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2',
 wrench='M14 6a4 4 0 005 5l-9 9a2 2 0 01-3-3l9-9a4 4 0 00-2-2z', users='M9 11a3 3 0 100-6 3 3 0 000 6zM3 20c0-4 12-4 12 0M17 11a3 3 0 100-6M21 20c0-3-3-4-4-4',
 box='M3 7l9-4 9 4v10l-9 4-9-4zM3 7l9 4 9-4M12 11v10', school='M2 9l10-5 10 5-10 5zM6 11v5c3 3 9 3 12 0v-5', shield='M12 3l8 3v6c0 5-4 8-8 9-4-1-8-4-8-9V6zM9 12l2 2 4-4')
def ic(k): return f'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="{I[k]}"/></svg>'

SV = [('Web Development', 'globe', 'Fast, modern websites and web apps built to convert visitors into customers.', 'web-development'),
 ('Custom Software Development', 'code', 'Tailor-made business software designed around the way you actually work.', 'software-development'),
 ('SaaS Development', 'cloud', 'Multi-tenant, subscription-ready platforms built to scale from MVP to market.', 'saas-development'),
 ('ERP Development', 'chart', 'Connected accounting, inventory, HR and reporting in one business system.', 'erp-development'),
 ('POS Software Development', 'store', 'Retail and restaurant POS with barcode, receipts and live inventory sync.', 'pos-development'),
 ('Mobile App Development', 'phone', 'Android, iOS and cross-platform apps for customers and teams.', 'mobile-app-development'),
 ('Desktop Application Development', 'monitor', 'Reliable desktop software for offline-capable, high-performance workflows.', 'software-development'),
 ('E-Commerce Development', 'cart', 'Online stores with secure checkout, catalogue and order management.', 'web-development'),
 ('AI & Automation Solutions', 'bot', 'AI chatbots, intelligent reporting and automated business workflows.', 'ai-automation'),
 ('API Development & Integration', 'plug', 'Secure APIs and integrations that connect your tools and data.', 'ai-automation'),
 ('UI/UX Design', 'pen', 'Clear, modern interfaces designed around real user journeys.', 'web-development'),
 ('Cloud Solutions', 'cloud', 'Cloud deployment, hosting and CI/CD on AWS, Google Cloud and Azure.', 'saas-development'),
 ('Database Design & Management', 'db', 'Well-structured, secure and performant databases for any workload.', 'software-development'),
 ('Business Process Automation', 'gear', 'Remove manual, repetitive work with reliable automated workflows.', 'ai-automation'),
 ('IT Consulting & Maintenance', 'wrench', 'Technical guidance, audits and ongoing support for your systems.', 'contact'),
 ('CRM Development', 'users', 'Custom CRMs to manage leads, customers and sales pipelines.', 'software-development'),
 ('Inventory Management Systems', 'box', 'Track stock, suppliers and movements across locations in real time.', 'erp-development'),
 ('School & Hostel Management Systems', 'school', 'Admissions, attendance, fees, rooms and reporting in one platform.', 'software-development')]

DET = {
'web-development': ('Web Development', 'Websites and web applications that turn visitors into customers.',
 'MESALY designs and builds fast, secure and search-friendly websites and web applications — from polished corporate sites to data-driven platforms with custom dashboards. Every project is mobile-first, structured for SEO and ready to grow with your business.',
 ['Business websites', 'Corporate websites', 'Portfolio websites', 'Dynamic web applications', 'Custom dashboards', 'Landing pages', 'E-commerce websites', 'Website redesign', 'Website maintenance'],
 ['Fast, mobile-first pages that support search visibility', 'Clean, maintainable code you can extend later', 'Designed around your leads, sales and brand'],
 'HTML5,CSS3,JavaScript,TypeScript,React,Next.js,Vue.js,Tailwind CSS,Node.js,Laravel',
 [('How long does a website project take?', 'It depends on scope. We confirm a clear schedule after the discovery phase.'), ('Will my website be SEO-friendly?', 'Yes. We use semantic HTML, clean URLs, metadata, structured data and performance best practices from the start.')]),
'software-development': ('Custom Software Development', 'Software built around your business, not the other way around.',
 'When off-the-shelf tools do not fit, MESALY builds custom business software that matches your workflows, integrates with your existing systems and can grow with your organisation.',
 ['Custom business software', 'Enterprise applications', 'Workflow automation', 'Management systems', 'Database-driven applications', 'Third-party integrations'],
 ['Software that fits your exact processes', 'Fewer manual steps and less duplicate data entry', 'Full ownership of a scalable, documented codebase'],
 'Python,Django,Flask,Node.js,.NET,PHP,PostgreSQL,MySQL,Docker',
 [('Can you integrate with our existing tools?', 'Yes. We build and connect APIs to accounting, payment, messaging and other third-party systems.'), ('Who owns the source code?', 'Ownership terms are agreed in writing before the project starts.')]),
'saas-development': ('SaaS Development', 'Launch a scalable SaaS product with a solid foundation.',
 'From MVP to production platform, MESALY builds multi-tenant SaaS applications with authentication, subscriptions, admin tools and cloud deployment designed for secure growth.',
 ['Multi-tenant SaaS architecture', 'Subscription management', 'User authentication', 'Role-based access', 'Admin dashboards', 'Payment gateway integration', 'Cloud deployment', 'SaaS MVP development'],
 ['Validate your idea quickly with a focused MVP', 'Architecture ready for more customers and features', 'Billing, roles and security built in from day one'],
 'Next.js,React,TypeScript,Node.js,PostgreSQL,Firebase,Supabase,AWS,Docker,CI/CD',
 [('What is a SaaS MVP?', 'A minimum viable product contains only the core features needed to test your idea with real users.'), ('Which payment gateways can you integrate?', 'We integrate the gateway that is available in your target markets, such as Stripe or regional providers.')]),
'erp-development': ('ERP Development', 'One connected system for your whole operation.',
 'MESALY develops ERP systems that bring accounting, inventory, HR, purchasing and sales into a single platform with the reporting you need to make decisions.',
 ['Accounting management', 'Inventory management', 'HR management', 'Employee management', 'Purchase management', 'Sales management', 'Reporting and analytics', 'Multi-branch management'],
 ['A single source of truth for business data', 'Better visibility through live reports', 'Modules you can add as you grow'],
 'Laravel,PHP,Python,Django,.NET,PostgreSQL,MySQL,React,Docker',
 [('Can the ERP be built in phases?', 'Yes. We usually start with the most important modules and add others over time.'), ('Does it support multiple branches?', 'Yes. Multi-branch management and branch-level reporting can be included.')]),
'pos-development': ('POS Software Development', 'Fast, dependable point-of-sale software for retail and restaurants.',
 'We build POS systems that speed up checkout, keep inventory accurate and give owners clear sales analytics — for single shops and multi-outlet businesses.',
 ['Retail POS', 'Restaurant POS', 'Barcode scanning', 'Inventory synchronization', 'Sales tracking', 'Receipt generation', 'Customer management', 'Business analytics'],
 ['Quicker billing and fewer errors', 'Stock levels that stay in sync', 'Daily sales insight at a glance'],
 'React,Node.js,Laravel,PostgreSQL,MySQL,Firebase,Flutter,.NET',
 [('Does the POS work with barcode scanners and receipt printers?', 'Yes. Standard barcode scanners and receipt printers can be supported.'), ('Can it handle several outlets?', 'Yes. Inventory and reports can be shared across branches.')]),
'mobile-app-development': ('Mobile App Development', 'Mobile apps your customers and teams will actually use.',
 'MESALY builds polished Android, iOS and cross-platform apps with secure backends, smooth interfaces and a clear path to the app stores.',
 ['Android applications', 'iOS applications', 'Cross-platform applications', 'Business applications', 'Customer applications'],
 ['One codebase for both platforms where it makes sense', 'Smooth, native-feeling experience', 'Secure backend and API integration'],
 'Flutter,React Native,Kotlin,Firebase,Node.js,PostgreSQL',
 [('Native or cross-platform?', 'Cross-platform suits most business apps; native can be better for hardware-heavy features. We advise after discovery.'), ('Do you help publish to the app stores?', 'Yes. We prepare builds and guide you through store submission.')]),
'ai-automation': ('AI & Automation Solutions', 'Put AI and automation to work inside your business.',
 'We build practical AI-powered tools and automated workflows that save time, reduce errors and connect the systems you already use.',
 ['AI-powered business tools', 'AI chatbots', 'Workflow automation', 'Intelligent reporting', 'API integrations', 'AI-assisted business processes'],
 ['Less manual, repetitive work', 'Faster answers for customers and staff', 'Reports that surface what matters'],
 'Python,Node.js,REST APIs,PostgreSQL,Firebase,Docker,AWS',
 [('Is my data safe when using AI features?', 'We design with security in mind and only send the data that is necessary, following your requirements.'), ('Where should we start?', 'Start with one repetitive process. We help you pick the one with the clearest payoff.')])}

STEPS = [('Discovery', 'Understand client requirements and business objectives.'), ('Planning', 'Create project architecture and development strategy.'), ('UI/UX Design', 'Design modern and user-friendly interfaces.'),
 ('Development', 'Build secure, scalable, high-performance solutions.'), ('Testing', 'Perform functionality, security, and performance testing.'), ('Deployment', 'Launch the solution.'), ('Support', 'Provide ongoing maintenance and improvements.')]

IND = [('Healthcare', 'store', 'Appointment, patient-record and clinic management systems designed for privacy and reliability.'), ('Education', 'school', 'Student, fee, attendance and e-learning platforms for schools, colleges and academies.'),
 ('Retail', 'cart', 'POS, inventory and e-commerce solutions that keep shelves and online stores in sync.'), ('Restaurants', 'store', 'Ordering, table, kitchen and billing workflows with clear daily sales reports.'),
 ('Real Estate', 'globe', 'Listing portals, CRM and lead-tracking tools for agents and developers.'), ('Logistics', 'box', 'Shipment tracking, dispatch and warehouse tools with live status dashboards.'),
 ('Manufacturing', 'gear', 'ERP, production planning and stock control tailored to your processes.'), ('Hospitality', 'users', 'Booking, room and hostel management with guest and billing records in one place.'),
 ('Finance', 'shield', 'Secure dashboards, reporting and workflow tools built with data protection in mind.'), ('E-commerce', 'cart', 'Custom storefronts, catalogue, payments and order management.'),
 ('Startups', 'bot', 'MVP and SaaS development to validate ideas fast and scale when ready.'), ('Professional Services', 'chart', 'Client portals, CRM, invoicing and automation for agencies and consultancies.')]

DEMO = [('Corporate Website Concept', 'Websites', 'Multi-page corporate website with service pages, blog and lead forms.', 'Next.js, Tailwind CSS, Firebase', 'A concept showing a fast, SEO-ready corporate site with a content admin area, service pages and inquiry forms.'),
 ('Subscription Platform Demo', 'SaaS Applications', 'Multi-tenant SaaS with plans, roles and an admin dashboard.', 'React, Node.js, PostgreSQL', 'A concept showing tenant separation, subscription plans, role-based access and billing integration.'),
 ('ERP Suite Demo', 'ERP Systems', 'Accounting, inventory and HR modules with reporting.', 'Laravel, MySQL, Docker', 'A concept showing modular ERP with multi-branch inventory, purchasing, HR and analytics reports.'),
 ('Retail POS Demo', 'POS Systems', 'Barcode billing, receipts and live stock sync.', 'React, Node.js, PostgreSQL', 'A concept showing quick checkout, receipt printing, customer records and daily sales analytics.'),
 ('Business Mobile App Demo', 'Mobile Applications', 'Cross-platform app for orders and customer updates.', 'Flutter, Firebase', 'A concept showing authentication, push notifications and a synced backend on Android and iOS.'),
 ('Workflow Automation Tool Demo', 'Custom Software', 'Approval workflows and automated reports.', 'Python, Django, PostgreSQL', 'A concept showing rule-based approvals, notifications and scheduled reporting across teams.')]

TECH = {'Frontend': ['HTML5', 'CSS3', 'JavaScript', 'TypeScript', 'React', 'Next.js', 'Vue.js', 'Tailwind CSS'], 'Backend': ['Node.js', 'Python', 'Django', 'Flask', 'PHP', 'Laravel', '.NET'],
 'Mobile': ['Flutter', 'React Native', 'Kotlin'], 'Database': ['Firebase', 'PostgreSQL', 'MySQL', 'MongoDB', 'Supabase'], 'Cloud & Infrastructure': ['AWS', 'Google Cloud', 'Microsoft Azure', 'Docker', 'GitHub', 'CI/CD']}

POSTS = [('choose-tech-stack-web-project', 'How to Choose the Right Tech Stack for a New Web Project', 'Web Development',
 ['The best stack is the one that fits your product, your team and your timeline — not the one that is trending. Start by listing what the site must do: content pages, user accounts, payments, dashboards. Content-driven sites usually benefit from frameworks such as Next.js, while data-heavy portals may need a stronger backend such as Laravel, Django or Node.js.',
  'Then weigh hiring, hosting cost and long-term maintenance. A slightly less fashionable tool with good documentation and a large community is often cheaper to run for years. When in doubt, build a small prototype first and validate it before committing to the full architecture.']),
 ('multi-tenant-saas-decisions', 'Multi-Tenant SaaS: What to Decide Before You Write Code', 'SaaS Development',
 ['Multi-tenancy means one application serves many customers while keeping their data separate. The first decision is isolation: a shared database with a tenant identifier on every row is simple and cost-efficient, while separate schemas or databases give stronger isolation at higher operating cost.',
  'Plan authentication, role-based access, subscription billing and an admin dashboard early, because retrofitting them is expensive. Launching a focused MVP with these foundations lets you learn from real users before investing in advanced features.']),
 ('automate-business-processes', '5 Business Processes You Can Automate This Quarter', 'Business Automation',
 ['Look for work that is repetitive, rule-based and spread across several tools: invoice generation, lead routing, report compilation, customer follow-ups and data entry between systems. Each hour saved there is an hour your team can spend on work that needs judgment.',
  'Start with one process, document the steps, automate it with APIs or a lightweight workflow tool, and measure the time saved. Once it works, extend the same approach to the next process.']),
 ('erp-vs-pos', 'ERP vs POS: Which System Does Your Business Need First?', 'ERP & POS',
 ['A POS system focuses on the point of sale: billing, receipts, barcode scanning and daily sales tracking. An ERP connects wider operations such as accounting, purchasing, inventory, HR and reporting in one place.',
  'Retail shops and restaurants usually begin with POS and add inventory and accounting later. Growing multi-branch businesses often move to an integrated ERP. The right choice depends on where your biggest operational pain is today.']),
 ('maintainable-code', 'Why Maintainable Code Matters More Than Fast Delivery', 'Software Engineering',
 ['Software spends most of its life being changed, not written. Readable code, automated tests, clear documentation and consistent structure make every future feature faster and cheaper to add.',
  'Small habits help: code reviews, version control with meaningful commits, CI/CD pipelines and regular dependency updates. They add a little effort upfront and prevent expensive rewrites later.']),
 ('ai-for-small-business', 'Practical Ways Small Businesses Can Use AI Today', 'AI & Technology',
 ['You do not need a research team to benefit from AI. Common starting points include chatbots that answer routine customer questions, tools that summarise documents and reports, and assistants that draft replies for your team to review.',
  'Begin with a narrow, low-risk task, keep a human in the loop and protect customer data. Measure results before expanding to other areas of the business.']),
 ('digital-transformation-roadmap', 'A Simple Roadmap for Digital Transformation', 'Digital Transformation',
 ['Digital transformation is not buying software — it is improving how work gets done. Begin by mapping your current processes and finding bottlenecks such as manual spreadsheets, duplicate data entry or slow approvals.',
  'Prioritise improvements by impact and effort, deliver them in small phases, and train your team as you go. Each phase should show a measurable result before the next begins.'])]

NAV = [('Home', 'index.html'), ('Services', 'services.html'), ('Industries', 'industries.html'), ('Work', 'portfolio.html'), ('Technologies', 'technologies.html'), ('About', 'about.html'), ('Blog', 'blog.html'), ('Contact', 'contact.html')]
HL = ['en', 'en-US', 'en-GB', 'en-CA', 'en-AU', 'en-AE', 'en-SA', 'en-DE']
BUDGETS = ['Under $1,000', '$1,000 – $3,000', '$3,000 – $10,000', '$10,000 – $25,000', '$25,000 – $50,000', '$50,000+', 'Not sure yet']
COUNTRIES = ['United States', 'United Kingdom', 'Canada', 'Australia', 'United Arab Emirates', 'Saudi Arabia', 'Germany', 'Pakistan', 'India', 'Qatar', 'Kuwait', 'Netherlands', 'France', 'Singapore', 'Malaysia', 'Turkey', 'South Africa', 'Ireland']
WA = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 00-8.6 15L2 22l5.2-1.4A10 10 0 1012 2zm0 2a8 8 0 11-4.2 14.800l-.3-.2-2.300.6.600-2.200-.2-.3A8 8 0 0112 4zm-2.600 4.200c-.2 0-.5.100-.7.400-.3.300-1 1-1 2.400s1 2.700 1.200 2.900c.1.200 2 3.100 4.900 4.300 2.400.9 2.900.7 3.400.7.500-.1 1.600-.7 1.800-1.300.2-.6.2-1.200.2-1.300l-.5-.3-1.800-.9c-.3-.1-.5-.1-.7.1l-.8 1c-.1.200-.3.200-.5.100-.9-.4-2.200-1.100-3.100-2.600-.2-.3 0-.4.100-.6l.5-.6.300-.5c.1-.2 0-.4 0-.5l-.8-1.900c-.2-.5-.4-.4-.6-.4z"/></svg>'

pages = []
def P(f, title, desc, body, crumbs=(), schema=(), nav=None, noindex=False, add=True):
    url = SITE + ('/' if f == 'index.html' else '/' + f)
    hl = ''.join(f'<link rel="alternate" hreflang="{h}" href="{url}">' for h in HL) + f'<link rel="alternate" hreflang="x-default" href="{url}">'
    sch = list(schema)
    if crumbs:
        sch.append({'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': [{'@type': 'ListItem', 'position': i + 1, 'name': n, 'item': SITE + '/' + u} for i, (n, u) in enumerate([('Home', 'index.html')] + list(crumbs))]})
    js = ''.join(f'<script type="application/ld+json">{json.dumps(s)}</script>' for s in sch)
    navh = ''.join(f'<li><a href="{u}"{" class=on aria-current=page" if u == nav else ""}>{n}</a></li>' for n, u in NAV)
    ft = '<div class="fgd"><div><a class="lg" href="index.html"><img src="logo.png" alt="MESALY logo" width="60" height="30"><span>MESALY</span></a><p style="margin-top:14px">' + TAG + ' Custom web, software, SaaS, ERP, POS and AI solutions for clients worldwide.</p></div>' \
        '<div><h4>Company</h4><ul><li><a href="about.html">About</a></li><li><a href="portfolio.html">Our Work</a></li><li><a href="technologies.html">Technologies</a></li><li><a href="blog.html">Blog</a></li><li><a href="contact.html">Contact</a></li></ul></div>' \
        '<div><h4>Services</h4><ul>' + ''.join(f'<li><a href="{k}.html">{v[0]}</a></li>' for k, v in DET.items()) + '</ul></div>' \
        '<div><h4>Newsletter</h4><p>Insights on software, SaaS and automation.</p><form data-col="subscribers" novalidate style="margin-top:12px"><div class="nl"><div class="f"><label for="nle" class="sr" style="position:absolute;left:-9999px">Email</label><input id="nle" name="email" type="email" placeholder="you@company.com" autocomplete="email"><span class="er"></span></div><button class="btn s" type="submit">Subscribe</button></div><input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true"><p class="st" role="status"></p></form>' \
        '<p style="margin-top:16px"><a data-link="linkedin">LinkedIn</a> &nbsp; <a data-link="github">GitHub</a></p></div></div><div class="cp">© <span id="yr"></span> MESALY. All rights reserved.</div>'
    h = f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{E(title)}</title><meta name="description" content="{E(desc)}">' \
        f'<link rel="canonical" href="{url}">{hl}<meta name="robots" content="{"noindex,follow" if noindex else "index,follow,max-image-preview:large"}"><meta name="theme-color" content="#0a1230">' \
        f'<meta property="og:type" content="website"><meta property="og:site_name" content="MESALY"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/og-image.png">' \
        f'<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(title)}"><meta name="twitter:description" content="{E(desc)}"><meta name="twitter:image" content="{SITE}/og-image.png">' \
        f'<link rel="icon" href="favicon.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap">' \
        f'<link rel="stylesheet" href="style.css">{js}</head><body><div id="pre"><img src="logo.png" alt="MESALY"></div><a href="#main" style="position:absolute;left:-9999px">Skip to content</a>' \
        f'<header class="top"><div class="w nv"><a class="lg" href="index.html"><img src="logo.png" alt="MESALY logo" width="60" height="38"><span>MESALY</span></a><nav aria-label="Main"><ul>{navh}<li><a class="btn s" href="quote.html">Get a Quote</a></li></ul></nav><button id="mt" aria-label="Menu" aria-expanded="false">☰</button></div></header>' \
        f'<main id="main">{body}</main><footer><div class="w">{ft}</div></footer><a class="wa" data-link="whatsapp" aria-label="Chat on WhatsApp">{WA}</a>' \
        '<dialog id="dlg"><form method="dialog"><h3></h3><p class="m"></p><p class="n tag d"></p><div class="acts"><a class="btn s" href="quote.html">Request a similar project</a><button class="btn s o">Close</button></div></form></dialog>' \
        '<script src="config.js"></script><script src="app.js"></script><script>document.getElementById("yr").textContent=new Date().getFullYear()</script></body></html>'
    w(f, h)
    if add and not noindex: pages.append(f)

def hero(t, p, crumbs, eb='', btns=''):
    bc = '<a href="index.html">Home</a>' + ''.join(f' / <a href="{u}">{n}</a>' for n, u in crumbs)
    return f'<section class="ph dark"><div class="w"><div class="bc" role="navigation" aria-label="Breadcrumb">{bc}</div>{f"<span class=eb>{eb}</span><br>" if eb else ""}<h1>{t}</h1><p>{p}</p>{btns}</div></section>'
def cta(t="Let's Build Something Amazing Together.", s=None):
    q = 'quote.html' + (f'?service={E(s).replace(" ", "%20").replace("&amp;", "%26")}' if s else '')
    return f'<section class="sec dark cta"><div class="w rv"><h2>{t}</h2><p class="m">Tell us about your project and get a tailored proposal from the MESALY team.</p><div class="acts" style="justify-content:center"><a class="btn" href="{q}">Start Your Project</a><a class="btn o" href="contact.html">Contact Us</a></div></div></section>'
def cards(items): return ''.join(f'<a class="card rv" href="{p}.html" style="transition-delay:{i % 3 * 80}ms"><div class="ic">{ic(k)}</div><h3>{t}</h3><p>{d}</p><span class="lm">Learn More →</span></a>' for i, (t, k, d, p) in enumerate(items))
def process(dark=True):
    return f'<section class="sec {"dark" if dark else "alt"}" id="process"><div class="w"><div class="hd c"><span class="eb">How we work</span><h2>Our Development Process</h2><p>A clear, transparent seven-step approach from first conversation to ongoing support.</p></div><div class="g g4">' + \
        ''.join(f'<div class="card rv" style="transition-delay:{i * 90}ms"><div class="num gt">0{i + 1}</div><h3>{n}</h3><p>{d}</p></div>' for i, (n, d) in enumerate(STEPS)) + '</div></div></section>'
def ab(t):
    ws = t.replace('.', ' ').split()
    return ''.join(x[0] for x in ws)[:3].upper() if len(ws) > 1 else t[:2]
def chips(l): return '<div class="chips">' + ''.join(f'<span class="chip"><b>{E(ab(t))}</b>{E(t)}</span>' for t in l) + '</div>'
def fld(n, l, t='text', ac='', full=False, extra=''): return f'<div class="f{" full" if full else ""}"><label for="{n}">{l} *</label><input id="{n}" name="{n}" type="{t}" autocomplete="{ac or "off"}" {extra}><span class="er" role="alert"></span></div>'
def sel(n, l, opts, ph): return f'<div class="f"><label for="{n}">{l} *</label><select id="{n}" name="{n}"><option value="">{ph}</option>' + ''.join(f'<option>{E(o)}</option>' for o in opts) + '</select><span class="er" role="alert"></span></div>'
def area(n, l, ph): return f'<div class="f full"><label for="{n}">{l} *</label><textarea id="{n}" name="{n}" rows="5" placeholder="{ph}"></textarea><span class="er" role="alert"></span></div>'
def form(col, inner, btn): return f'<form class="card" data-col="{col}" novalidate><div class="fg">{inner}</div><input class="hp" name="website" tabindex="-1" autocomplete="off" aria-hidden="true"><button class="btn" type="submit">{btn}</button><p class="st" role="status"></p></form>'

ORG = {'@context': 'https://schema.org', '@graph': [{'@type': 'Organization', '@id': SITE + '/#org', 'name': 'MESALY', 'url': SITE, 'logo': SITE + '/logo.png', 'slogan': TAG, 'areaServed': 'Worldwide'},
 {'@type': 'ProfessionalService', 'name': 'MESALY', 'url': SITE, 'image': SITE + '/og-image.png', 'description': 'Software development company building websites, custom software, SaaS, ERP, POS and AI solutions.', 'areaServed': 'Worldwide', 'parentOrganization': {'@id': SITE + '/#org'}},
 {'@type': 'WebSite', 'name': 'MESALY', 'url': SITE}]}

# ---------- home ----------
vis = f'<div class="vis" aria-label="Animated illustration of software, cloud, dashboards and AI" role="img"><div class="orb"></div><img class="mid" src="logo.png" alt="MESALY M logo"><div class="fc c1">Business dashboard<div class="bars"><i style="height:40%"></i><i style="height:70%"></i><i style="height:50%"></i><i style="height:92%"></i><i style="height:64%"></i></div></div><div class="fc c2">&lt;/&gt; build(software)</div><div class="fc c3">{ic("cloud")}Cloud infra</div><div class="fc c4">{ic("bot")}AI engine</div><div class="fc c5">{ic("plug")}Connected apps</div></div>'
trust = [('Custom-Built Solutions', 'code', 'Every system is designed around your goals.'), ('Scalable Technology', 'cloud', 'Architecture that grows with your business.'), ('Security-Focused Development', 'shield', 'Secure practices built in from the start.'), ('Global Client Support', 'globe', 'Remote collaboration with clients worldwide.')]
home = f'<section class="hero"><div class="w hg"><div><span class="eb">Software Development Company</span><h1>We Build Technology That <span class="gt">Moves Businesses Forward.</span></h1><p class="lead">From custom software and intelligent business systems to scalable SaaS platforms, MESALY transforms complex business challenges into powerful digital solutions.</p><div class="acts"><a class="btn" href="quote.html">Start Your Project</a><a class="btn o" href="#services">Explore Our Services</a></div></div>{vis}</div></section>' \
  '<section class="sec alt"><div class="w"><div class="g g4">' + ''.join(f'<div class="card rv"><div class="ic">{ic(k)}</div><h3>{t}</h3><p>{d}</p></div>' for t, k, d in trust) + '</div></div></section>' \
  '<section class="sec" id="services"><div class="w"><div class="hd c"><span class="eb">What we do</span><h2>Services Built for Modern Businesses</h2><p>Eighteen specialised services covering web, software, SaaS, ERP, POS, mobile, AI and more.</p></div><div class="g g3">' + cards(SV) + '</div></div></section>' + process() + \
  '<section class="sec"><div class="w"><div class="hd c"><span class="eb">Industries</span><h2>Technology Tailored to Your Industry</h2></div><div class="chips" style="justify-content:center">' + ''.join(f'<a class="chip" href="industries.html">{n}</a>' for n, _, _ in IND) + '</div><p style="text-align:center;margin-top:28px"><a class="btn o s" style="color:var(--b)" href="industries.html">See how we help each industry</a></p></div></section>' \
  '<section class="sec alt" id="tst" hidden><div class="w"><div class="hd c"><span class="eb">Testimonials</span><h2>What Clients Say</h2></div><div class="g g3"></div></div></section>' + cta()
P('index.html', 'MESALY | Software Development Company — Web, SaaS, ERP & POS', 'MESALY is a software development company building custom software, web applications, SaaS, ERP, POS and AI automation for businesses worldwide.', home, schema=[ORG], nav='index.html')

# ---------- services ----------
P('services.html', 'Software & Web Development Services | MESALY', 'Explore MESALY services: web development, custom software, SaaS, ERP, POS, mobile apps, AI automation, cloud, CRM and more.',
  hero('Our Services', 'End-to-end technology services for startups, growing businesses and enterprises.', [('Services', 'services.html')]) + '<section class="sec"><div class="w"><div class="g g3">' + cards(SV) + '</div></div></section>' + cta(), crumbs=[('Services', 'services.html')], nav='services.html')
for k, (t, tg, ds, ft, bn, tc, fq) in DET.items():
    sch = [{'@context': 'https://schema.org', '@type': 'Service', 'name': t, 'description': ds, 'provider': {'@type': 'Organization', 'name': 'MESALY', 'url': SITE}, 'areaServed': 'Worldwide', 'serviceType': t},
           {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}} for q, a in fq]}]
    qs = 'quote.html?service=' + t.replace(' ', '%20').replace('&', '%26')
    body = hero(t, tg, [('Services', 'services.html'), (t, k + '.html')], 'Service', f'<div class="acts"><a class="btn" href="{qs}">Get a Quote for {t}</a><a class="btn o" href="contact.html">Talk to Our Team</a></div>') + \
      f'<section class="sec"><div class="w g g2" style="align-items:center"><div class="rv"><span class="eb">Overview</span><h2>{t} by MESALY</h2><p class="m" style="margin-top:16px">{ds}</p></div><div class="card rv"><h3>Key benefits</h3><ul class="ck" style="margin-top:16px">' + ''.join(f'<li>{b}</li>' for b in bn) + '</ul></div></div></section>' \
      '<section class="sec alt"><div class="w"><div class="hd"><span class="eb">What we deliver</span><h2>Features & Capabilities</h2></div><div class="g g3">' + ''.join(f'<div class="card rv"><div class="ic">{ic("code")}</div><h3>{f}</h3></div>' for f in ft) + '</div></div></section>' \
      '<section class="sec"><div class="w"><div class="hd"><span class="eb">Stack</span><h2>Technologies We Use</h2></div>' + chips(tc.split(',')) + '</div></section>' + process(False) + \
      '<section class="sec"><div class="w pr"><div class="hd"><span class="eb">FAQ</span><h2>Frequently Asked Questions</h2></div>' + ''.join(f'<details><summary>{E(q)}</summary><p>{E(a)}</p></details>' for q, a in fq) + '</div></section>' + cta(s=t)
    P(k + '.html', f'{t} Company | MESALY', f'{tg} {ds[:110]}', body, crumbs=[('Services', 'services.html'), (t, k + '.html')], schema=sch, nav='services.html')

# ---------- industries / work / tech ----------
P('industries.html', 'Industries We Serve | MESALY Software Solutions', 'MESALY builds customised software for healthcare, education, retail, restaurants, real estate, logistics, manufacturing, hospitality, finance, e-commerce and startups.',
  hero('Industries We Serve', 'Every industry works differently. We tailor each solution to your processes, customers and goals.', [('Industries', 'industries.html')]) + '<section class="sec"><div class="w"><div class="g g3">' + ''.join(f'<div class="card rv"><div class="ic">{ic(k)}</div><h3>{n}</h3><p>{d}</p></div>' for n, k, d in IND) + '</div></div></section>' + cta(), crumbs=[('Industries', 'industries.html')])
def mock(i):
    a, b = [('#2563ff', '#7c3aed'), ('#0ea5e9', '#2563ff'), ('#7c3aed', '#db2777'), ('#0891b2', '#2563ff'), ('#4f46e5', '#06b6d4'), ('#2563ff', '#0a1230')][i % 6]
    bars = ''.join(f'<rect x="{150 + j * 26}" y="{120 - h}" width="16" height="{h}" rx="3" fill="#fff" opacity=".{o}"/>' for j, (h, o) in enumerate([(30, 6), (60, 8), (45, 6), (80, 9), (55, 7)]))
    return f'<svg class="mk" viewBox="0 0 320 170" role="img" aria-label="Illustration of {E(DEMO[i][0])}"><defs><linearGradient id="g{i}" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{a}"/><stop offset="1" stop-color="{b}"/></linearGradient></defs><rect width="320" height="170" fill="url(#g{i})"/><rect x="18" y="16" width="284" height="12" rx="6" fill="#fff" opacity=".25"/><rect x="18" y="40" width="100" height="112" rx="10" fill="#fff" opacity=".18"/><rect x="132" y="40" width="170" height="112" rx="10" fill="#fff" opacity=".12"/>{bars}</svg>'
work = '<section class="sec"><div class="w"><p class="m" style="margin-bottom:12px"><span class="tag d">Demonstration projects</span> The projects below are concepts created by MESALY to show typical scope and quality. They are not client work. Real case studies will appear here as projects are completed.</p><div class="pills">' + ''.join(f'<span class="tag">{c}</span>' for c in ['Websites', 'SaaS Applications', 'ERP Systems', 'POS Systems', 'Mobile Applications', 'Custom Software']) + '</div><div class="g g3" id="projects">' + \
  ''.join(f'<div class="card rv">{mock(i)}<span class="tag">{c}</span> <span class="tag d">Demo</span><h3>{t}</h3><p>{d}</p><p><strong>Tech:</strong> {tc}</p><button class="btn s" style="margin-top:14px" data-t="{E(t)}" data-more="{E(m)}" data-demo="1">View Project</button></div>' for i, (t, c, d, tc, m) in enumerate(DEMO)) + '</div></div></section>'
P('portfolio.html', 'Our Work — Demonstration Projects | MESALY', 'Browse MESALY demonstration projects across websites, SaaS, ERP, POS, mobile apps and custom software. Clearly labelled concepts, not client work.', hero('Our Work', 'Demonstration projects that show what MESALY can build for you.', [('Our Work', 'portfolio.html')]) + work + cta(), crumbs=[('Our Work', 'portfolio.html')], nav='portfolio.html')
P('technologies.html', 'Technologies We Use | MESALY', 'MESALY builds with React, Next.js, Node.js, Python, Laravel, .NET, Flutter, PostgreSQL, Firebase, AWS, Azure, Docker and more.', hero('Technologies We Use', 'A modern, proven stack chosen to fit each project — never forced.', [('Technologies', 'technologies.html')]) + '<section class="sec"><div class="w">' + ''.join(f'<div class="rv" style="margin-bottom:40px"><h2 style="font-size:1.5rem;margin-bottom:16px">{c}</h2>{chips(l)}</div>' for c, l in TECH.items()) + '</div></section>' + cta(), crumbs=[('Technologies', 'technologies.html')], nav='technologies.html')

# ---------- about ----------
vals = [('Quality', 'We build clean, tested and maintainable software.'), ('Transparency', 'Clear communication, scope and progress at every step.'), ('Security', 'Secure practices are part of every build.'), ('Scalability', 'Solutions designed to grow with your business.'), ('Partnership', 'We work as an extension of your team.')]
why = ['Custom-built solutions, not one-size-fits-all templates', 'Modern, maintainable technology stack', 'Security-focused development practices', 'Clear process and transparent communication', 'Flexible engagement for startups through enterprises', 'Remote collaboration with clients worldwide']
about = hero('Technology With Purpose. <span class="gt">Innovation Without Limits.</span>', 'MESALY is a technology-focused company dedicated to helping businesses grow through innovative software, modern web applications, scalable SaaS platforms, and intelligent digital solutions.', [('About', 'about.html')]) + \
  '<section class="sec"><div class="w g g2"><div class="card rv"><div class="ic">' + ic('shield') + '</div><h3>Our Mission</h3><p>To help businesses of every size work smarter by delivering reliable, secure and scalable software that solves real problems.</p></div><div class="card rv"><div class="ic">' + ic('globe') + '</div><h3>Our Vision</h3><p>To be a trusted global technology partner known for quality engineering and long-term client success.</p></div></div></section>' \
  '<section class="sec alt"><div class="w"><div class="hd c"><span class="eb">Values</span><h2>What We Believe In</h2></div><div class="g g3">' + ''.join(f'<div class="card rv"><h3>{t}</h3><p>{d}</p></div>' for t, d in vals) + '<div class="card rv"><h3>Development Philosophy</h3><p>Understand the problem first, keep solutions simple, ship in small steps and improve continuously.</p></div></div></div></section>' \
  '<section class="sec"><div class="w g g2"><div class="rv"><span class="eb">Why choose us</span><h2>Why Choose MESALY?</h2></div><ul class="ck rv">' + ''.join(f'<li>{x}</li>' for x in why) + '</ul></div></section>' + process() + cta()
P('about.html', 'About MESALY | Technology With Purpose', 'Learn about MESALY — a technology company building innovative software, web applications, SaaS platforms and intelligent digital solutions for businesses worldwide.', about, crumbs=[('About', 'about.html')], nav='about.html')

# ---------- quote & contact ----------
PK = [('Custom Website Development', 'Business, corporate, e-commerce and landing-page websites.'), ('Custom Software Development', 'Management systems, workflow automation and integrations.'), ('SaaS Development', 'MVPs and full multi-tenant subscription platforms.'), ('ERP/POS Development', 'Inventory, accounting, billing and multi-branch systems.'), ('Mobile App Development', 'Android, iOS and cross-platform applications.')]
svopts = [s[0] for s in SV] + ['Other']
qf = form('inquiries', fld('name', 'Full Name', ac='name') + fld('email', 'Email Address', 'email', 'email') + fld('company', 'Company Name', ac='organization') + '<div class="f"><label for="country">Country *</label><input id="country" name="country" list="cl" autocomplete="country-name"><datalist id="cl">' + ''.join(f'<option value="{c}">' for c in COUNTRIES) + '</datalist><span class="er" role="alert"></span></div>' + sel('service', 'Service Required', svopts, 'Select a service') + sel('budget', 'Estimated Budget (USD)', BUDGETS, 'Select a budget range') + area('message', 'Project Description', 'Tell us about your goals, users and timeline'), 'Submit Project Request')
quote = hero('Request a Quote', 'Every project is different, so we price based on scope. Share your requirements and receive a tailored proposal.', [('Request a Quote', 'quote.html')]) + \
  '<section class="sec"><div class="w"><div class="g g3">' + ''.join(f'<div class="card rv"><h3>{t}</h3><p>{d}</p><p class="gt" style="font-weight:700;font-size:1.2rem">Custom quote</p><a class="btn s" style="margin-top:14px" href="quote.html?service={t.replace(" ", "%20").replace("&", "%26")}#qf">Request a quote</a></div>' for t, d in PK) + '</div></div></section>' \
  '<section class="sec alt" id="qf"><div class="w pr"><div class="hd"><span class="eb">Project request</span><h2>Tell Us About Your Project</h2></div>' + qf + '</div></section>'
P('quote.html', 'Request a Quote — Custom Software & Web Development | MESALY', 'Request a custom quote from MESALY for web development, software, SaaS, ERP, POS or mobile apps. Budget ranges in USD.', quote, crumbs=[('Request a Quote', 'quote.html')])
cf = form('messages', fld('name', 'Full Name', ac='name') + fld('email', 'Email Address', 'email', 'email') + fld('subject', 'Subject', full=True) + area('message', 'Message', 'How can we help?'), 'Send Message')
contact = hero("Let's Build Something Amazing Together.", 'Questions, ideas or a project in mind? Send us a message and we will respond as soon as possible.', [('Contact', 'contact.html')]) + \
  f'<section class="sec"><div class="w g g2" style="align-items:start"><div>{cf}</div><div class="g"><div class="card"><h3>Get in touch</h3><ul class="ck" style="margin-top:14px"><li>Email: <a data-link="email"><span data-text="email"></span></a></li><li><a data-link="whatsapp">Chat on WhatsApp</a></li><li><a data-link="linkedin">LinkedIn</a></li><li><a data-link="github">GitHub</a></li></ul></div><div class="card"><h3>Project inquiry</h3><p>Planning a website, SaaS, ERP, POS or mobile app? Share your requirements for a tailored proposal.</p><a class="btn s" style="margin-top:14px" href="quote.html">Request a Quote</a></div></div></div></section>'
P('contact.html', 'Contact MESALY | Start Your Software Project', 'Contact MESALY to discuss your web, software, SaaS, ERP, POS or mobile project. Send a message or request a quote.', contact, crumbs=[('Contact', 'contact.html')], nav='contact.html')

# ---------- blog ----------
ex = lambda p: p[0].split('. ')[0].rstrip('.') + '.'
cats = list(dict.fromkeys(p[2] for p in POSTS))
blog = hero('Blog & Resources', 'Practical insights on software, SaaS, automation and digital transformation.', [('Blog', 'blog.html')]) + \
  '<section class="sec"><div class="w"><label for="bs" class="m">Search articles</label><input id="bs" type="search" placeholder="Search…" style="max-width:420px;display:block;margin-top:6px"><div class="pills"><button class="pill on" data-c="">All</button>' + ''.join(f'<button class="pill" data-c="{c}">{c}</button>' for c in cats) + '</div><div class="g g3" id="posts">' + \
  ''.join(f'<a class="card" href="blog-{s}.html"><span class="tag">{c}</span><h3>{t}</h3><p>{ex(b)}</p><span class="lm">Read article →</span></a>' for s, t, c, b in POSTS) + '</div></div></section>'
P('blog.html', 'Blog — Software, SaaS & Automation Insights | MESALY', 'Articles on web development, SaaS, business automation, ERP & POS, software engineering, AI and digital transformation from MESALY.', blog, crumbs=[('Blog', 'blog.html')], nav='blog.html')
for i, (s, t, c, b) in enumerate(POSTS):
    rel = [POSTS[(i + 1) % len(POSTS)], POSTS[(i + 2) % len(POSTS)]]
    body = hero(t, c, [('Blog', 'blog.html'), (t, f'blog-{s}.html')], c) + '<section class="sec"><div class="w pr">' + ''.join(f'<p>{x}</p>' for x in b) + '</div></section><section class="sec alt"><div class="w"><div class="hd"><h2>Related Articles</h2></div><div class="g g2">' + ''.join(f'<a class="card" href="blog-{a}.html"><span class="tag">{cc}</span><h3>{tt}</h3><p>{ex(bb)}</p></a>' for a, tt, cc, bb in rel) + '</div></div></section>' + cta()
    P(f'blog-{s}.html', f'{t} | MESALY Blog', ex(b), body, crumbs=[('Blog', 'blog.html'), (t, f'blog-{s}.html')], nav='blog.html',
      schema=[{'@context': 'https://schema.org', '@type': 'Article', 'headline': t, 'articleSection': c, 'author': {'@type': 'Organization', 'name': 'MESALY'}, 'publisher': {'@type': 'Organization', 'name': 'MESALY', 'logo': {'@type': 'ImageObject', 'url': SITE + '/logo.png'}}}])
P('post.html', 'Article | MESALY Blog', 'MESALY blog article.', '<div id="pd"><section class="ph dark"><div class="w"><span class="tag"></span><h1>Loading…</h1></div></section><section class="sec"><div class="w pr"></div></section></div>' + cta(), noindex=True, nav='blog.html')
P('404.html', 'Page not found | MESALY', 'Page not found.', hero('Page not found', 'The page you are looking for does not exist.', [], '', '<div class="acts"><a class="btn" href="index.html">Back to Home</a></div>'), noindex=True)

# ---------- sitemap / robots ----------
w('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'<url><loc>{SITE}{"/" if p == "index.html" else "/" + p}</loc></url>\n' for p in pages) + '</urlset>\n')
w('robots.txt', f'User-agent: *\nAllow: /\nDisallow: /admin.html\nDisallow: /post.html\n\nSitemap: {SITE}/sitemap.xml\n')
print(len(pages), 'indexable pages built')
