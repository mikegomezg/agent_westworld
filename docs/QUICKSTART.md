# Quick Start Guide

## Get Up and Running in 5 Minutes

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Validate Your Story

```bash
python checks/validate.py
```

### 3. Check Continuity

```bash
python checks/continuity.py
```

### 4. Create Your First Scene

1. Copy `story/scenes/TEMPLATE.yml`
2. Fill in the details
3. Run validation again

## What You Can Do Right Now

### ✅ Already Working

- **Character validation** - All 11 main characters validated
- **Location validation** - 9 key locations validated  
- **Episode structure** - S01E01 fully documented
- **Timeline events** - 25 key events documented
- **Theme system** - 12 core themes defined
- **Validation system** - Automated checks working
- **Continuity checking** - Reference validation working

### 🚀 Ready to Use

- **Scene creation** - Template and example provided
- **Character development** - Add traits, relationships, goals
- **Timeline expansion** - Add new events and connections
- **Theme exploration** - Connect content to established themes

## Example: Add a New Scene

1. **Copy the template:**
```bash
cp story/scenes/TEMPLATE.yml story/scenes/my_new_scene.yml
```

2. **Edit the scene file:**
```yaml
id: S01E01-011
episode: S01E01
title: "My New Scene"
location: L-SWEETWATER
characters: ["C-DOLORES", "C-TEDDY"]
synopsis: "Description of what happens..."
themes: ["T-CONSCIOUSNESS"]
```

3. **Validate your work:**
```bash
python checks/validate.py
```

## Key Commands

| Command | Purpose |
|---------|---------|
| `python checks/validate.py` | Validate all story content |
| `python checks/continuity.py` | Check for continuity issues |
| `python checks/validate.py --strict` | Treat warnings as errors |

## Next Steps

1. **Explore the canon** - Check out `canon/` directory
2. **Read the docs** - Start with `docs/AGENTS.md`
3. **Create content** - Use the templates and examples
4. **Join the community** - Use GitHub issues for collaboration

## Need Help?

- **Documentation**: Check `docs/` directory
- **Examples**: Look at existing files in `story/` and `canon/`
- **Issues**: Create GitHub issues for problems or requests
- **Validation**: Run the check tools to identify specific issues

---

**You're all set!** The framework is ready to use and all systems are working. Start creating content and let the AI agents help you build an amazing story.
