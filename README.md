# MESALY — Company Website

Static, zero-dependency website (HTML/CSS/JS) — no build tools needed to host it. Optional Firebase backend for saved forms, blog/portfolio/testimonials and the admin panel.

## What is inside
- 23 SEO pages: home, services (+7 detailed service pages), industries, portfolio (labelled demo projects), technologies, about, quote, contact, blog (+7 articles)
- `admin.html` — admin panel (Firebase Auth + role-based access), `post.html` — blog posts created from admin
- `` — style.css, app.js, config.js, logo (M mark), favicon, og-image
- `sitemap.xml`, `robots.txt`, hreflang + x-default, canonical, Open Graph, Twitter cards, Organization / Service / Breadcrumb / FAQ / Article schema
- `build.py` — regenerates all HTML (`python3 build.py`, needs Python 3 + Pillow only if `logo-original.png` exists)
- `firestore.rules` — security rules

## 1. Run locally
Open `index.html`, or: `python3 -m http.server 8000` → http://localhost:8000

## 2. Configure (`config.js`)
Set `email`, `whatsapp` (digits with country code), `linkedin`, `github`. Empty LinkedIn/GitHub links stay hidden. 
Until Firebase is configured, forms open the visitor's email app addressed to your `email` (a real email is required — the placeholder will show a "not configured" message).

## 3. Set your domain
Edit `SITE` at the top of `build.py` (default `https://www.mesaly.com`), then run `python3 build.py`. This updates canonical URLs, hreflang, sitemap, robots and schema.

## 4. Enable Firebase (forms + admin)
1. Create a project at console.firebase.google.com → add a Web app → copy the config into `config.js` (`firebase: {...}`).
2. Build → Authentication → enable **Email/Password**; create your admin user.
3. Build → Firestore Database → create database → Rules → paste `firestore.rules` → Publish.
4. Create a document in collection `admins` with ID = your user's UID and field `role` = `admin` (editors: `editor`, can manage posts/projects/testimonials only).
5. Open `/admin.html`, sign in. Inquiries, messages and subscribers appear automatically.
6. In Authentication → Settings → Authorized domains, add your live domain.

Content collections the site reads (only documents with `published: true`):
- `posts` {title, category, excerpt, body (separate paragraphs with a blank line), published}
- `projects` {title, category, description, tech, more, demo (true/false), published}
- `testimonials` {name, role, company, quote, published} — the testimonials section stays hidden until you add genuine ones.

## 5. Deploy
Any static host works: **Netlify** or **Cloudflare Pages** (drag & drop the folder), **Vercel** (`vercel --prod`), **Firebase Hosting** (`firebase init hosting` → public dir = this folder → `firebase deploy`). Then submit `https://YOUR-DOMAIN/sitemap.xml` in Google Search Console.

## Notes
- Portfolio items are labelled demonstration projects. Replace them with real case studies when available (add via admin with `demo: false`).
- No fake statistics, certifications or testimonials are included.
- Never put secret keys in the frontend; Firebase web config is public by design — security comes from the rules.
