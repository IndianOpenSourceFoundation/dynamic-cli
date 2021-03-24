from rich.markdown import Markdown
from rich.console import Console
import html as html


class MarkdownRenderer(object):
    def __init__(self, markdown_text, console_print=True):
        assert isinstance(markdown_text, str), "Expected a string"

        markdown_text = html.unescape(markdown_text)
        self.markdown_text = markdown_text
        self.do_console_print = bool(console_print)

        self.console = Console()  # rich console

        self.render = self.print_mark_down_text()

    def print_mark_down_text(self):
        rendered_markdown = Markdown(self.markdown_text)

        if self.do_console_print:
            self.console.print(rendered_markdown)

        return rendered_markdown

    def __repr__(self):
        return str(self.render)

    def __len__(self):
        if isinstance(self.render, str):
            return len(self.render)
        return -1

    def __str__(self):
        return str(self.render)

    def __repr__(self):
        return str(self.render)
