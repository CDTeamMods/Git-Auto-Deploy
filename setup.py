from setuptools import setup, find_packages
import os

# Helper function to read files
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8") as f:
        return f.read()

def read_requirements(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

def package_files(package_path, directory_name):
    paths = []
    directory_path = os.path.join(package_path, directory_name)

    for (path, directories, filenames) in os.walk(directory_path):
        relative_path = os.path.relpath(path, package_path)
        for filename in filenames:
            if filename[0] == ".":
                continue
            paths.append(os.path.join(relative_path, filename))
    return paths

# Get path to project
package_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "gitautodeploy")

# Get list of data files
wwwroot_files = package_files(package_path, "wwwroot")
data_files = package_files(package_path, "data")

setup(
    name='git-auto-deploy',
    version='0.1',
    url='https://github.com/CDTeamMods/Git-Auto-Deploy',
    author='CDTeam',
    author_email='contato@cdteam.xyz',
    packages=find_packages(),
    package_data={'gitautodeploy': data_files + wwwroot_files},
    entry_points={
        'console_scripts': [
            'git-auto-deploy = gitautodeploy.__main__:main'
        ]
    },
    install_requires=read_requirements('requirements.txt'),
    description="Deploy your GitHub, GitLab or Bitbucket projects automatically on Git push events or webhooks.",
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
    ],
    python_requires='>=3.6',
)
