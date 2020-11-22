# Libraries
import setuptools

# Requirements
requirements = []
with open('requirements.txt') as f:
    requirements = [line for line in f.read().splitlines() if not line.startswith('#')]

# Long description
long_description = ''
with open('README.md', 'r') as f:
    long_description = f.read()

# Setup configurations
setuptools.setup(
    name='gitlabci-local',
    use_scm_version=True,
    author='Adrian DC',
    author_email='radian.dc@gmail.com',
    license='Apache License 2.0',
    description='Launch .gitlab-ci.yml jobs locally',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://gitlab.com/AdrianDC/gitlabci-local',
    project_urls={
        'Bug Reports': 'https://gitlab.com/AdrianDC/gitlabci-local/-/issues',
        'Changelog': 'https://gitlab.com/AdrianDC/gitlabci-local/blob/master/CHANGELOG.md',
        'Documentation': 'https://gitlab.com/AdrianDC/gitlabci-local#gitlabci-local',
        'Source': 'https://gitlab.com/AdrianDC/gitlabci-local',
        'Statistics': 'https://pypistats.org/packages/gitlabci-local'
    },
    packages=setuptools.find_packages(exclude=['tests']),
    setup_requires=['setuptools_scm'],
    install_requires=requirements,
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    keywords='gitlab-ci local gcil pipeline',
    python_requires='>=3, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, !=3.5.*',
    entry_points={
        'console_scripts': [
            'gitlabci-local = gitlabci_local.main:main',
            'gcil = gitlabci_local.main:main',
        ],
    },
)
