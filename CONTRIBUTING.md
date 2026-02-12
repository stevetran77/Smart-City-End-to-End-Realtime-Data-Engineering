# Git Branching Convention

This document outlines the naming conventions and workflow for Git branches in this project. Following these rules ensures a clean history, easy tracking of features, and better collaboration.

## 1. Branch Naming Structure
All branches (except permanent ones) must follow this pattern:
`[category]/[short-description]`

- **category**: The type of change being made (see list below).
- **short-description**: 2-4 words in lowercase, separated by hyphens.

---

## 2. Branch Categories

| Prefix | Purpose | Example |
| :--- | :--- | :--- |
| `feat/` | New features, pipelines, or data models. | `feat/add-spark-job` |
| `fix/` | Bug fixes in code or logic. | `fix/fix-null-values` |
| `infra/` | Changes to Docker, Airflow, or Cloud Infra. | `infra/update-kafka-ram` |
| `refactor/` | Code optimization without changing logic. | `refactor/clean-joins` |
| `data/` | Backfilling, migrations, or data cleanup. | `data/backfill-2023` |
| `docs/` | Documentation, README, or Wiki updates. | `docs/update-erd` |
| `hotfix/` | Urgent production fixes. | `hotfix/prod-auth-crash` |

---

## 3. Permanent Branches

- **`main`**: Contains production-ready code. Commits are only made via Pull Requests from `develop` or `hotfix`.
- **`develop`**: The main integration branch for active development.



---

## 4. Best Practices

1.  **Lowercase Only**: Use `feat/` instead of `Feat/`.
2.  **Kebab-case**: Use hyphens (`-`) for descriptions, never spaces or underscores.
3.  **Delete After Merge**: Feature and fix branches should be deleted locally and remotely once merged.
4.  **No Personal Names**: Avoid naming branches after yourself (e.g., `hoang/my-fix`). Use the category prefix instead.

---

## 5. Typical Workflow

1. **Update local develop**: 
   `git checkout develop && git pull origin develop`
2. **Create new branch**: 
   `git checkout -b feat/setup-kafka-sink`
3. **Commit changes**: 
   `git commit -m "feat: implement kafka sink for sales data"`
4. **Push to remote**: 
   `git push origin feat/DE-100-setup-kafka-sink`
5. **Create Pull Request**: Merge `feat/DE-100-setup-kafka-sink` into `develop`.