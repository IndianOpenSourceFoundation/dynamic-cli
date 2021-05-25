from termcolor import colored


class SearchError():
    def __init__(self, error_statement, suggestion="Try again"):
        # the error statement
        self.error_statement = error_statement

        # the suggestion statement
        self.suggestion = suggestion

        self.evoke_search_error(self.error_statement)

    def evoke_search_error(self, error_statement):
        print_text = [
            colored(error_statement, 'red'),
            colored(self.suggestion, 'green')
        ]
        for text_to_print in print_text:
            print(text_to_print)

class LoginError():
    def __init__(self, error_statement, success=False):
        """Implements error printing for User Login

        :error_statement: Error statement to print
        :success: Indicates success of login attempt
                  Prints in green if True else red
        """
        self.error_statement = error_statement
        self.success = success
        self.evoke_search_error()

    def evoke_search_error(self):
        color = "green" if self.success else "red"
        print_text = colored(self.error_statement, color)
        print(print_text)