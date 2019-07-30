"""PPDDL lexer for Pygments. Adapted from Scheme lexer in the main
distribution."""

import re

from pygments.lexer import RegexLexer
from pygments.token import Text, Comment, Operator, Keyword, Name, String, \
    Number, Punctuation

__all__ = ['PPDDLLexer']


class PPDDLLexer(RegexLexer):
    """
    A PDDL lexer which also highlights probabilistic (PPDDL) stuff.
    """
    name = 'PPDDL'
    aliases = ['ppddl', 'pddl']
    filenames = ['*.ppddl', '*.pddl']
    mimetypes = ['text/x-ppddl', 'application/x-ppddl']

    keywords = ('define', 'problem', 'domain')
    # next few get highlighted as attributes
    colon_keywords = (
        ':parameters', ':constants', ':predicates', ':types', ':requirements',
        ':objects', ':goal', ':init', ':action', ':precondition', ':effect',
        ':domain',
        # ':typing', ':strips', ':probabilistic-effects',
        # ':conditional-effects', ':negative-preconditions',
        # ':disjunctive-preconditions'
    )
    type_list_keywords = (':objects', ':constants', ':parameters')
    operators = ('*', '+', '-', '/', '<', '<=', '=', '>', '>=')
    word_operators = ('and', 'or', 'not', 'probabilistic', 'forall', 'exists',
                      'when')

    # valid names for identifiers
    # (cannot consist only of dash)
    valid_name = r'[\w!$%&*+,/:<=>?@^~|][\w!$%&*+,/:<=>?@^~|-]+'

    tokens = {
        'root': [
            # line comment
            (r';.*$', Comment.Single),

            # whitespace ignored
            (r'\s+', Text),

            # numbers
            (r'-?\d+\.\d+', Number.Float),
            (r'-?\d+/\d+', Number.Float),
            (r'-?\d+', Number.Integer),

            # strings, symbols and characters
            (r'"(\\\\|\\"|[^"])*"', String),

            # typed lists of things
            (r':types\b', Keyword.Declaration, 'type-list'),
            (r'(%s)\b' % '|'.join(
                re.escape(entry)
                for entry in type_list_keywords),
             Keyword.Declaration,
             'typed-term-list'),
            (r':predicates\b', Keyword.Declaration, 'predicate-list'),

            # keywords/reserved words
            ('(%s)' % '|'.join(re.escape(entry) + r'\b'
                               for entry in keywords), Keyword),
            ('(%s)' % '|'.join(re.escape(entry) + r'\b'
                               for entry in colon_keywords),
             Keyword.Declaration),

            # highlight the symbol and word operators
            (r"(?<=\()(%s)" % '|'.join(
                re.escape(entry) + r'(?=($|\s))' for entry in operators),
             Operator),
            (r"(?<=\()(%s)" % '|'.join(
                re.escape(entry) + r'(?=($|\s))'
                for entry in word_operators), Operator.Word),

            # the remaining functions
            (r'(?<=\()' + valid_name, Name.Function),
            # find the remaining variables
            (valid_name, Name.Variable),

            # the famous parentheses!
            (r'(\(|\))', Punctuation),

            # implicit reward fluent
            (r'reward', Name.Builtin.Pseudo),
        ],
        'predicate-list': [
            # whitespace, line comments
            (r'\s+', Text),
            (r';.*$', Comment.Single),
            # everything else
            (r'\(', Punctuation),
            (r'(?<=\()' + valid_name, Name.Function, 'typed-term-list'),
            (r'\)', Punctuation, '#pop')
        ],
        'type-list': [  # yapf: disable
            # whitespace, line comments
            (r'\s+', Text),
            (r';.*$', Comment.Single),
            # everything else
            (r'\(', Punctuation),
            (r'-', Punctuation),
            (valid_name, Name.Class),
            (r'\)', Punctuation, '#pop')
        ],  # yapf: enable
        'typed-term-list': [
            # whitespace, line comments
            (r'\s+', Text),
            (r';.*$', Comment.Single),
            # everything else
            (r'\(', Punctuation),
            (valid_name, Name.Variable),
            # highlight type names differently
            (r'-', Punctuation, 'type'),
            (r'\)', Punctuation, '#pop')
        ],
        'type': [
            # whitespace, line comments
            (r'\s+', Text),
            (r';.*$', Comment.Single),
            # everything else
            (valid_name, Name.Class, '#pop'),
        ]
    }
