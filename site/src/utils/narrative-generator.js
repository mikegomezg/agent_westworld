export function generateSceneNarrative(scene, characters, world) {
    // Safety checks for required properties
    if (!scene || !scene.title) {
        return "## Scene Error\n\nUnable to generate narrative for this scene.";
    }

    const characterMap = Object.fromEntries(
        characters.map(c => [c.id, c])
    );

    const locationMap = Object.fromEntries(
        (world.locations || []).map(l => [l.id, l])
    );

    // Safely get location, with fallback
    const sceneLocation = scene.location || 'Unknown Location';
    const location = locationMap[sceneLocation];
    const sceneCharacters = (scene.characters || []).map(id => characterMap[id]);

    let narrative = `## ${scene.title}\n\n`;

    // Add location description if available
    if (location && location.description) {
        narrative += `*${location.description}*\n\n`;
    } else {
        narrative += `*${sceneLocation}*\n\n`;
    }

    // Add synopsis if available
    if (scene.synopsis) {
        narrative += scene.synopsis + '\n\n';
    }

    // Add dialogue if available
    if (scene.dialogue && scene.dialogue.length > 0) {
        narrative += '---\n\n';
        scene.dialogue.forEach(line => {
            narrative += `> "${line}"\n\n`;
        });
    }

    // Add actions if available
    if (scene.actions && scene.actions.length > 0) {
        narrative += scene.actions.join(' ');
    }

    return narrative;
}
