import setuptools

setuptools.setup(
    name="jupyter-omnidb-proxy",
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
            'omnidb = jupyter_omnidb_proxy:setup_omnidb',
        ]
    },
    package_data={
        'jupyter_omnidb_proxy': ['icons/*'],
    },
)
