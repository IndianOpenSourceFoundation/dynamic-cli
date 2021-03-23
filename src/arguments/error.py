from clint.textui import colored as TextColor


class SearchError():
    def __init__(self, error_statement, suggestion="Try again"):
        self.error_statement = error_statement
        self.suggestion = suggestion
        self.evoke_search_error(self.error_statement)

    def evoke_search_error(self, error_statement):
        print_text = [
            TextColor.red(error_statement),
            TextColor.green(self.suggestion)
        ]
        for text_to_print in print_text:
            print(text_to_print)
