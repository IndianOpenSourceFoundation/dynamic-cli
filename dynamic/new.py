from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion, NestedCompleter

command_dict = {
             'dynamic':{
             '-s': '--search for a question',
             '-v': '--current version',
             '-no': '--notion-login',
             '-c': '--custom API Key',
             '-p': '--access playbook',
             '-h': '--help',
             '-GET': '--API GET',
             '-POST': '--API POST',
             '-DELETE': 'API DELETE'
            }
}


class CustomCompleter(Completer):
    def __init__(self, command_dict):
        self.command_dict = command_dict

    def get_completions(self, document, complete_event):
        matches = [name for name in self.command_dict.keys() if document.text in name]
        for m in matches:
            yield Completion(m, start_position=-len(document.text_before_cursor),
            display = m)
        if(document.text[0:7] == 'dynamic'):
            matches = [name for name in self.command_dict['dynamic'].keys() if document.get_word_before_cursor() in name]
            for m in matches:
                yield Completion(m, start_position=-len(document.get_word_under_cursor()),
                          display = m, display_meta = self.command_dict['dynamic'][m])
            

        
completer = CustomCompleter(command_dict)


if __name__ == '__main__':
    answer = prompt('>>> ', completer = completer)
    print('ID: %s' % answer)

