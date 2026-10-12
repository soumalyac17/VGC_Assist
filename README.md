# VGC-Assist

**Meta-independent, explainable Pokémon team optimization system.**

VGC-Assist is an independent project exploring how role-based reasoning and constraint-driven optimization can help players build structurally coherent competitive Pokémon teams. The goal is to explain *why* a Pokémon may help a particular team instead of relying primarily on usage statistics or opaque recommendations.

## Status

This is an early public project scaffold. The landing page and planning documents are included; the eight scoring functions, candidate optimizer, and finished team-builder interface are **not implemented yet**. Do not treat placeholder data as validated competitive advice.

## Core functionality planned

- **Build:** evaluate partially completed teams and suggest candidates.
- **Score:** evaluate role coverage, defensive coverage, offensive coverage, speed structure, archetype coherence, win conditions, synergy, and balance/redundancy.
- **Explain:** show why a recommendation helps and what trade-offs it introduces.

## Architecture

```text
Objective Pokémon facts
        ↓
VGC-Assist interpretation layer
 roles · functions · archetype affinities
        ↓
Team-level relationships
        ↓
Eight scoring functions
        ↓
Candidate ranking + explanations
```

## Files

- `index.html`, `style.css`, `script.js`: public project landing page.
- `data/`: Pokémon dataset/schema files.
- `data/interpretation-schema.json`: proposed second-layer field definitions.
- `algorithm/scoring-spec.md`: formulas and implementation requirements.

## The eight planned scores

1. Role Coverage — 15%
2. Defensive Coverage — 12%
3. Offensive Coverage — 12%
4. Speed Structure — 12%
5. Archetype Coherence — 12%
6. Win Conditions — 12%
7. Pokémon Synergy — 15%
8. Balance / Redundancy — 10%

These are initial design weights, not empirically validated constants.

## Run locally

Open `index.html` in a browser. No build tools are required for the landing page.

## Publish with GitHub Pages

1. Create a GitHub repository, for example `VGC-Assist`.
2. Upload the contents of this folder to the repository root.
3. Open **Settings → Pages**.
4. Under build/deployment, select **Deploy from a branch**, choose `main` and `/ (root)`, then save.
5. Use the URL GitHub Pages displays after deployment completes.

## Data design principle

Keep **objective facts** (types, stats, abilities, type matchups) separate from **interpretation** (role strengths, functional attributes, archetype affinities). Format legality is format-dependent and should be represented separately. Interpretations are design judgments and need documented rules and review status.

## Roadmap

- [x] Define the project and initial architecture
- [x] Create public landing page and scoring specification
- [ ] Review interpretation tags and data for all supported Pokémon
- [ ] Implement and unit-test the eight scoring functions
- [ ] Implement candidate evaluation and explanations
- [ ] Build the interactive team builder
- [ ] Test with manually reviewed example teams

**Project principle: Complex reasoning, simple presentation.**
