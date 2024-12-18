<p align="center">
  <a href="https://github.com/XpressAI/xircuits/tree/master/xai_components#xircuits-component-library-list">Component Libraries</a> •
  <a href="https://github.com/XpressAI/xircuits/tree/master/project-templates#xircuits-project-templates-list">Project Templates</a>
  <br>
  <a href="https://xircuits.io/">Docs</a> •
  <a href="https://xircuits.io/docs/Installation">Install</a> •
  <a href="https://xircuits.io/docs/category/tutorials">Tutorials</a> •
  <a href="https://xircuits.io/docs/category/developer-guide">Developer Guides</a> •
  <a href="https://github.com/XpressAI/xircuits/blob/master/CONTRIBUTING.md">Contribute</a> •
  <a href="https://www.xpress.ai/blog/">Blog</a> •
  <a href="https://discord.com/invite/vgEg2ZtxCw">Discord</a>
</p>





<p align="center"><i>Xircuits Component Library for SQLite – Simplify database operations within your workflows.</i></p>

---
## Xircuits Component Library for SQLite

This library enables seamless integration of SQLite database operations into Xircuits workflows. It supports tasks like database connection management, executing SQL queries, and retrieving or manipulating data.

## Table of Contents

- [Preview](#preview)
- [Prerequisites](#prerequisites)
- [Main Xircuits Components](#main-xircuits-components)
- [Try the Examples](#try-the-examples)
- [Installation](#installation)

## Preview

### The Example:

<img src="https://github.com/user-attachments/assets/80ed1f2f-8f9a-4d06-9b56-93b567e6631b" alt="sqlite_sample"  />

### The Result:

<img src="https://github.com/user-attachments/assets/65320dfe-d89f-4875-8186-1eb9ee712c5f" alt="sqlite_sample_result" />

## Prerequisites

Before you begin, you will need the following:

1. Python3.9+.
2. Xircuits.

## Main Xircuits Components

### SqliteOpenDB Component:
Establishes a connection to the SQLite database file, making it accessible for query execution.

<img src="https://github.com/user-attachments/assets/fb2e01d8-3e19-41d9-849f-79d6f07821de" alt="SqliteOpenDB" width="200" height="75" />

### SqliteFetchOne Component:
Executes a query and retrieves a single row from the database result set as a dictionary.

<img src="https://github.com/user-attachments/assets/1e3c2a7f-673a-4f33-ab6f-54ac1c4ebec6" alt="SqliteFetchOne" width="200" height="100" />

### SqliteFetchAll Component:
Executes a query and retrieves all rows from the database result set, returning them as a list of dictionaries.

### SqliteWithTransaction Component:
Executes multiple SQLite operations within a transaction, ensuring all operations are committed or rolled back.

### SqliteExecute Component:
Executes a single SQL query, with optional arguments, on the connected SQLite database.

### SqliteExecuteScript Component:
Runs an SQL script from a file on the SQLite database, enabling batch query execution.

## Try the Examples

We've provided an example workflow to help you get started with the SQLite component library. Give it a try and see how you can interact with an SQLite database in a Xircuits workflow.

### Sqlite Sample
This example demonstrates basic database operations, including creating a table, inserting records, and fetching data from the SQLite database.

## Installation

To install the SQLite component library, you can use the component library interface or the CLI:

```bash
xircuits install sqlite
```

Or you can install it manually by cloning and setting up the library:

```bash
# base Xircuits directory
git clone https://github.com/XpressAI/xai-sqlite xai_components/xai_sqlite
```



