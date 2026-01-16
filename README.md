# Vidya Sagar Reddy Venna - Personal Website

Ultra-minimal personal website built with Jekyll. Pure grayscale design, Markdown blogging, deployed on GitHub Pages with automatic HTTPS.

**Live Site:** [https://ViSaReVe.github.io](https://visareve.github.io)

---

## Quick Start

### Adding a Blog Post (No Terminal Needed!)

1. Go to [https://github.com/vsrvenna/vsrvenna.github.io](https://github.com/visareve/visareve.github.io)
2. Navigate to the `_posts/` folder
3. Click "Add file" → "Create new file"
4. Name your file: `YYYY-MM-DD-your-post-title.md` (e.g., `2026-01-20-intro-to-neural-decoding.md`)
5. Copy the template from `BLOG-TEMPLATE.md` (see below)
6. Write your content in Markdown
7. Click "Commit new file"
8. Wait 1-2 minutes for GitHub Pages to rebuild
9. View your post at `https://vsrvenna.github.io/posts/your-post-title`

**That's it!** No command line, no local setup required.

---

## Markdown Basics

Markdown is MUCH simpler than HTML. Here are the basics:

### Headings
```markdown
# Heading 1
## Heading 2
### Heading 3
```

### Text Formatting
```markdown
**Bold text**
*Italic text*
```

### Lists
```markdown
- Bullet point 1
- Bullet point 2
- Bullet point 3

1. Numbered item 1
2. Numbered item 2
3. Numbered item 3
```

### Links
```markdown
[Link text](https://example.com)
```

### Code Blocks
````markdown
```python
# Python code here
print("Hello, world!")
```
````

### Images (if needed)
```markdown
![Alt text](/assets/images/filename.jpg)
```

---

## Site Structure

```
vsrvenna.github.io/
├── _config.yml              # Site configuration
├── _layouts/                # Page templates
├── _includes/               # Reusable components
├── _posts/                  # Blog posts (Markdown files)
├── _data/                   # Structured content
│   ├── projects.yml         # Your projects
│   ├── publications.yml     # Your papers
│   └── experience.yml       # Your work history
├── assets/css/              # Styling
├── index.html               # Homepage
├── about.md                 # About page
└── posts.html               # Blog listing
```

---

## Common Tasks

### 1. Add a Project

Edit `_data/projects.yml`:

```yaml
- title: "Your New Project"
  institution: "USC / Company"
  date: "Spring 2026"
  description: "One paragraph description of your project..."
  tags:
    - Tag1
    - Tag2
  featured: true  # true = shows on homepage, false = only on About page
```

Commit the changes on GitHub web interface or locally.

**Featured projects** (with `featured: true`) appear on the homepage. All projects appear on the About page.

### 2. Add a Publication

Edit `_data/publications.yml`:

```yaml
- title: "Your Paper Title"
  authors: "Author1, Author2, You"
  venue: "Conference Name YYYY"
  year: 2026
```

### 3. Add Work Experience

Edit `_data/experience.yml`:

```yaml
- role: "Your Role"
  organization: "Company / University"
  period: "Month YYYY - Present"
  description: "Brief description of what you did..."
```

### 4. Update Personal Info

**To change email, social links:**
Edit `_config.yml`:

```yaml
author:
  name: "Vidya Sagar Reddy Venna"
  email: "your-new-email@example.com"
  github: "your-github-username"
  linkedin: "your-linkedin-username"
  scholar: "your-scholar-id"
```

**To change bio:**
Edit `about.md` directly.

### 5. Customize Colors

Edit `assets/css/main.scss`:

```scss
// Change these hex codes
$color-black: #1a1a1a;
$color-gray-dark: #333333;
$color-gray: #666666;
$color-gray-light: #999999;
$color-white: #ffffff;
```

### 6. Customize Spacing

Edit `assets/css/main.scss`:

```scss
// Increase whitespace
$space-12: 8rem;  // Change from 6rem to 8rem for more space
```

---

## Local Development (Optional)

If you want to preview changes locally before pushing to GitHub:

### Requirements

- Ruby 2.7 or higher
- Bundler

### Setup

```bash
# 1. Clone the repository
git clone https://github.com/vsrvenna/vsrvenna.github.io.git
cd vsrvenna.github.io

# 2. Install dependencies
bundle install

# 3. Run local server
bundle exec jekyll serve

# 4. Open browser
# Visit http://localhost:4000
```

---

## Deployment

The site is automatically deployed to GitHub Pages whenever you push changes to the `main` branch.

**GitHub Pages URL:** [https://vsrvenna.github.io](https://vsrvenna.github.io)

**HTTPS:** Automatic and free (provided by GitHub Pages)

### Initial Setup (Already Done!)

1. Create GitHub repository named `vsrvenna.github.io`
2. Push all files to `main` branch
3. Go to repo Settings → Pages
4. Source: Deploy from `main` branch, `/` (root)
5. Wait 1-2 minutes for initial build
6. Site live at `https://vsrvenna.github.io`

---

## Troubleshooting

### Blog post not showing up

**Problem:** You created a blog post but it's not appearing on the site.

**Solutions:**
1. **Check filename:** Must be `YYYY-MM-DD-title.md` format
2. **Check frontmatter:** Must have valid YAML frontmatter (between `---` markers)
3. **Check date:** Date in filename must be today or earlier (future dates won't show)
4. **Wait:** GitHub Pages takes 1-2 minutes to rebuild after each commit
5. **Check build status:** Go to repo → Actions tab → see if build succeeded

### Site build failing

**Problem:** GitHub Actions shows build error.

**Common causes:**
1. **YAML syntax error:** Missing colon, wrong indentation in frontmatter
2. **Missing closing code blocks:** Need three backticks (```) to close code blocks
3. **Liquid syntax error:** Check `{% %}` and `{{ }}` tags are closed

**How to fix:**
1. Go to repo → Actions tab
2. Click on failed build
3. Read error message
4. Fix the issue in the file
5. Commit and push again

### Post formatting looks wrong

**Problem:** Text isn't formatted correctly on the site.

**Solutions:**
1. **Check code blocks:** Make sure you're using three backticks (```) not single backticks
2. **Check headers:** Need space after `#` (e.g., `## Heading` not `##Heading`)
3. **Check lists:** Need blank line before and after list
4. **Check links:** Format is `[text](url)` not `[text] (url)`

### Local Jekyll won't install

**Problem:** `bundle install` fails or Jekyll command not found.

**Solutions:**
1. **Check Ruby version:** Need Ruby 2.7+. Run `ruby --version`
2. **Update RubyGems:** `gem update --system`
3. **Use system Ruby:** On Mac, system Ruby may be too old. Install Ruby via Homebrew:
   ```bash
   brew install ruby
   ```
4. **Skip local dev:** You don't need local Jekyll! Just edit on GitHub web interface.

---

## Resources

### Jekyll & Markdown
- **Jekyll Docs:** [https://jekyllrb.com/docs/](https://jekyllrb.com/docs/)
- **Markdown Guide:** [https://www.markdownguide.org/basic-syntax/](https://www.markdownguide.org/basic-syntax/)
- **GitHub Pages Docs:** [https://docs.github.com/en/pages](https://docs.github.com/en/pages)

### Tools
- **GitHub Web Editor:** [https://github.com/vsrvenna/vsrvenna.github.io](https://github.com/vsrvenna/vsrvenna.github.io)
- **GitHub Desktop** (GUI app): [https://desktop.github.com/](https://desktop.github.com/)
- **VS Code** (local editing): [https://code.visualstudio.com/](https://code.visualstudio.com/)

### Help
- **Jekyll Community:** [https://talk.jekyllrb.com/](https://talk.jekyllrb.com/)
- **GitHub Community:** [https://github.community/](https://github.community/)
- **Markdown Help:** [https://commonmark.org/help/](https://commonmark.org/help/)

---

## Design Philosophy

This site follows an **ultra-minimal** design aesthetic:

- **Pure grayscale** (black, white, grays only)
- **No borders** on cards or sections
- **No shadows** or visual effects
- **No hover animations**
- **Maximum whitespace** (96px between sections)
- **Content-first** approach
- **Single column** layout
- **System fonts** for native look

**Why minimal?**
- Faster load times
- More professional appearance
- Focus on content over decoration
- Easier to maintain
- Better for readers

---

## License

This website design is created for Vidya Sagar Reddy Venna. Feel free to use as inspiration but please don't copy directly.

Content (blog posts, projects, publications) © 2026 Vidya Sagar Reddy Venna. All rights reserved.

---

## Questions?

Have questions about maintaining this site? Email me at [vvenna@usc.edu](mailto:vvenna@usc.edu).

---

**Last Updated:** January 2026
