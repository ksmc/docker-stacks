# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'pgadmin': {
        #Set the port for pgadmin dynamically
        'command': [
            'gunicorn',
            '-b',
            '127.0.0.1:{port}',
            '-e',
            'SCRIPT_NAME={base_url}pgadmin',
            '--chdir',
            '/opt/conda/lib/python3.7/site-packages/pgadmin4',
            'pgAdmin4:app',
        ],
        'absolute_url': True,
        'timeout': 120,
        'launcher_entry': {
            'enabled': True,
            'icon_path': '/home/jovyan/.jupyter/postgresql-logo.svg',
            'title': 'pgAdmin',
        },
    },
}