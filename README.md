# PyMarkowitz

## Purpose

Provide utility to create visually appealing and customisable graphic representation of markowitz's
modern portfolio theory.

## Usage

For this you will need two files:

- A layout file (for now see examples in layouts directory)
- A SQLite database or a list of csv files (specify with `-l` in the options default is `sqlite`)
  with historical data, specify the header you want to load by providing an argument to `-c`
  (default is `clot`).

You can use this package as a CLI:

```
>> python -m markowitz --help

usage: __main__.py [-h] [-l LOADER] [-c COLUMN] [--debug] [--style STYLE]
                   layout input [input ...]

Display assets and portfolio graphs from layout

positional arguments:
  layout                Layout file path
  input                 Data input file

optional arguments:
  -h, --help            show this help message and exit
  -l LOADER, --loader LOADER
                        loader to use available: [sqlite, csv]
  -c COLUMN, --column COLUMN
                        column name in the file
  --debug               activate debug mode
  --style STYLE         matplotlib graph style
```

Or as individual modules:

- `markowitz/graphs` for graph points generators
- `markowitz/sets` for point generators
- `markowitz/financial` for the assets

## Extending the capabilities

You can extend the available graphs and sets by adding them in the `markowitz/graphs` and
`markowitz/sets` directories.

- **Sets** are mathematical vector space point iterators. To implement one you need to subclass
  `markowitz/sets/abstract.py` which will force you to write a valid point iterator.

- **Graphs** are point iterators that map one set (hence `markowitz/sets`) to a set of points that
  can be graphed. To implement one you need to subclass `markowitz/graphs/abstract.py` which will
  force you to write a `points()` method which is called when generating the graph, make sure to zip
  the coordinates together, eg. `zip(x, y)`. Graphs are loaded dynamically at runtime, use your
  implementation by mentioning the class name in the layout file, and name your implementation file
  the same way but **_lowercase_**. The abstract class holds the default config for a graph, you can
  override this config and the config passed when parsing layout files in your implementation.

- **Loader** holds the state of the assets and how they will be loaded, you can implement you own by
  following the already existing ones.

## To be done

- Add better logging
- Add unittests
- Generate documentation
- Split github.io website in two parts: project and documentation
- Add package to pypy
- Add ability to specify other graph obj directory

## Credits

- This project is licenced under MIT, see `LICENSE.md` for more information.
- Produced by Léo Duret as part of his annual project following the
  [CMI EFiQuaS](cmi-efiquas.u-paris2.fr) curriculum.
