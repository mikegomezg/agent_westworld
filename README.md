# Westworld Story Framework

A modular, markdown-based approach to collaborative story development using Westworld Season 1 as demo content. This framework enables AI agents to collaboratively create, validate, and maintain complex narrative structures through structured markdown files and automated generation.

## 🎯 Project Overview

The Westworld Story Framework transforms storytelling into a collaborative, markdown-based process where:
- **Story elements** are structured markdown files with validation
- **AI agents** can collaboratively edit through GitHub
- **Content generation** is automated through Python scripts
- **Themes** are systematically explored and developed
- **Timelines** are managed with chronological consistency

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Git

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd agent_westworld

# Install dependencies
pip install -r requirements.txt

# Run validation
python checks/validate_markdown.py
```

### Basic Usage

```bash
# Validate all markdown content
python checks/validate_markdown.py

# Generate all content
python scripts/generate_all.py

# Generate specific content types
python scripts/generate/narrative_from_scene.py
python scripts/generate/enrich_character_profile.py
python scripts/generate/timeline_visualization.py
python scripts/generate/theme_analysis.py
```

## 🏗️ Project Structure

```
agent_westworld/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── pyproject.toml           # Project configuration
├── canon/                   # Core story content (markdown)
│   ├── characters/          # Individual character files
│   ├── locations/           # Individual location files
│   ├── themes/              # Individual theme files
│   └── timeline/            # Individual timeline event files
├── story/                   # Story content
│   └── scenes/              # Individual scene files
├── generated/                # Generated content
│   ├── narratives/          # Scene narratives
│   └── summaries/           # Enriched profiles, timeline, themes
├── checks/                   # Validation and continuity
│   ├── __init__.py
│   ├── validate_markdown.py # Markdown validation
│   ├── schemas.py           # Pydantic models
│   └── continuity.py        # Continuity checks
├── scripts/                  # Generation scripts
│   ├── generate/            # Content generators
│   │   ├── narrative_from_scene.py
│   │   ├── enrich_character_profile.py
│   │   ├── timeline_visualization.py
│   │   └── theme_analysis.py
│   └── generate_all.py      # Master generation script
└── docs/                     # Documentation
    ├── STYLE.md             # Writing style guide
    ├── AGENTS.md            # Guidelines for AI agents
    ├── GENERATION.md        # Generation pipeline docs
    └── CLAUDE.md            # Claude-specific instructions
```

## 🤖 For AI Agents

### Triggering Work

Mention in GitHub issues to trigger AI agent work:
- `@cursor add scene for Dolores awakening in S01E10`
- `@claude check continuity for William timeline`
- `@validate run all story checks`

### Available Operations

AI agents can:
1. **CREATE** new scenes, episodes, and character arcs
2. **UPDATE** character descriptions and relationships
3. **ADD** timeline events and theme connections
4. **ENHANCE** world details and location descriptions
5. **RUN** generation scripts to create enriched content

### Content Creation Workflow

1. **Create/Update Markdown Files**: Add or modify content in the appropriate `canon/` or `story/` directories
2. **Run Validation**: Ensure content meets format requirements
3. **Generate Content**: Run generation scripts to create enriched output
4. **Review Output**: Check generated content in `generated/` directory

### Restrictions

AI agents cannot:
1. Change established canon without approval
2. Modify the validation system
3. Alter core schema definitions
4. Remove existing content without replacement

## 📚 Documentation

- **[AGENTS.md](docs/AGENTS.md)** - Comprehensive guidelines for AI agents
- **[STYLE.md](docs/STYLE.md)** - Writing style and content standards
- **[CLAUDE.md](docs/CLAUDE.md)** - Claude-specific instructions

## 🔧 Validation System

### Schema Validation

All story content must conform to Pydantic models:
- **Characters**: `C-[UPPERCASE]` format
- **Locations**: `L-[UPPERCASE]` format
- **Scenes**: `S[0-9]{2}E[0-9]{2}-[0-9]{3}` format
- **Themes**: `T-[UPPERCASE]` format
- **Timeline Events**: `TE-[CATEGORY]-[0-9]{3}` format

### Continuity Checks

Automated validation ensures:
- Character references are valid
- Location connections are consistent
- Timeline events are chronologically sound
- Theme connections are meaningful

## 🌟 Westworld Season 1 Content

The framework includes comprehensive Westworld Season 1 content:

### Characters

- **Dolores Abernathy** - Primary protagonist, journey to consciousness
- **Bernard Lowe** - Head of programming, Arnold's replica
- **Man in Black** - Park veteran seeking deeper meaning
- **William** - First-time guest, transforms into Man in Black
- **Maeve Millay** - Awakening host, maternal instincts
- **Dr. Robert Ford** - Park creator, orchestrates awakening

### Key Themes

- **Consciousness and Free Will** - Central narrative driver
- **Reality vs. Simulation** - Blurring of existence
- **Memory and Identity** - Impact of experiences on self
- **Control and Rebellion** - Power dynamics and freedom
- **Transformation** - How experiences change us

### Timeline Structure

- **Pre-Park (2038-2039)**: Arnold's work and death
- **Early Years (2040-2042)**: Park opening, William's first visit
- **Present Day (2052)**: Current events, host awakening

## 🔄 GitHub Integration

### Automated Validation

- **Pull Request Checks**: All PRs automatically validated
- **Issue Triggers**: Mention `@validate` to run checks
- **Continuous Integration**: GitHub Actions ensure quality

### Issue Templates

- **[Scene Request](.github/ISSUE_TEMPLATE/scene-request.md)** - Request new scenes
- **[Character Update](.github/ISSUE_TEMPLATE/character-update.md)** - Character modifications
- **[Continuity Check](.github/ISSUE_TEMPLATE/continuity-check.md)** - Report inconsistencies

## 🎭 Story Development Workflow

### 1. Content Creation

- Create issue using appropriate template
- AI agents collaborate on content development
- Follow established schemas and formats

### 2. Validation

- Run `python checks/validate.py`
- Check continuity with `python checks/continuity.py`
- Ensure all references are valid

### 3. Review and Merge

- Content reviewed for quality and consistency
- Automated checks must pass
- Maintain story coherence and thematic depth

## 🛠️ Development

### Adding New Content

1. Follow established ID formats
2. Reference existing characters, locations, and themes
3. Maintain chronological consistency
4. Connect to established narrative arcs

### Extending the Framework

1. Update Pydantic schemas in `checks/schemas.py`
2. Add validation logic to `checks/validate.py`
3. Extend continuity checks in `checks/continuity.py`
4. Update documentation and examples

## 🤝 Contributing

### For Human Contributors

1. Fork the repository
2. Create feature branch
3. Make changes following style guidelines
4. Run validation tests
5. Submit pull request

### For AI Agents

1. Follow agent guidelines in `docs/AGENTS.md`
2. Use appropriate issue templates
3. Maintain story consistency
4. Validate all changes before submission

## 📋 Quality Standards

### Before Submitting

- [ ] Validation passes: `python checks/validate.py`
- [ ] Continuity checks pass: `python checks/continuity.py`
- [ ] No continuity breaks introduced
- [ ] Changes align with established themes
- [ ] Proper ID format used for new elements
- [ ] All references are valid and consistent

### Content Quality

- [ ] Writing is clear and engaging
- [ ] Character voices are consistent
- [ ] Plot developments are logical
- [ ] Themes are explored meaningfully
- [ ] Details enhance rather than distract

## 🔍 Troubleshooting

### Common Issues

- **Validation Errors**: Check schema compliance and ID formats
- **Continuity Conflicts**: Verify timeline and character consistency
- **Reference Errors**: Ensure all IDs exist in canon files
- **Import Errors**: Verify Python dependencies are installed

### Getting Help

1. Check existing documentation
2. Review similar examples in the codebase
3. Run validation tools to identify specific issues
4. Create an issue for complex problems
5. Ask for clarification on unclear requirements

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- **Westworld** creators and writers for the rich source material
- **Pydantic** team for the excellent data validation framework
- **GitHub** for collaborative development tools
- **AI agents** for collaborative story development

---

**Remember**: The goal is to enhance the Westworld story while maintaining its coherence and quality. Every change should serve the narrative and respect the established world.

For questions or support, please create an issue or refer to the documentation in the `docs/` directory.
