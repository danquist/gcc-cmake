import os
import pathlib

images = [
  ('6', '3.1', '3'),
  ('6', '3.2', '3'),
  ('6', '3.3', '2'),
  ('6', '3.4', '3'),
  ('6', '3.5', '2'),
  ('6', '3.6', '3'),
  ('6', '3.7', '2'),
  ('6', '3.8', '2'),
  ('6', '3.9', '6'),
  ('6', '3.10', '3'),
  ('6', '3.11', '0'),
  ('6', '3.11', '1'),
  ('7', '3.1', '3'),
  ('7', '3.2', '3'),
  ('7', '3.3', '2'),
  ('7', '3.4', '3'),
  ('7', '3.5', '2'),
  ('7', '3.6', '3'),
  ('7', '3.7', '2'),
  ('7', '3.8', '2'),
  ('7', '3.9', '6'),
  ('7', '3.10', '3'),
  ('7', '3.11', '0'),
  ('7', '3.11', '1'),
]

root = os.path.abspath(os.path.join(os.path.dirname(__file__ ), '..'))

installrepo = 'danquist/install-cmake'
installBranch = 'master'
installFile = 'install-cmake.sh'
installer = 'https://raw.githubusercontent.com/{}/{}/{}'.format(installrepo, installBranch, installFile)

template = """FROM gcc:{gcc}

ARG CMAKE_VERSION={version}
ARG CMAKE_BUILD={build}

RUN wget -q {installer} /; \\
    chmod +x /install-cmake.sh; \\
    /install-cmake.sh $CMAKE_VERSION $CMAKE_BUILD; \\
    rm -f /install-cmake.sh
"""

def createImage(file, gcc, version, build):
  dir = os.path.dirname(file)
  pathlib.Path(dir).mkdir(parents=True, exist_ok=True) 
  content = template.format(gcc = gcc, version = version, build = build, installer = installer)
  
  with open(file, 'w') as f:
    f.write(content)


def createImages():
  for i in images:
    file = os.path.join(root, 'gcc' + i[0], i[1] + '.' + i[2], 'Dockerfile')
    createImage(file, i[0], i[1], i[2])

def createLatest():
  file = os.path.join(root, 'latest', 'Dockerfile')
  createImage(file, 'latest', '3.11', '1')

createImages()
createLatest()
