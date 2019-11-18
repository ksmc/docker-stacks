import setuptools
 
setuptools.setup(
    name="jupyter-pilot-proxy",
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
    py_modules=['jupyter_pilot_proxy'],
    entry_points={
        'jupyter_serverproxy_servers': [
            'pilot = jupyter_pilot_proxy:setup_pilot',
        ]
    }
)