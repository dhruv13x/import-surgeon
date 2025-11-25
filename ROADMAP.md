# 🧠 Import Surgeon Roadmap

This document outlines the strategic vision for `import-surgeon`, categorized into phases from core essentials to ambitious, long-term goals.

---

## Phase 1: Foundation (Q1 2026)

**Focus**: Core functionality, stability, security, and basic usage.

- [x] **AST-Based Refactoring**: Core engine for safe, syntax-aware import refactoring.
- [x] **Command-Line Interface**: Robust CLI for performing refactoring operations.
- [x] **Configuration Files**: Support for YAML-based configuration for batch processing.
- [x] **File Backups**: Automatic backups of modified files to prevent data loss.
- [x] **Git Integration**: Options to ensure a clean working directory and to auto-commit changes.
- [ ] **Enhanced Error Handling**: More granular error messages and suggestions for common issues.
- [ ] **Improved Performance**: Optimize file scanning and processing for large codebases.

---

## Phase 2: The Standard (Q2 2026)

**Focus**: Feature parity with top competitors, user experience improvements, and robust error handling.

- [ ] **Interactive Mode**: An interactive TUI for selecting symbols and previewing changes.
- [ ] **Symbol Dependency Analysis**: Warn users when moving a symbol that other symbols depend on.
- [ ] **Dry-Run Enhancements**: An improved dry-run mode with more detailed output and a clearer diff format.
- [ ] **Broader Python Version Support**: Ensure compatibility with the latest Python versions.

---

## Phase 3: The Ecosystem (Q3 2026)

**Focus**: Webhooks, API exposure, 3rd party plugins, SDK generation, and extensibility.

- [ ] **IDE Integration**: Plugins for VSCode and PyCharm to run `import-surgeon` from within the editor.
- [ ] **Pre-Commit Hook**: A pre-commit hook to automate import refactoring during development.
- [ ] **Public API**: Expose a public API to allow other tools to programmatically use `import-surgeon`.
- [ ] **Plugin Architecture**: A plugin system to allow for custom refactoring rules and integrations.

---

## Phase 4: The Vision (Q4 2026)

**Focus**: "Futuristic" features, AI integration, advanced automation, and industry-disrupting capabilities.

- [ ] **AI-Powered Suggestions**: Use AI to suggest refactoring opportunities and to predict potential issues.
- [ ] **Automated Code Modernization**: Automatically update code to use new language features and best practices.
- [ ] **Cross-Language Support**: Extend `import-surgeon` to support other languages, such as JavaScript or Go.
- [ ] **Integration with Static Analysis Tools**: Integrate with tools like SonarQube to provide a more holistic view of code quality.

---

## The Sandbox (Ongoing)

**Focus**: Wild, creative, experimental ideas that set the project apart.

- [ ] **Visual Refactoring**: A graphical interface for visualizing code dependencies and for performing drag-and-drop refactoring.
- [ ] **Gamification**: A system of achievements and rewards for improving code quality.
- [ ] **Code Archaeology**: Tools for analyzing the history of a codebase to identify refactoring opportunities.
