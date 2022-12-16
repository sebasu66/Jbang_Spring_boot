package src.main.java.sebasu;

import java.util.Map;

public class JsonToHtml {


    //private constructor
    private JsonToHtml() {
    }

    // Generate HTML code for a button
    private static String generateButtonHtml(Map<String, Object> buttonProps) {
        String label = (String) buttonProps.get("label");
        String url = (String) buttonProps.get("url");
        return "<a class='button' href='" + url + "'>" + label + "</a>";
    }

    // Generate HTML code for a link
    private static String generateLinkHtml(Map<String, Object> linkProps) {
        String label = (String) linkProps.get("label");
        String url = (String) linkProps.get("url");
        return "<a href='" + url + "'>" + label + "</a>";
    }

    // Generate HTML code for an image
    private static String generateImageHtml(Map<String, Object> imageProps) {
        String alt = (String) imageProps.get("alt");
        String src = (String) imageProps.get("src");
        return "<img src='" + src + "' alt='" + alt + "' />";
    }

    // Parse a JSON object and generate the corresponding HTML code
    public static String parseJson(Map<String, Object> json) {
        StringBuilder html = new StringBuilder();

        // Iterate over the properties of the JSON object
        for (Map.Entry<String, Object> entry : json.entrySet()) {
            String key = entry.getKey();
            Object value = entry.getValue();

            // Generate HTML code for the property based on its type
            if (value instanceof Map) {
                Map<String, Object> props = (Map<String, Object>) value;
                if (key.equals("button")) {
                    html.append(generateButtonHtml(props));
                } else if (key.equals("link")) {
                    html.append(generateLinkHtml(props));
                } else if (key.equals("image")) {
                    html.append(generateImageHtml(props));
                }
            }
        }

        // Return the generated HTML code
        return html.toString();
    }

}

