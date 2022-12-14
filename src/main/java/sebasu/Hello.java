package src.main.java.sebasu;


import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class Hello {

    @GetMapping("/jelou")
    public String hello() {
        return "Hello World!";
    }
}
