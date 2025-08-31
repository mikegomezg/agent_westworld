export function generateSceneNarrative(scene, characters, world) {
    const characterMap = Object.fromEntries(
        characters.map(c => [c.id, c])
    );

    const locationMap = Object.fromEntries(
        (world.locations || []).map(l => [l.id, l])
    );

    const location = locationMap[scene.location];
    const sceneCharacters = (scene.characters || []).map(id => characterMap[id]);

    let narrative = `## ${scene.title}\n\n`;
    narrative += `*${location?.description || scene.location}*\n\n`;
    narrative += scene.synopsis + '\n\n';

    if (scene.dialogue && scene.dialogue.length > 0) {
        narrative += '---\n\n';
        scene.dialogue.forEach(line => {
            narrative += `> "${line}"\n\n`;
        });
    }

    if (scene.actions && scene.actions.length > 0) {
        narrative += scene.actions.join(' ');
    }

    return narrative;
}
