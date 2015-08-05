"""
Default styling.
This contains the default style from Pygments, but adds the styling for
prompt-toolkit specific Tokens on top.
"""
from __future__ import unicode_literals
from pygments.styles.default import DefaultStyle as PygmentsDefaultStyle
from pygments.token import Token

__all__ = (
    'default_style_extensions',
    'DefaultStyle',
)


default_style_extensions = {
    # Highlighting of search matches in document.
    Token.SearchMatch:                            '#ffffff bg:#000000',
    Token.SearchMatch.Current:                    '#ffffff bg:#aa4444',

    # Highlighting of select text in document.
    Token.SelectedText:                           '#ffffff bg:#666666',

    # Highlighting of matching brackets.
    Token.MatchingBracket:                        'bg:#aaaaff #000000',

    # Line numbers.
    Token.LineNumber:                             '#888888',

    # Default prompt.
    Token.Prompt:                                 'bold',
    Token.Prompt.Arg:                             'noinherit',
    Token.Prompt.Search:                          'noinherit',
    Token.Prompt.Search.Text:                     'bold',

    # Search toolbar.
    Token.Toolbar.Search:                         '',
    Token.Toolbar.Search.Text:                    'bold',

    # System toolbar
    Token.Toolbar.System.Prefix:                  'bg:#000000 #ffffff bold',

    # "arg" toolbar.
    Token.Toolbar.Arg:                            '',
    Token.Toolbar.Arg.Text:                       'bold',

    # Validation toolbar.
    Token.Toolbar.Validation:                     'bg:#550000 #ffffff',

    # Completions toolbar.
    Token.Toolbar.Completions:                    'bg:#bbbbbb #000000',
    Token.Toolbar.Completions.Arrow:              'bg:#bbbbbb #000000 bold',
    Token.Toolbar.Completions.Completion:         'bg:#bbbbbb #000000',
    Token.Toolbar.Completions.Completion.Current: 'bg:#444444 #ffffff',

    # Completions menu.
    Token.Menu.Completions.Completion:            'bg:#bbbbbb #000000',
    Token.Menu.Completions.Completion.Current:    'bg:#888888 #ffffff',
    Token.Menu.Completions.Meta:                  'bg:#999999 #000000',
    Token.Menu.Completions.Meta.Current:          'bg:#aaaaaa #000000',
    Token.Menu.Completions.ProgressBar:           'bg:#aaaaaa',
    Token.Menu.Completions.ProgressButton:        'bg:#000000',

    # When Control-C has been pressed. Grayed.
    Token.Aborted:                                '#888888',
}


class DefaultStyle(PygmentsDefaultStyle):
    background_color = None
    styles = {}
    styles.update(default_style_extensions)
    styles.update(PygmentsDefaultStyle.styles)
