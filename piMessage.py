from ScriptingBridge import SBApplication
iMessage = SBApplication.applicationWithBundleIdentifier_("com.apple.iChat")
buddies = list(iMessage.buddies())


class Buddy:
    def __init__(self, native_obj):
        self._native_obj = native_obj
        self.name = native_obj.name()
        self.handle = native_obj.handle()
        self.service = native_obj.service().service_type()


