  <a href="https://xircuits.io/docs/category/developer-guide">Developer Guides</a> •
  <a href="https://github.com/XpressAI/xircuits/blob/master/CONTRIBUTING.md">Contribute</a> •
  <a href="https://www.xpress.ai/blog/">Blog</a> •
  <a href="https://discord.com/invite/vgEg2ZtxCw">Discord</a>
</p>



<p align="center"><i>Xircuits Component Library for SQLite Database Management! Easily manage SQLite databases and execute SQL queries within workflows.</i></p>

Welcome to the xai-sqlite component library! This library allows you to manage SQLite databases seamlessly within your Xircuits workflows. With xai-sqlite, you can open, execute transactions, and retrieve data from SQLite databases using custom components.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Getting Started with Xai-SQLite](#getting-started-with-xai-sqlite)
- [Try the Examples](#try-the-examples)
  - [Sqlite Sample](#sqlite-sample)
  

## Prerequisites

Before you begin, ensure you have the following:

1. Python 3.8+.
2. Xircuits.

## Installation

To install the SQLite component library, you can use the component library interface or the CLI:

```bash
xircuits install sqlite
```

Or you can install it manually by cloning and setting up the library:

```bash
# base Xircuits directory
git clone https://github.com/XpressAI/xai-sqlite xai_components/xai_sqlite
pip install -r xai_components/xai_sqlite/requirements.txt
```

## Getting Started with Xai-SQLite

This component library provides several components to help you interact with SQLite databases in your Xircuits workflows. Each component is designed to handle specific database operations, making it easy to perform tasks like opening a database connection, executing queries, and fetching data.

## Try the Examples

We've provided an example workflow to help you get started with the xai-sqlite component library. Give it a try and see how you can interact with an SQLite database in a Xircuits workflow.

### Sqlite Sample
Explore the sqlite_sample.xircuits workflow. This example demonstrates basic database operations, including creating a table, inserting records, and fetching data from the SQLite database.

## Contributing

We welcome contributions to the **Sqllite XAI Components Library**! If you would like to contribute:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Open a pull request with a detailed description of your changes.

Please feel free to suggest new components, improvements, or optimizations. If you encounter any issues or have ideas for enhancements, you can open an issue in the repository.

---

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.