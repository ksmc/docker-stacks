import setuptools

setuptools.setup(
    name="jupyter-pgadmin-proxy",
    version='1.0',
    url="https://github.com/ksmc/management-guidance",
    author="Project Jupyter Contributors",
    description="projectjupyter@gmail.com",
    packages=setuptools.find_packages(),
	keywords=['Jupyter'],
	classifiers=['Framework :: Jupyter'],
    install_requires=[
        'jupyter-server-proxy'
    ],
    entry_points={
        'jupyter_serverproxy_servers': [
            'pgadmin = jupyter_pgadmin_proxy:setup_pgadmin',
        ]
    },
    package_data={
        'jupyter_pgadmin_proxy': ['icons/*'],
    },
)
