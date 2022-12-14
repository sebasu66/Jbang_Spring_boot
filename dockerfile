FROM ubuntu:latest

RUN cd lib

RUN apt-get update && \
    apt-get -y install node git curl && \
    curl -Ls https://sh.jbang.dev | bash -s - app setup && \
    git clone https://github.com/sebasu66/Jbang_Spring_boot.git

CMD ["/bin/bash"]