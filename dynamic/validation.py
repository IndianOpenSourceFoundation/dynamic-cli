from prompt_toolkit.validation import Validator, ValidationError

class Arg0_Validator(Validator):
    def validate(self, document):
        text = document.text

        if(len(text) > 6):
            if(text[0:7] != 'dynamic'):
                raise ValidationError(message='Usage: dynamic -[OPTIONS]')
            if(len(text) >= 8 and text[7] != ' '):
                raise ValidationError(message='Usage: dynamic <space> -[OPTIONS]')
            if(len(text) >= 9 and text[8] != '-'):
                raise ValidationError(message='Usage: dynamic -[OPTIONS]')

        else:
            raise ValidationError(message='Usage: dynamic -[OPTIONS]')