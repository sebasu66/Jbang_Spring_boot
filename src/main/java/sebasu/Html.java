package src.main.java.sebasu;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;

@RestController
public class Html {


    //read and parse html file located at /html/demo/home.html
    static String getHtmlContent(String fileName){
        File file = new File("html/demo/" + fileName + ".html");
        try {
            return new String(Files.readAllBytes(file.toPath()));
        } catch (IOException e) {
            return "Error reading file: " + fileName;
        }
    }

    //getHtml restService, expect optional page name parameter, default is "home"
    @GetMapping("/getHtml")

    public String getHtml(String page) {
        if (page == null) {
            page = "home";
        }
        return getHtmlContent(page);
    }

}
