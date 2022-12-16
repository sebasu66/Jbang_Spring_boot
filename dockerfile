FROM ubuntu:latest

RUN cd lib

RUN apt-get update && \
    apt-get -y install git curl && \
    curl -Ls https://sh.jbang.dev | bash -s - app setup && \
    git clone https://github.com/sebasu66/Jbang_Spring_boot.git

#PRINT THE FOLDER CONTENT TO CHECK IF THE FILES ARE THERE
RUN ls -la

RUN cd jbang-spring-boot/src/main/java/sebasu && \
    jbang --java 11 ./Main.java

CMD ["/bin/bash"]
EXPOSE 3000
