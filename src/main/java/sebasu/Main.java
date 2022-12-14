package src.main.java.sebasu;

///usr/bin/env jbang "$0" "$@" ; exit $?
//add the needed jbang deps here
//DEPS org.springframework.boot:spring-boot-starter-web:2.3.4.RELEASE
////DEPS org.springframework.boot:spring-boot-starter-data-jpa:2.3.4.RELEASE
///DEPS org.springframework.boot:spring-boot-starter-test:2.3.4.RELEASE
///DEPS org.springframework.boot:spring-boot-starter-actuator:2.3.4.RELEASE
///DEPS org.springframework.boot:spring-boot-starter-security:2.3.4.RELEASE
///DEPS org.springframework.boot:spring-boot-starter-data-rest:2.3.4.RELEASE
////DEPS org.springframework.boot:spring-boot-starter-data-mongodb:2.3.4.RELEASE
//JAVA 11
//SOURCES Hello.java

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Main {

    public static void main(String[] args) {

        //set server to localhost:3030
        System.setProperty("server.port", "3030");
        System.setProperty("server.IP", "localhost");


        SpringApplication.run(Main.class, args);
    }

}
