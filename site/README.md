# Westworld Story Viewer

An Astro-based web application that renders story content and generates narrative prose from YAML data.

## Features

- **Dynamic Content**: Renders characters, scenes, and timeline from YAML files
- **Narrative Generation**: Automatically converts scene data to prose narratives
- **Responsive Design**: Modern, mobile-friendly interface
- **Auto-deployment**: GitHub Actions workflow for Vercel deployment

## Quick Start

### Local Development

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Visit http://localhost:4321
```

### Build and Deploy

```bash
# Generate narratives and build
npm run build

# Preview production build
npm run preview
```

## Project Structure

```
site/
├── src/
│   ├── pages/           # Astro pages and routes
│   ├── components/      # Reusable components
│   ├── layouts/         # Page layouts
│   ├── utils/           # Utility functions
│   └── content/         # Generated content
├── package.json         # Dependencies and scripts
├── astro.config.mjs     # Astro configuration
└── vercel.json          # Vercel deployment config
```

## Scripts

- `npm run dev` - Start development server
- `npm run build` - Generate narratives and build for production
- `npm run preview` - Preview production build
- `npm run generate` - Run Python narrative generator

## Data Sources

The site reads from the parent directory:
- `canon/characters.yml` - Character definitions
- `canon/scenes.yml` - Scene data
- `canon/timeline.yml` - Timeline events
- `canon/themes.yml` - Story themes
- `canon/world.yml` - World and location data

## Deployment

The site automatically deploys to Vercel on every push to the main branch via GitHub Actions.

## Customization

- Modify `src/layouts/Layout.astro` to change the site-wide design
- Update `src/utils/narrative-generator.js` to change narrative generation logic
- Add new pages in `src/pages/` following Astro conventions
