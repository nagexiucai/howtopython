function SyntaxPaser(text) {
    var code = text || "";
    function operation() {
        return {
            "name": undefined,
            "type": undefined,
            "parameters": [],
            "inner": [],
            "outer": undefined
        };
    };
    var ast = operation();
    ast.name = "module";
    ast.outer = undefined;
    while (code.indexOf("\r") != -1) {
        code = code.replace("\r", " ")
    }
    while (code.indexOf("\n") != -1) {
        code = code.replace("\n", " ")
    }
    while (code.indexOf("  ") != -1) {
        code = code.replace("  ", " ");
    }
    code = code.trim();
    console.log(code);
    var level = 0;
    var identifier = "";
    var status = undefined;
    var mode = [];
    var cursor = ast;
    for (var i=0; i<code.length; i++) {
        if (code[i] == "{") {
            // 开始子过程
            level += 1;
            mode.push(status);
        }
        else if (code[i] == "}") {
            // 结束子过程
            level -= 1;
            mode.pop();
        }
        else if (code[i] == " ") {
            if (identifier) status = "cut";
        }
        else if (code[i] == "(") {
            // 进入调用子句
            status = "FUNCTION";
            var o = operation();
            o.name = identifier;
            o.type = status;
            identifier = "";
            o.outer = cursor;
            cursor.inner.push(o);
            cursor = o;
            mode.push(status);
        }
        else if (code[i] == ")") {
            // 退出调用子句
            cursor.parameters.push(identifier);
            identifier = "";
            cursor = cursor.outer;
            mode.pop()
        }
        else if (code[i] == ";") {
            // 分句优化
        }
        else {
            identifier += code[i];
            status = undefined;
        }
        if (status == "cut") {
            console.log(level + " --- " + identifier);
            if (identifier == "REVOLVE") {
                // 进入REVOLVE子句
                status = "revolve";
            }
            else if (identifier == "IF") {
                // 进入IF子句
                status = "if";
            }
            else if (identifier == "ELSE") {
                // 进入ELSE子句
                status = "else";
            }
            else if (identifier == "NOT") {
                // 进入NOT子句
                status = "not";
            }
            else if (identifier == "AND") {
                // 进入AND子句
                status = "and";
            }
            else {}
            identifier = "";
            status = undefined;
        }
    }
}