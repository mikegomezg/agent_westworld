import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';

const ROOT_DIR = path.resolve(process.cwd(), '..');

export function loadYaml(filePath) {
    try {
        const fullPath = path.join(ROOT_DIR, filePath);
        if (!fs.existsSync(fullPath)) {
            console.warn(`File not found: ${fullPath}`);
            return {};
        }
        const fileContents = fs.readFileSync(fullPath, 'utf8');
        return yaml.load(fileContents) || {};
    } catch (error) {
        console.error(`Error loading YAML file ${filePath}:`, error);
        return {};
    }
}

export function loadAllCharacters() {
    try {
        const data = loadYaml('canon/characters.yml');
        const characters = data.characters || [];

        // Ensure all characters have required properties and relationships are arrays
        return characters.map(character => ({
            id: character.id || 'unknown',
            name: character.name || 'Unknown Character',
            role: character.role || 'Unknown Role',
            description: character.description || 'No description available.',
            relationships: Array.isArray(character.relationships) ? character.relationships : [],
            ...character
        }));
    } catch (error) {
        console.error('Error loading characters:', error);
        return [];
    }
}

export function loadAllScenes() {
    try {
        const scenesDir = path.join(ROOT_DIR, 'story/scenes');
        if (!fs.existsSync(scenesDir)) {
            console.warn(`Scenes directory not found: ${scenesDir}`);
            return [];
        }

        const files = fs.readdirSync(scenesDir)
            .filter(f => f.endsWith('.yml') && f !== 'TEMPLATE.yml');

        const scenes = files.map(file => {
            try {
                const data = loadYaml(`story/scenes/${file}`);
                // Ensure required fields exist
                if (!data.id) {
                    console.warn(`Scene file ${file} missing id field`);
                    data.id = file.replace('.yml', '');
                }
                return { ...data, filename: file };
            } catch (error) {
                console.error(`Error loading scene ${file}:`, error);
                return { id: file.replace('.yml', ''), title: 'Error Loading Scene', filename: file };
            }
        });

        return scenes;
    } catch (error) {
        console.error('Error loading scenes:', error);
        return [];
    }
}

export function loadTimeline() {
    try {
        const data = loadYaml('canon/timeline.yml');
        return data.events || [];
    } catch (error) {
        console.error('Error loading timeline:', error);
        return [];
    }
}

export function loadThemes() {
    try {
        const data = loadYaml('canon/themes.yml');
        return data.themes || [];
    } catch (error) {
        console.error('Error loading themes:', error);
        return [];
    }
}

export function loadWorld() {
    try {
        const data = loadYaml('canon/world.yml');
        return data || {};
    } catch (error) {
        console.error('Error loading world:', error);
        return {};
    }
}
