"""
Return config on servers to start for theia
 
See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil
 
def setup_pilot():
    # Make sure theia is in $PATH
    def _pilot_command(port):
        return ['python','/home/jovyan/uindy_pilot/manage.py', 'runserver', '0.0.0.0:{}'.format(str(port))]
 
    return {
        'command': _pilot_command,
#         'timeout': 120,
#         'absolute_url': True,
        'launcher_entry': {
            'title': 'Open UIndy Pilot Site'
        }
    }