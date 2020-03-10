from setuptools import setup, find_packages

setup(
    name='mkdocs-git-info-plugin',
    version='0.0.3',
    description='MkDocs plugin that exposes helpful git information in the context',
    keywords='mkdocs git meta info yaml frontmatter',
    url='https://github.com/gidven/mkdocs-git-info-plugin',
    author='Gid van der Ven',
    author_email='giddevanderven@gmail.com',
    license='MIT',
    python_requires='>=3.4',
    install_requires=[
        'mkdocs>=0.17',
        'GitPython',
        'jinja2'
    ],
    packages=find_packages(),
    entry_points={
        'mkdocs.plugins': [
            'git-info = mkdocs_git_info_plugin.plugin:GitInfoPlugin'
        ]
    }
)