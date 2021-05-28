import webbrowser


class ReportIssues(object):
    url = "https://github.com/IndianOpenSourceFoundation/dynamic-cli/issues/new?assignees=&labels=proposal&template=proposal.md&title=<title-text>"

    def __init__(self, prompt=None):
        self.prompt = prompt
        if self.prompt:
            message = self.create_issue_prompt()
            are_you_sure = self.prompt("Are you sure (y/n)").prompt()
            if are_you_sure.lower() == "y":
                webbrowser.open(self.url.replace("<title-text>", message))

    def create_issue_prompt(self):
        data = self.prompt("Issue").prompt()
        return data
