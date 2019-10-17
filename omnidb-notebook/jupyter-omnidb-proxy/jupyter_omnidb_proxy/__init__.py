"""
Return config on servers to start for theia

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil

def setup_omnidb():
    # Make sure theia is in $PATH
    def _omnidb_command(port):
#         return ['omnidb-server','-H', '0.0.0.0', '-p', str(port)]
        return ['python', '/opt/conda/omnidb/OmniDB/OmniDB/omnidb-server.py','-H', '0.0.0.0', '-p', str(port), '-c', '/opt/conda/omnidb/OmniDB/OmniDB/omnidb.conf']

    return {
        'command': _omnidb_command,
        'environment': {
            'USE_LOCAL_GIT': 'true'
        },
        'timeout': 20,
#         'absolute_url': True,
        'launcher_entry': {
            'title': 'OmniDB IDE',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'theia.svg')
        }
    }