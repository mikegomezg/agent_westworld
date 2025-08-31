# GitHub Pages Setup for agent_westworld

This project now uses GitHub Pages with Jekyll for a simple, robust website.

## What Was Created

### 1. Jekyll Configuration (`_config.yml`)

- Basic site settings
- Navigation structure
- Excludes unnecessary files from processing

### 2. Main Pages

- `index.md` - Homepage with links to all sections
- `characters.md` - Character information
- `scenes.md` - Scene listings
- `narratives.md` - Generated narrative content

### 3. Narrative Generator (`scripts/generate_site_content.py`)

- Automatically creates markdown files from scene YAML data
- Resolves character IDs to names
- Generates formatted narrative content
- Creates navigation indexes

### 4. GitHub Actions Workflow (`.github/workflows/generate-site.yml`)

- Automatically runs when story files change
- Generates new narratives
- Commits changes back to repository
- Runs daily to ensure content freshness

## How to Use

### Enable GitHub Pages

1. Go to your repository settings
2. Scroll to "Pages" section
3. Select "Deploy from a branch"
4. Choose "main" branch and "/ (root)" folder
5. Click Save

### Generate Narratives Manually

```bash
python scripts/generate_site_content.py
```

### View Your Site

After pushing changes, wait 2-3 minutes for GitHub Pages to build, then visit:
`https://mikegomezg.github.io/agent_westworld/`

## Creating Issues for Claude

### Generate All Narratives

```markdown
Title: Generate narrative for Peter's malfunction

@claude Please run `python scripts/generate_site_content.py` to generate narratives from all scene files. Commit the results.
```

### Improve Narrative Generation

```markdown
Title: Improve scene narrative output

@claude Please update the generate_site_content.py script to include:
1. Character names instead of IDs
2. Location descriptions
3. Theme connections
Then regenerate all narratives.
```

## File Structure

```
agent_westworld/
├── _config.yml              # Jekyll configuration
├── index.md                 # Homepage
├── characters.md            # Character page
├── scenes.md                # Scenes page
├── narratives.md            # Narratives index
├── narratives/              # Generated narrative files
│   ├── index.md            # Narratives navigation
│   ├── S01E01-001.md       # Individual narratives
│   └── S01E01-003.md
├── canon/                   # Canon data (included in site)
├── story/                   # Story structure (included in site)
├── scripts/                 # Generation scripts
└── .github/workflows/       # Auto-generation workflow
```

## Advantages

1. **Zero dependencies** - Just Python and GitHub's built-in Jekyll
2. **Always works** - GitHub Pages rarely fails
3. **Version controlled** - All narratives are committed to repo
4. **Simple feedback** - Just create issues asking for regeneration
5. **Readable fallback** - Even if Jekyll fails, markdown files are readable on GitHub

## Troubleshooting

### Site Not Building

- Check GitHub Actions tab for workflow failures
- Ensure `_config.yml` is valid YAML
- Verify all markdown files have proper front matter

### Narratives Not Updating

- Check if GitHub Actions workflow is enabled
- Verify the workflow has permission to push to main branch
- Run the generation script manually to test

### Missing Content

- Ensure files are in the correct directories
- Check that `_config.yml` includes the right directories
- Verify markdown files have proper Jekyll front matter
