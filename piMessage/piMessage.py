from ScriptingBridge import SBApplication


class Service:
    def __init__(self, native_obj):
        self._native_obj = native_obj
        self.name = native_obj.name()
        self.id = native_obj.id()
        self.service_type = native_obj.serviceType()

    def __repr__(self):
        return self.name.encode('utf-8')


class Buddy:
    def __init__(self, native_obj):
        self._native_obj = native_obj
        self.name = native_obj.name()
        self.full_name = native_obj.fullName()
        self.first_name = native_obj.firstName()
        self.last_name = native_obj.lastName()
        self.handle = native_obj.handle()
        self._id = native_obj.id()
        self.service = Service(native_obj.service())

    def __repr__(self):
        return u"Buddy {} of {} with handle {}".format(
            self.name,
            self.service.name,
            self.handle
        ).encode('utf-8')


class Chat(object):
    def __init__(self, native_obj):
        self._native_obj = native_obj
        self.id = native_obj.id()
        try:
            self.service = Service(native_obj.serivce())
        except:
            try:
                self.service = Service(native_obj.serivce())
            except:
                self.service = ''

        self.secure = native_obj.secure()

    def __repr__(self):
        return u"{}".format(
            self.id,
        ).encode('utf-8')
        #return u"{} {}".format(
        #    self.id,
        #    u"\U0001F512" if self.secure else u"\U0001F513"
        #).encode('utf-8')


class TextChat(Chat):
    def __init__(self, native_obj):
        super(TextChat, self).__init__(native_obj)
        self.name = native_obj.name()
        self.chat_type = native_obj.chatType()


client = SBApplication.applicationWithBundleIdentifier_("com.apple.iChat")
buddies = []
for buddy in client.buddies():
    buddies.append(Buddy(buddy))

text_chats = []
for chat in client.textChats():
    text_chats.append(TextChat(chat))

version = client.version()
print "you are using iMsg version", version

def send(text, buddy):
    assert isinstance(buddy, Buddy)
    client.send_to_(text,buddy._native_obj)
    return
    # alt method of sending using apple script
    import subprocess
    m = """
    tell application "Messages"
        repeat with myBuddy in buddies
            if id of myBuddy is {buddy.id} then
                send "i would get one myself" to myBuddy
                exit repeat
            end if
        end repeat
    end tell
    """
    p = subprocess.Popen(['osascript'],stdin=subprocess.PIPE)
    p.communicate(input=m)
