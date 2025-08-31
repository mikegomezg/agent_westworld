import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const ROOT_DIR = path.resolve(process.cwd(), '..');

export function loadYaml(filePath) {
    const fullPath = path.join(ROOT_DIR, filePath);
    const fileContents = fs.readFileSync(fullPath, 'utf8');
    return yaml.load(fileContents);
}

export function loadAllCharacters() {
    return loadYaml('canon/characters.yml').characters || [];
}

export function loadAllScenes() {
    const scenesDir = path.join(ROOT_DIR, 'story/scenes');
    const files = fs.readdirSync(scenesDir)
        .filter(f => f.endsWith('.yml') && f !== 'TEMPLATE.yml');

    return files.map(file => {
        const data = loadYaml(`story/scenes/${file}`);
        return { ...data, filename: file };
    });
}

export function loadTimeline() {
    return loadYaml('canon/timeline.yml').events || [];
}

export function loadThemes() {
    return loadYaml('canon/themes.yml').themes || [];
}

export function loadWorld() {
    return loadYaml('canon/world.yml');
}
