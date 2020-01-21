# Libraries
import setuptools

# Requirements
requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

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
        'Changelog': (
            'https://gitlab.com/AdrianDC/gitlabci-local/blob/master/CHANGELOG.md')
    },
    packages=setuptools.find_packages(exclude=['tests']),
    setup_requires=['setuptools_scm'],
    install_requires=requirements,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    keywords='gitlab-ci local pipeline',
    python_requires='>=3',
    entry_points={
        'console_scripts': [
            'gitlabci-local = gitlabci_local.main:main',
        ],
    },
)
