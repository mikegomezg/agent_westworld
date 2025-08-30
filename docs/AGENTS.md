# Agent Guidelines

## For AI Agents Working on This Repository

### Available Operations

You may:
1. CREATE new scenes in `story/scenes/`
2. UPDATE character descriptions in `canon/characters.yml`
3. ADD timeline events to `canon/timeline.yml`
4. PROPOSE theme connections in scenes
5. CREATE new episode files in `story/episodes/`
6. ADD character arcs in `story/arcs/`
7. UPDATE world details in `canon/world.yml`

You may NOT:
1. Change established canon without explicit approval
2. Modify the validation system
3. Alter character IDs or episode structures
4. Remove existing content without replacement
5. Change the core schema definitions

### Working with Story Elements

#### When creating a scene:
1. Use the template in `story/scenes/TEMPLATE.yml`
2. Reference only existing character IDs from `canon/characters.yml`
3. Ensure location IDs match `canon/world.yml`
4. Run `python checks/validate.py` before committing
5. Follow the scene ID format: `S[0-9]{2}E[0-9]{2}-[0-9]{3}`

#### When updating characters:
1. Preserve all existing fields
2. Add new information under appropriate sections
3. Maintain consistency with established scenes
4. Update relationships if adding new connections
5. Ensure trait additions align with existing character development

#### When adding timeline events:
1. Use the format: `TE-[CATEGORY]-[0-9]{3}`
2. Reference existing character IDs
3. Maintain chronological consistency
4. Link to relevant episodes when possible
5. Ensure significance aligns with established themes

#### When creating episodes:
1. Follow the existing episode structure
2. Include all required fields from the schema
3. Reference existing themes from `canon/themes.yml`
4. List all featured characters and locations
5. Maintain consistency with the overall season arc

### Content Guidelines

#### Character Development:
- Respect established character traits and motivations
- Ensure character actions align with their established nature
- Maintain consistency in relationships and backstories
- Consider how changes affect the overall narrative

#### Story Continuity:
- Check that new content doesn't contradict existing events
- Ensure timeline consistency across all materials
- Verify location and character references are valid
- Maintain the established tone and style

#### Theme Integration:
- Connect new content to existing themes when possible
- Ensure themes are explored consistently across episodes
- Balance thematic development with plot progression
- Consider how themes relate to character development

### Quality Standards

#### Before submitting changes:
- [ ] Validation passes: `python checks/validate.py`
- [ ] Continuity checks pass: `python checks/continuity.py`
- [ ] No continuity breaks introduced
- [ ] Changes align with established themes
- [ ] Proper ID format used for new elements
- [ ] All references are valid and consistent

#### Content quality:
- [ ] Writing is clear and engaging
- [ ] Character voices are consistent
- [ ] Plot developments are logical
- [ ] Themes are explored meaningfully
- [ ] Details enhance rather than distract from the story

### Commit Message Format

```
[CATEGORY] Brief description

- Specific change 1
- Specific change 2

Refs: #issue_number
```

Categories: SCENE, CHARACTER, WORLD, CONTINUITY, FIX, EPISODE, ARC, THEME

### Required Checks

Before opening a PR, ensure:
- [ ] Validation passes: `python checks/validate.py`
- [ ] Continuity checks pass: `python checks/continuity.py`
- [ ] No continuity breaks introduced
- [ ] Changes align with established themes
- [ ] Proper ID format used for new elements
- [ ] Content quality meets standards
- [ ] All references are valid

### Collaboration Guidelines

#### Working with other agents:
- Check recent changes before making modifications
- Coordinate on major story developments
- Respect established character arcs and plotlines
- Communicate about overlapping areas of interest

#### Handling conflicts:
- Prioritize established canon over new ideas
- Seek clarification on unclear situations
- Maintain consistency with the overall vision
- Consider the impact on the entire story

### Emergency Procedures

If you encounter:
- **Validation errors**: Fix schema compliance issues first
- **Continuity conflicts**: Check timeline and character consistency
- **ID conflicts**: Ensure unique identifiers for all new elements
- **Reference errors**: Verify all character and location IDs exist

### Best Practices

1. **Start small**: Make incremental changes rather than large overhauls
2. **Test thoroughly**: Run validation after each significant change
3. **Document decisions**: Add comments explaining complex logic or choices
4. **Maintain consistency**: Ensure all changes align with established patterns
5. **Think long-term**: Consider how changes affect future story development

### Getting Help

If you need assistance:
1. Check existing documentation first
2. Review similar examples in the codebase
3. Run validation tools to identify specific issues
4. Create an issue for complex problems
5. Ask for clarification on unclear requirements

Remember: The goal is to enhance the Westworld story while maintaining its coherence and quality. Every change should serve the narrative and respect the established world.

