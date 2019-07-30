This is a (P)PDDL lexer for Pygments. It's useful for rendering PPDDL in your
LaTeX documents via the `minted` package. You can install it with `pip install`
& then just use the `pddl` or `ppddl` aliases when rendering stuff with
Pygments. The parser is really just a hacked-up version of the Pygments'
built-in Scheme lexer, and there's no guarantee it will parse anything well
except for the stuff in my thesis. May still be useful for somebody.
