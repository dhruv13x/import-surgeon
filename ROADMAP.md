# Strategic Roadmap V3.0

This living document outlines the strategic direction for `import-surgeon`, balancing innovation with stability and technical debt repayment.

---

## 🏁 Phase 0: The Core (Stability & Debt)
**Goal**: Solid foundation. Ensure the codebase is robust, well-tested, and easy to maintain before adding complexity.

- [x] **Testing**: Maintain coverage > 85%. `[Debt]` (Size: S)
- [x] **CI/CD**: Enforce linting (`ruff`/`black`) and strict type checking (`mypy`). `[Debt]` (Size: S)
- [ ] **Documentation**: Comprehensive `README.md` and inline docstrings "Gold Standard". `[Debt]` (Size: M)
- [ ] **Refactoring**: Remove `DummyTqdm` fallback and standardize optional dependencies. `[Debt]` (Size: S)

---

## 🚀 Phase 1: The Standard (Feature Parity)
**Goal**: Competitiveness. Polish the user experience and ensure performance matches market expectations.
**Risk**: Low.

- [x] **UX**: Interactive TUI for migration selection. `[Feat]` (Size: M)
- [ ] **UX**: Enhanced Dry-Run with side-by-side rich diffs. `[Feat]` (Size: M)
- [ ] **Config**: Schema validation for `migrate.yaml` to prevent invalid configs. `[Feat]` (Size: S)
- [ ] **Performance**: Async I/O for file discovery and reading. `[Feat]` (Size: L)
- [ ] **Performance**: Caching of AST parsing results to speed up repeated runs. `[Feat]` (Size: M)

---

## 🔌 Phase 2: The Ecosystem (Integration)
**Goal**: Interoperability. Allow other tools and developers to build on top of `import-surgeon`.
**Risk**: Medium (Requires API design freeze).
**Dependencies**: Requires Phase 1.

- [ ] **API**: Public Python API (`import import_surgeon`) for scriptable refactoring. `[Feat]` (Size: L)
- [ ] **Plugins**: Extension system for custom `Visitor`/`Transformer` logic. `[Feat]` (Size: XL)
- [ ] **Integrations**: Official Pre-Commit Hook and GitHub Action. `[Feat]` (Size: M)

---

## 🔮 Phase 3: The Vision (Innovation)
**Goal**: Market Leader. cutting-edge features that differentiate the product.
**Risk**: High (R&D).
**Dependencies**: Requires Phase 2.

- [ ] **AI**: LLM Integration for "Refactoring Advisor" and architectural suggestions. `[Feat]` (Size: XL)
- [ ] **Cloud**: Docker container and Kubernetes Job definitions for large-scale monorepo migrations. `[Feat]` (Size: M)
- [ ] **Self-Healing**: Automated fix for `ImportError` tracebacks. `[Feat]` (Size: L)
