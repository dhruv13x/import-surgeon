<div align="center">
  <img src="https://raw.githubusercontent.com/dhruv13x/import-surgeon/main/import-surgeon_logo.png" alt="import-surgeon logo" width="200"/>
</div>

<div align="center">

<!-- Package Info -->
[![PyPI version](https://img.shields.io/pypi/v/import-surgeon.svg)](https://pypi.org/project/import-surgeon/)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
![Wheel](https://img.shields.io/pypi/wheel/import-surgeon.svg)
[![Release](https://img.shields.io/badge/release-PyPI-blue)](https://pypi.org/project/import-surgeon/)

<!-- Build & Quality -->
[![Build status](https://github.com/dhruv13x/import-surgeon/actions/workflows/publish.yml/badge.svg)](https://github.com/dhruv13x/import-surgeon/actions/workflows/publish.yml)
[![Codecov](https://codecov.io/gh/dhruv13x/import-surgeon/graph/badge.svg)](https://codecov.io/gh/dhruv13x/import-surgeon)
[![Test Coverage](https://img.shields.io/badge/coverage-90%25%2B-brightgreen.svg)](https://github.com/dhruv13x/import-surgeon/actions/workflows/test.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/badge/linting-ruff-yellow.svg)](https://github.com/astral-sh/ruff)
![Security](https://img.shields.io/badge/security-CodeQL-blue.svg)

<!-- Usage -->
![Downloads](https://img.shields.io/pypi/dm/import-surgeon.svg)
![OS](https://img.shields.io/badge/os-Linux%20%7C%20macOS%20%7C%20Windows-blue.svg)
[![Python Versions](https://img.shields.io/pypi/pyversions/import-surgeon.svg)](https://pypi.org/project/import-surgeon/)

<!-- License -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

</div>

---

# import-surgeon 🩺⚙️

**Precision Python import refactoring — safe, atomic, AST-exact, rollback-friendly.**

---

## 🧠 Overview

`import-surgeon` is an **Elite import refactoring engine** for Python codebases.

It precisely updates imports and moves symbols across modules without breaking your code, using full **LibCST AST guarantees**, backup files, atomic writes, and optional auto-formatting.

> **Think of it as:**
> `libcst` + `git-protection` + `atomic rollback-safe refactor surgery`

### Use it for:
*   ✅ **Package restructures**
*   ✅ **Module renames**
*   ✅ **Moving functions/classes between files**
*   ✅ **Gradual API migrations**
*   ✅ **Org-wide import cleanup**
*   ✅ **CI-safe automated refactors**

No regex. No AST guessing. No broken imports.

---

## 🚀 Quick Start

### Prerequisites
*   Python 3.8+
*   Powered by `libcst`, `rich`, `tqdm`, `pyyaml`, `regex`, `black`, `isort`.

### Installation

```bash
pip install import-surgeon
```

> **Optional:** For improved encoding detection:
> ```bash
> pip install chardet
> ```

### Usage Example

**1. Basic dry-run (default)**
```bash
import-surgeon --old-module utils --new-module core.utils --symbols load,save
```

**2. Apply changes**
```bash
import-surgeon --old-module old.pkg --new-module new.pkg --symbols Foo,Bar --apply
```

**3. Rewrite dotted usages too**
```bash
import-surgeon --apply --rewrite-dotted \
  --old-module old.mod --new-module new.mod --symbols Client
```

---

## ✨ Key Features

*   **Accurate import rewrites**: LibCST powered symbol movement (AST-exact).
*   **Dotted name rewrites**: `old.module.Foo` → `new.module.Foo` if `--rewrite-dotted`.
*   **Advanced Alias Handling**: Updates usages like `import old.pkg as o; o.Symbol()` → `new.pkg.Symbol()`.
*   **Atomic file updates**: Guaranteed atomic writes + metadata restore.
*   **Auto backup & rollback**: `--no-backup` optional; `--rollback` supported.
*   **Supports aliases**: `from A import Foo as Bar` handled correctly.
*   **Respects relative imports**: `--force-relative` + auto `base-package` detection.
*   **Batch migrations**: YAML config for multi-module migrations.
*   **Safe in CI**: `--require-clean-git` to prevent dirty changes.
*   **Git auto-commit**: `--auto-commit "msg"`.
*   **Optional format**: `black` + `isort` applied after changes (`--format`).
*   **Warnings for risky spots**: Wildcards, dotted patterns, skipped relative imports.
*   **Progress bar**: `tqdm` fallback built-in.
*   **Parallel Processing**: Multiprocessing support via `--jobs N`.

---

## ⚙️ Configuration & Advanced Usage

### YAML Migration File (`migrate.yml`)

```yaml
migrations:
  - old_module: old.auth
    new_module: services.auth
    symbols: [User, Token]
```

Run with config:
```bash
import-surgeon --config migrate.yml --apply
```

### Rollback a Refactor

```bash
import-surgeon --rollback --summary-json summary.json
```

### CLI Arguments

| Flag | Description | Default |
| :--- | :--- | :--- |
| `target` | The target file or directory to scan. | `.` |
| `--old-module` | The fully qualified module path to move symbols from. | **Required**¹ |
| `--new-module` | The fully qualified module path to move symbols to. | **Required**¹ |
| `--symbols` | A comma-separated list of symbols to move. | **Required**¹ |
| `--apply` | Apply changes to files instead of showing a dry-run. | `False` |
| `--config` | Path to a YAML file for batch migrations. | `None` |
| `--rewrite-dotted` | Rewrite direct `module.symbol` usages in code. | `False` |
| `--format` | Apply `black` and `isort` formatting after changes. | `False` |
| `--rollback` | Roll back a previous migration using a summary file. | `False` |
| `--summary-json` | Path to write a JSON summary of all changes. | `None` |
| `--auto-commit` | Git commit message to auto-commit changes. | `None` |
| `--require-clean-git` | Abort if the Git repository has uncommitted changes. | `False` |
| `--no-backup` | Disable creation of `.bak` files for changed modules. | `False` |
| `--base-package` | Specify the base package for resolving relative imports. | Auto-detected |
| `--force-relative` | Force the use of relative imports where possible. | `False` |
| `--exclude` | Comma-separated glob patterns to exclude from scan. | `None` |
| `--max-files` | Maximum number of files to scan. | `10000` |
| `--strict-warnings` | Exit with a non-zero code if any warnings occur. | `False` |
| `--quiet` | Set the logging level (`none`, `errors`, `all`). | `none` |
| `-v, --verbose` | Increase logging verbosity. | `0` |
| `--version` | Show the program's version number and exit. | N/A |
| `--jobs`, `-j` | Number of parallel jobs for processing files. | `1` |
| `--symbol` | **Deprecated** alias for `--symbols`. | `None` |

¹ Required if not using a `--config` file.

### Exit Codes

*   `0`: Success
*   `1`: Changes had errors
*   `2`: CLI/config error

---

## 🏗️ Architecture

The core logic resides in the `src/import_surgeon/` directory.

```
src/import_surgeon/
├── cli.py             # Main CLI entry point and argument parsing
├── banner.py          # ASCII art banner
└── modules/           # Core logic modules
    ├── __init__.py
    ├── analysis.py    # AST analysis and symbol detection
    ├── config.py      # YAML configuration loading
    ├── cst_utils.py   # LibCST helper functions
    ├── encoding.py    # File encoding detection
    ├── file_ops.py    # File read/write operations
    ├── git_ops.py     # Git repository interactions
    └── process.py     # Main file processing and orchestration
```

The tool works by parsing Python files into an Abstract Syntax Tree (AST) using `LibCST`, identifying import statements, and then surgically replacing them based on the migration rules. It ensures safety through backups, atomic writes, and optional Git integration.

---

## 🗺️ Roadmap

### Phase 1: Foundation (Current)
*   ✅ AST-Based Refactoring
*   ✅ Robust CLI & Configuration Files
*   ✅ File Backups & Git Integration

### Phase 2: The Standard
*   Interactive TUI for selecting symbols.
*   Symbol Dependency Analysis warning system.
*   Broader Python Version Support.

### Phase 3: The Ecosystem
*   IDE Integration (VSCode / PyCharm plugins).
*   Pre-Commit Hook automation.
*   Public API for programmatic use.

### Phase 4: The Vision
*   AI-Powered Refactoring Suggestions.
*   Automated Code Modernization.
*   Cross-Language Support.

---

## 🤝 Contributing & License

**PRs welcome!** We are looking for help with:
*   Editor plugins
*   Safety analyzers
*   Batch migration assistants

**License**: [MIT](https://opensource.org/licenses/MIT) — commercial and open use welcome.

---

## ⭐ Support

Star the repo — every ⭐ funds more time for DevTools research 🙏

[https://github.com/dhruv13x/import-surgeon](https://github.com/dhruv13x/import-surgeon)

---

> 🩺 **Your imports deserve precision surgery — not blind search-replace.**
> **Run `import-surgeon` and refactor with confidence.**
