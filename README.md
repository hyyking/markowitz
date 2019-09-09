# PyMarkowitz

## Purpose

## Usage

For this you will need two files:
- A layout file (for now see examples in layouts directory)
- A SQLite database with financial products as single tables with UPPERCASE names and at least the following header: `clot`

You can use this package as a CLI
- `python -m markowitz [LAYOUT] [SQLITE DATABASE]`

Or as library:
- Just like the CLI to integrate in your program
- For financial assets abstractions
- For graphing objects abstractions

You can extend the available graphs by adding them in the `markowitz/graph_objs` directory in lowercase, be sure to subclass the Graph class

### To be done

- Refactor python code
- Add better logging
- Generate documentation
- Split website in two parts: project and documentation
- Add package to pypy
- Add support for other database types
- Add ability to specify other graph obj directory

### Credits

Produced by Léo Duret as part of his annual project for the CMI EFiQuaS.
I'd like to thank Adrien Chaillout my partner on this project.
