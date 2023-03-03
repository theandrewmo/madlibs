"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

story1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

story2 = Story(
    ["adjective", "noun", "adjective", "verb_past_tense", "plural_noun", 'adjective', 'verb'],
    """
    Once upon a time, a {adjective} {noun} went on a {adjective} 
    adventure and {verb_past_tense} many {plural_noun}. They were 
    very {adjective} and couldn't wait to {verb} again. The end.
    """
)

story3 = Story(
    ["adjective", "noun", "adjective", "animal", "verb", "adjective", "noun", "verb", "verb_past_tense", "plural_noun"],
    """
    In a {adjective} {noun}, there lived a {adjective} {animal} 
    who loved to {verb}. One day, they met a {adjective} {noun} 
    who needed their help to {verb}. Together, they {verb_past_tense} 
    and saved the day. From then on, they became the best of {plural_noun}.
    """
)

stories = [story1, story2, story3]
