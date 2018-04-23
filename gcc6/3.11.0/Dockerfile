FROM gcc:6

ARG version=3.11
ARG build=0

LABEL gcc-version=6
LABEL cmake-version=$version.$build

RUN installer=cmake-$version.$build-Linux-x86_64.sh; \
  cd ~; \
  wget "https://cmake.org/files/v$version/$installer" -P .; \
  mkdir /opt/cmake; \
  sh $installer --prefix=/opt/cmake --skip-license; \
  ln -s /opt/cmake/bin/cmake /usr/local/bin/cmake; \
  rm -f $installer