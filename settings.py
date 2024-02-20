import os
import pathlib
import platform

from OptionsDialog import OptionsDialog
from utilities import FileBackedDictionary

print('in settings, os.environ',os.environ)
for e in ['USERPROFILE','APPDATA','HOME']:
    if e in os.environ: home_ = os.environ[e]
print('in settings, home_=',home_)
settings = FileBackedDictionary(
    str(pathlib.Path(home_) / '.molpro' / 'iMolpro.settings.json'))


def settings_edit(parent=None):
    box = OptionsDialog(dict(settings), ['CHEMSPIDER_API_KEY', 'mo_translucent', 'expertise'], title='Settings',
                        parent=parent)
    result = box.exec()
    if result is not None:
        for k in result:
            try:
                result[k] = int(result[k])
            except:
                try:
                    if type(result[k]) != int:
                        result[k] = float(result[k])
                except:
                    pass
            settings[k] = result[k]
        for k in settings:
            if k not in result:
                del settings[k]
