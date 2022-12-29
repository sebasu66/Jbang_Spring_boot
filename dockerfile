FROM ubuntu:latest

RUN apt-get update && \
    apt-get -y install git curl && \
    git clone https://github.com/sebasu66/Jbang_Spring_boot.git

RUN curl -Ls https://sh.jbang.dev | bash -s - app setup \
cmd su \
cmd curl -Ls https://sh.jbang.dev | bash -s - properties@jbangdev \
cmd jbang --java 11 ./Jbang_Spring_boot/src/main/java/sebasu/Main.java

CMD ["/bin/bash"]
EXPOSE 3000
