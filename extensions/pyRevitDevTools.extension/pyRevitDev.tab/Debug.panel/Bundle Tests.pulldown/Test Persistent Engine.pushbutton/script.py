"""Testing non-modal windows calling actions thru external events.

Shift-Click:
Run window as Modal
"""
# pylint: skip-file
from pyrevit import forms
from pyrevit import UI
from pyrevit.coreutils import basetypes


__title__ = "Test Persistent Engine (NonModal)"
__author__ = "{{author}}"
__persistentengine__ = True


class NonModalWindow(forms.WPFWindow):
    def __init__(self, xaml_file_name, ext_event, ext_event_handler):
        forms.WPFWindow.__init__(self, xaml_file_name)
        self.ext_event = ext_event
        self.ext_event_handler = ext_event_handler
        self.prev_title = "Title Changed..."

    def action(self, sender, args):
        if __shiftclick__:
            self.Close()
            forms.alert("Stuff")
        else:
            self.ext_event_handler.KeynoteKey = "12"
            self.ext_event_handler.KeynoteType = UI.PostableCommand.UserKeynote
            self.ext_event.Raise()

    def other_action(self, sender, args):
        self.Title, self.prev_title = self.prev_title, self.Title


handler = basetypes.PlaceKeynoteExternalEventHandler()

NonModalWindow(
    'NonModalWindow.xaml',
    ext_event=UI.ExternalEvent.Create(handler),
    ext_event_handler=handler
    ).show(modal=__shiftclick__)