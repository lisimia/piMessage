from ScriptingBridge import SBApplication
iMessage = SBApplication.applicationWithBundleIdentifier_("com.apple.iChat")
bubbies = list(iChat.buddies())
