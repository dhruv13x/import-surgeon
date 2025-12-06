# 🧠 Import Surgeon Roadmap

This document outlines the strategic vision for `import-surgeon`, categorized into phases from core essentials to ambitious, long-term goals.

---

## Phase 1: Foundation (CRITICALLY MUST HAVE)

**Focus**: Core functionality, stability, security, and basic usage.
**Status**: Q1 2026

- [x] **AST-Based Refactoring Engine**: Core `LibCST` logic for safe, syntax-aware refactoring.
- [x] **Robust CLI**: Argument parsing, logging, and granular verbosity controls.
- [x] **YAML Configuration**: Support for batch migrations via `migrate.yml`.
- [x] **Safety First**: Automatic file backups (`.bak`) and atomic write operations.
- [x] **Git Integration**: Clean repo checks (`--require-clean-git`) and auto-commit.
- [x] **Rollback Capability**: Restore files to previous state using `--rollback`.
- [x] **Code Formatting**: Integration with `black` and `isort` (`--format`).
- [x] **Parallel Processing**: Multiprocessing support to speed up scanning on large monorepos.
- [x] **Advanced Alias Handling**: Support for refactoring symbols accessed via module aliases (e.g., `import old.pkg as o; o.Symbol()`).

---

## Phase 2: The Standard (MUST HAVE)

**Focus**: Feature parity with top competitors, user experience improvements, and robust error handling.
**Status**: Q2 2026

- [ ] **Interactive TUI**: A `rich`-powered interactive mode for selecting symbols and previewing changes before applying.
- [ ] **Symbol Dependency Analysis**: Analyze and warn if moving a symbol will break internal dependencies in the old module.
- [ ] **Enhanced Dry-Run**: Side-by-side rich diffs to visualize changes more clearly than unified diffs.
- [ ] **"Unused Import" Cleanup**: Detect and surgically remove unused imports left behind after moving symbols.
- [ ] **Advanced Pattern Matching**: Support regex or glob patterns for selecting symbols to move (e.g., `User*`).

---

## Phase 3: The Ecosystem (INTEGRATION & SHOULD HAVE)

**Focus**: Webhooks, API exposure, 3rd party plugins, SDK generation, and extensibility.
**Status**: Q3 2026

- [ ] **Public Python API**: stable `import import_surgeon` interface for use in other Python scripts.
- [ ] **Pre-Commit Hook**: Official `.pre-commit-hooks.yaml` for automated cleanup in CI/CD.
- [ ] **IDE Integration**: VSCode and PyCharm extensions wrapping the CLI for "Right-click -> Move Symbol".
- [ ] **GitHub Action**: A marketplace action to automatically propose refactors on PRs.
- [ ] **Plugin System**: Architecture for custom `Visitor`/`Transformer` plugins to handle framework-specific patterns (e.g., Django models).

---

## Phase 4: The Vision (GOD LEVEL)

**Focus**: "Futuristic" features, AI integration, advanced automation, and industry-disrupting capabilities.
**Status**: Q4 2026

- [ ] **AI-Driven Refactoring Advisor**: LLM integration to analyze code and suggest architectural improvements (e.g., "Move these 3 coupled classes to `services.py`").
- [ ] **"Self-Healing" Imports**: A mode that runs on `ImportError` tracebacks to automatically find and fix the missing import.
- [ ] **Architectural Enforcement**: Define "layers" (e.g., `api` -> `services` -> `db`) and forbid imports that violate the hierarchy.
- [ ] **Dependency Graph Visualization**: Generate interactive Mermaid/Dot graphs showing the before/after import structure.

---

## The Sandbox (OUT OF THE BOX / OPTIONAL)

**Focus**: Wild, creative, experimental ideas that set the project apart.

- [ ] **"Time Travel" Refactoring**: Replay git history and apply a refactor to past commits to clean up history.
- [ ] **Gamification**: Leaderboards for "Lines of Code Cleaned" or "Spaghetti Entanglements Removed".
- [ ] **Code Archaeology**: Heatmaps showing which files are most frequently refactored, indicating tech debt hotspots.
