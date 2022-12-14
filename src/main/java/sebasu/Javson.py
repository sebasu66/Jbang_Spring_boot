jsonObject ={
    "package": "src.main.java.sebasu",
    "jbang": "/usr/bin/env jbang \"$0\" \"$@\" ; exit $?",
    "deps": [
        "org.springframework.boot:spring-boot-starter-web:2.3.4.RELEASE",
        "javax.transaction:javax.transaction-api:1.3"
    ],
    "imports": [
        "org.springframework.boot.SpringApplication",
        "org.springframework.boot.autoconfigure.SpringBootApplication",
        "org.springframework.stereotype.Component",
        "org.springframework.web.bind.annotation.GetMapping"
    ],
    "class": {
        "name": "Main",
        "tags": [
            "@SpringBootApplication",
            "@Component"
        ],
        "methods": [
            {
                "name": "main",
                "access": "public",
                "static": "true",
                "return": "void",
                "tags": [],
                "params": [
                    {
                        "name": "args",
                        "type": "String[]"
                    }
                ],
                "body": "SpringApplication.run(Main.class, args);"
            },
            {
                "name": "hello",
                "access": "public",
                "static": "false",
                "return": "String",
                "tags": [
                    "@GetMapping(\"/hello\")"
                ],
                "params": [],
                "body": "return myString;"
            },
        ],
        "fields": [
            {
                "name": "myString",
                "tags": [],
                "type": "String",
                "access": "private",
                "static": "true",
                "value": "\"Hello World!\""
            }
        ]
    }
}

#json structure object

jsonFrame = {
    "package":{
        "_edit":"true",
        "_type":"text",
        "_allow":"package",
        "_label":"Package",
        "value":"",
    },
    "jbang":{
        "_edit":"true",
        "_type":"text",
        "_allow":"jbang",
        "_label":"Jbang",
        "value":"",
        "default":"//usr/bin/env jbang \"$0\" \"$@\" ; exit $?",
        "dep_list": {
                "_edit":"true",
                "_type":"text[]",
                "_label":"Jbsng Dependence",
                "value":"[]",
                "_allow":"jbang_dep_list",
        "_hint":"org.springframework.boot:spring-boot-starter-web:2.3.4.RELEASE",
            }},
    "import_list":{
        "_edit":"true",
        "value":"[]",
        "_type":"text[]",
        "_label":"Imports",
"_allow":"import_list",
        "_hint":"org.springframework.boot.SpringApplication",
    },
    "class":{
        "_edit":"true",
        "_type":"object",
        "_label":"Class",
        "_allow":"class"
    },
    "field_list":{
        "_edit":"true",
        "_type":"object[]",
        "_label":"Fields",
        "_allow":"field_list",
        "value":"[]",
    },
    "method_list":{
        "_edit":"true",
        "_type":"object[]",
        "_label":"Methods",
        "_allow":"method_list",
        "value":"[]",
    },
}




jsonObject ={
    "package": "src.main.java.sebasu",
    "jbang": "/usr/bin/env jbang \"$0\" \"$@\" ; exit $?",
    "deps": [
        "org.springframework.boot:spring-boot-starter-web:2.3.4.RELEASE",
        "javax.transaction:javax.transaction-api:1.3"
    ],
    "imports": [
        "org.springframework.boot.SpringApplication",
        "org.springframework.boot.autoconfigure.SpringBootApplication",
        "org.springframework.stereotype.Component",
        "org.springframework.web.bind.annotation.GetMapping"
    ],
    "class": {
        "name": "Main",
        "tags": [
            "@SpringBootApplication",
            "@Component"
        ],
        "methods": [
            {
                "name": "main",
                "access": "public",
                "static": "true",
                "return": "void",
                "tags": [],
                "params": [
                    {
                        "name": "args",
                        "type": "String[]"
                    }
                ],
                "body": "SpringApplication.run(Main.class, args);"
            },
            {
                "name": "hello",
                "access": "public",
                "static": "false",
                "return": "String",
                "tags": [
                    "@GetMapping(\"/hello\")"
                ],
                "params": [],
                "body": "return myString;"
            },
        ],
        "fields": [
            {
                "name": "myString",
                "tags": [],
                "type": "String",
                "access": "private",
                "static": "true",
                "value": "\"Hello World!\""
            }
        ]
    }
}

# write a python function that receives the json object and returns a String representing the java class:

def parse_json_to_java_class(json_object):
    # your code goes here
    # return the java class as a String
    package = "package " + json_object["package"] + ";\n\n"
    jBangComment = "//" + json_object["jbang"] + "\n" if "jbang" in json_object else ""
    jbangDeps = ""
    for dep in json_object["deps"]:
        jbangDeps += "//DEPS " + dep + "\n"
    jbangDeps += "\n"
    imports = ""
    for i in json_object["imports"]:
        imports += "import " + i + ";\n"
    imports += "\n"
    class_name = json_object["class"]["name"]
    tags = ""
    for i in json_object["class"]["tags"]:
        tags += i + "\n"
    fields = ""
    for i in json_object["class"]["fields"]:
        if i["tags"]:
            for j in i["tags"]:
                fields += j + "\n"
        fields += i["access"] + " " + i["type"] + " " + i["name"] + " = " + i["value"] + ";\n"
    fields += "\n"
    methods = ""
    for i in json_object["class"]["methods"]:
        method_tags = ""
        for j in i["tags"]:
            method_tags += j + "\n"
        method_params = ""
        for j in i["params"]:
            method_params += j["type"] + " " + j["name"] + ", "
        method_params = method_params[:-2]
        methods += method_tags + i["access"] + " " + ("static " if i["static"] else "") + i["return"] + " " + i["name"] + "(" + method_params + ") {\n" + i["body"] + "\n}\n\n"
    return package + jBangComment + jbangDeps + imports + tags + "public class " + class_name + " {\n\n" + fields + methods + "}"















