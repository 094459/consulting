# Tech Consulting Solutions Website

A modern, high-performance static website built with Hugo and the Adritian theme.

## Quick Start

### Running the Development Server

```bash
hugo server
```

Visit http://localhost:1313 to see your site.

### Building for Production

```bash
hugo
```

The built site will be in the `public/` directory.

## Customization Guide

### Adding Your Logos

Copy your logo files to these locations:
- Main logo: `static/images/logo.jpg` or `static/images/logo.png`
- Favicon: `assets/icons/favicon.png` (high-resolution, will be auto-resized)
- Banner/hero image: `static/images/showcase/showcase.png`

The theme will automatically generate favicons in multiple sizes from your `assets/icons/favicon.png` file.

### Updating Site Content

#### Homepage
Edit `content/home/home.md` to customize:
- Hero section text
- About section
- Services/expertise
- Social media links

#### Blog Posts
Create new blog posts in `content/blog/`:
```bash
hugo new blog/your-post-title.md
```

#### Experience/Projects
Add client projects in `content/experience/`:
```bash
hugo new experience/project-name.md
```

#### Client Work Showcase
Add portfolio items in `content/client-work/`:
```bash
hugo new client-work/client-name.md
```

### Configuration

Main configuration is in `hugo.toml`:
- Site title and description
- Navigation menus
- Social media links
- Analytics settings
- Blog layout options

### Key Features

- ⚡ Lightning-fast performance
- 📱 Fully responsive design
- 🌓 Automatic dark/light theme
- 🔍 Built-in search functionality
- 📝 Blog with categories and tags
- 💼 Portfolio/project showcase
- 📧 Contact form integration
- 🌐 Multi-language support (currently English only, but expandable)

## Theme Documentation

For detailed theme documentation, visit:
- [Adritian Theme GitHub](https://github.com/zetxek/adritian-free-hugo-theme)
- [Demo Site](https://adritian-demo.vercel.app/)

## Deployment

This site can be deployed to:
- Vercel (recommended)
- Netlify
- GitHub Pages
- Any static hosting service

### Vercel Deployment

1. Push your code to GitHub
2. Import the repository in Vercel
3. Vercel will auto-detect Hugo and deploy

## Next Steps

1. Replace placeholder images with your actual logos and photos
2. Update social media links in `content/home/home.md`
3. Customize the color scheme in `assets/scss/custom.scss` (if needed)
4. Add your actual client projects and testimonials
5. Write blog posts about your services and expertise
6. Set up contact form with Formspree or similar service
7. Configure analytics (Google Analytics or Vercel Analytics)

## Support

For theme-specific issues, check the [theme documentation](https://github.com/zetxek/adritian-free-hugo-theme) or open an issue on GitHub.
