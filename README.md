# PDDL / PPDDL lexer for Pygments

This is a [(Probabilistic) Planning Domain Definition Language][pddl]
lexer for Pygments. It's useful for rendering (P)PDDL in your
LaTeX documents via the `minted` package.

## Installation
You can install it with:

```bash
pip install git+https://github.com/eldruin/pygments-ppddl-lexer
```

Then just use the `pddl` or `ppddl` aliases when rendering stuff with
Pygments. The parser is really just a hacked-up version of the Pygments'
built-in Scheme lexer, and there's no guarantee it will parse anything well
except for the stuff in my thesis. May still be useful for somebody.

[pddl]: https://en.wikipedia.org/wiki/Planning_Domain_Definition_Language
