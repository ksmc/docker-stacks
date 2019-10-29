"""
Return config on servers to start for theia

See https://jupyter-server-proxy.readthedocs.io/en/latest/server-process.html
for more information.
"""
import os
import shutil

def setup_pgadmin():
    # Make sure theia is in $PATH
    def _pgadmin_command(port):
        return ['python', '/opt/conda/lib/python3.7/site-packages/pgadmin4/pgAdmin4.py', '--port=' + str(port)]

    return {
        'command': _pgadmin_command,
        'environment': {
            'USE_LOCAL_GIT': 'true'
        },
        'timeout': 120,
        'absolute_url': True,
        'mappath': {'/':'/browser'},
        'launcher_entry': {
            'title': 'PgAdmin IDE',
            'icon_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'theia.svg')
        }
    }