# PyMarkowitz

## Purpose

Provide utility to create visually appealing and customisable graphic representation of markowitz's
modern portfolio theory.

## Usage

For this you will need two files:

- A layout file (for now see examples in layouts directory)
- A SQLite database with financial products as single tables with UPPERCASE names and at least the
  following header: `clot`

You can use this package as a CLI

- `python -m markowitz [LAYOUT] [SQLITE DATABASE]`

Or as library:

- Just like the CLI to integrate in your program
- For financial assets abstractions
- For graphing objects abstractions

## Extending the capabilities 

You can extend the available graphs and sets by adding them in the `markowitz/graphs` and `markowitz/sets` directories.
- **Sets** are mathematical vector space point iterators. To implement one you need to subclass `markowitz/sets/abstract.py` which will force you to write an iterator and implement `.gen()` and `.map(func, *args, **kwargs)`

- **Graphs** are point iterators that map one set (hence `markowitz/sets`) to a set of points that can be graphed. To implement one you need to subclass `markowitz/graphs/abstract.py` which will force you to write a `points()` method which is called when generating the graph, make sure to zip the coordinates together, eg. `zip(x, y)`. Graphs are loaded dynamically at runtime, use your implementation by mentioning the class name in the layout file, and name your implementation file the same way but ***lowercase***. The abstract class holds the default config for a graph, you can override this config and the config passed when parsing layout files in your implementation.

## To be done

- Refactor python code (only structs left)
- Add better logging
- Generate documentation
- Split website in two parts: project and documentation
- Add package to pypy
- Add support for other database types
- Add ability to specify other graph obj directory

## Credits

Produced by Léo Duret as part of his university annual project following the CMI EFiQuaS curriculum.

I'd like to thank Adrien Chaillout my partner on this project.
