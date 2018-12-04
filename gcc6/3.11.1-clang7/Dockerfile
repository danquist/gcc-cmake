FROM gcc:6

ARG CMAKE_VERSION=3.11
ARG CMAKE_BUILD=1

RUN wget -q https://raw.githubusercontent.com/danquist/install-cmake/master/install-cmake.sh /; \
    chmod +x /install-cmake.sh; \
    /install-cmake.sh $CMAKE_VERSION $CMAKE_BUILD; \
    rm -f /install-cmake.sh

# Install clang and add to path
RUN curl -SL http://releases.llvm.org/7.0.0/clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04.tar.xz \
  | tar -xJC . && \
  mv clang+llvm-7.0.0-x86_64-linux-gnu-ubuntu-16.04 clang_7.0.0 && \
  echo 'export PATH=/clang_7.0.0/bin:$PATH' >> ~/.bashrc && \
  echo 'export LD_LIBRARY_PATH=/clang_7.0.0/lib:LD_LIBRARY_PATH' >> ~/.bashrc
  