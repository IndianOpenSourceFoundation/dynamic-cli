from clint.textui import colored


class SearchError():
    def __init__(self, error_statement, suggestion="Try again"):
        # the error statement
        self.error_statement = error_statement

        # the suggestion statement
        self.suggestion = suggestion

        self.evoke_search_error(self.error_statement)

    def evoke_search_error(self, error_statement):
        print_text = [
            colored.red(error_statement),
            colored.green(self.suggestion)
        ]
        for text_to_print in print_text:
            print(text_to_print)
