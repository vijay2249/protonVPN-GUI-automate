 - [Trying to use win32ui with pywin32 gives: A dynamic link library (DLL) initialization routine failed](https://stackoverflow.com/questions/64444740/trying-to-use-win32ui-with-pywin32-gives-a-dynamic-link-library-dll-initializ)

 - [GUI automation blog post](https://www.apriorit.com/dev-blog/615-qa-gui-testing-windows-python-pywinauto)

 - [updated dependencies sample code github repo link](https://github.com/anunay1/SampleWADPython/blob/master/Sample.py)

 - [pywinauto docs](https://pywinauto.readthedocs.io/en/latest/)

 - [Cannot import from pywinauto: ImportError: DLL load failed while importing win32ui: A dynamic link library (DLL) initialization routine failed](https://stackoverflow.com/questions/64655079/cannot-import-from-pywinauto-importerror-dll-load-failed-while-importing-win32)

 - [prebuilt windows pywin32 binaries v228](https://github.com/CristiFati/Prebuilt-Binaries/tree/master/PyWin32/v228)

 - ## Official v228 (and older) doesn't work with Python 3.9.

 - [https://github.com/mhammond/pywin32/issues/1431#issuecomment-698179224](https://github.com/mhammond/pywin32/issues/1431#issuecomment-698179224)
 
    for _"import win32api # noqa: E402 ImportError: DLL load failed while importing win32api: The specified procedure could not be found."_ error

process in solving the above mentioned error:
1. uninstalled previous versions of modules
2. updated all conda modules and dependencies
3. follow the complete issue number 1431, using the above link