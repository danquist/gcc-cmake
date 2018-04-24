FROM gcc:6

ARG CMAKE_VERSION=3.11
ARG CMAKE_BUILD=1

RUN wget -q https://raw.githubusercontent.com/danquist/install-cmake/master/install-cmake.sh /; \
    chmod +x /install-cmake.sh; \
    /install-cmake.sh $CMAKE_VERSION $CMAKE_BUILD; \
    rm -f /install-cmake.sh
