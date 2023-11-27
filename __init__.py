from mycroft import MycroftSkill, intent_file_handler


class Voicegptlink(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('voicegptlink.intent')
    def handle_voicegptlink(self, message):
        self.speak_dialog('voicegptlink')


def create_skill():
    return Voicegptlink()

