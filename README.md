# VGC-Assist

**An explainable, meta-independent Pokémon team optimization system.**

VGC-Assist is an independent project designed to help new players learn competitive Pokémon team-building while building teams around Pokémon they enjoy. Rather than relying primarily on usage statistics or simply recommending popular choices, it uses role-based reasoning, team synergy, and constraint-driven optimization to help players build more cohesive teams around their favorites and develop strategies to compete more effectively.

Beyond recommending Pokémon, VGC-Assist explains how each addition contributes to a team, helping players understand competitive strategies, recognize weaknesses, and make more informed team-building decisions independently.

## Features

The interactive Base44 prototype includes:

- **Team Builder:** Select up to six Pokémon, view their sprites, types, stats, and abilities, and modify individual team slots.
- **Team Optimization:** Fill empty team slots with recommended Pokémon.
- **Team Evaluation:** Generate an overall team score and category-level evaluations.
- **Type Coverage:** Examine offensive and defensive type matchups.
- **Speed Analysis:** Evaluate speed tiers and speed-control options.
- **Role and Synergy Analysis:** Examine role distribution, physical and special balance, and compatibility between teammates.
- **Archetype Analysis:** Evaluate how well a team supports strategies such as Balance, Hyper Offense, and Trick Room.
- **Threat Coverage:** Assess how well the team can address opposing threats.
- **Recommendations:** Explain suggested additions and their contributions to team structure.
- **Reference Charts:** Access type-effectiveness and Pokémon nature charts.
- **Team Import:** Import an existing team for evaluation and further development.

## How It Works

VGC-Assist separates objective Pokémon data from the competitive interpretations used to evaluate teams.

1. **Objective Data:** Pokémon types, base stats, abilities, and type matchups.
2. **Interpretation Layer:** Assigns role strengths, functional attributes, and archetype affinities.
3. **Team Analysis:** Evaluates individual Pokémon and relationships across the team.
4. **Optimization:** Ranks potential additions based on their contributions to the existing team.
5. **Explanations:** Presents the reasoning behind recommendations and identifies remaining weaknesses.

## Scoring Framework

The prototype uses eight categories to evaluate team structure:

- Type Coverage
- Defensive Synergy
- Speed Control
- Role Balance
- Physical/Special Balance
- Archetype Coherence
- Threat Coverage
- Core Synergy

The scoring framework is being refined as the underlying interpretation and optimization systems develop. The overall score represents structural team evaluation, not a prediction of battle outcomes.

## Data

The project uses an objective dataset covering 1,025 Pokémon species, including their types, base stats, abilities, and defensive type matchups.

Competitive interpretations, including roles and archetype affinities, are maintained separately from objective data. This distinction allows the system's reasoning to remain transparent and its classifications to be reviewed independently.

Format legality is handled separately because restrictions vary across competitive formats and regulations.

## Current Development

- Established the objective Pokémon dataset.
- Designed the interpretation schema for roles, functional attributes, and archetypes.
- Developed the initial scoring framework.
- Built a functional interactive team-builder prototype in Base44, including team selection, optimization, evaluation, reference charts, and team import.
- Created the GitHub project landing page and algorithm documentation.

The next stage is to complete the competitive interpretation layer, implement and validate the scoring functions, and integrate the optimization engine with the interactive interface.

## Repository Structure

- `index.html`, `style.css`, `script.js` — GitHub project landing page.
- `data/` — Pokémon dataset and interpretation schema.
- `algorithm/scoring-spec.md` — Scoring framework, formulas, and implementation specifications.

## Roadmap

- [x] Establish the project architecture and objective dataset.
- [x] Build the public landing page and algorithm specification.
- [x] Develop the interactive Base44 prototype.
- [ ] Complete and review Pokémon role and archetype classifications.
- [ ] Implement and test the scoring functions.
- [ ] Develop and validate the recommendation engine.
- [ ] Integrate the optimization engine with the interactive interface.
- [ ] Evaluate results using manually reviewed teams.

**Project Principle: Complex reasoning, simple presentation.**
