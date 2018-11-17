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
    ast.name = "root";
    ast.type = "module"
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
    // console.log(code);
    var level = 0;
    var identifier = "";
    var status = undefined;
    var mode = [];
    var cursor = ast;
    for (var i=0; i<code.length; i++) {
        if (code[i] == "{") {
            // 开始子过程
            level += 1;
            // 用SYNTAX CLAUSE {标记开始的压栈（在具体语法标志处）
            if (status.endsWith("if")) {
                var o = cursor.inner.pop();
                cursor.parameters.push(o);
            }
        }
        else if (code[i] == "}") {
            // 结束子过程
            level -= 1;
            cursor = cursor.outer; // 外跳一层
            status = mode.pop(); // 用}标记结束的弹栈
        }
        else if (code[i] == " ") {
            if (identifier) status = "cut";
        }
        else if (code[i] == "(") {
            // 进入调用子句
            // IsHole(side) IsWall(side)
            // IsEnd()
            // Echo(message)
            mode.push(status); // 函数闭包压栈
            status = "function";
            var o = operation();
            o.name = identifier;
            o.type = status;
            identifier = "";
            cursor.inner.push(o);
            o.outer = cursor;
            cursor = o;
            mode.push(status); // 用(标记开始的压栈
        }
        else if (code[i] == ")") {
            // 退出调用子句
            if (identifier) cursor.parameters.push(identifier); // 函数嵌套调用
            identifier = "";
            cursor = cursor.outer;
            status = mode.pop() // 用)标记结束的弹栈
            if (status != "function") {
                alert("见鬼！");
            }
            status = mode.pop() // 函数闭包弹栈
        }
        else if (code[i] == ";") {
            // 分句优化
        }
        else {
            identifier += code[i];
        }
        if (status == "cut") {
            // console.log(level + " --- " + identifier);
            if (identifier == "REVOLVE") {
                // 进入REVOLVE子句
                status = "revolve";
                var o = operation();
                o.name = identifier;
                o.type = status;
                cursor.inner.push(o);
                o.outer = cursor;
                cursor = o;
                mode.push(status);
            }
            else if (identifier == "GOON") {
                // 进入GOON从句
                status = "goon";
                var o = operation();
                o.name = identifier;
                o.type = status;
                cursor.inner.push(o);
                o.outer = cursor;
                // 最内层
            }
            else if (identifier == "IF") {
                // 进入IF子句
                status = "if";
                var o = operation();
                o.name = identifier;
                o.type = status;
                cursor.inner.push(o);
                o.outer = cursor;
                cursor = o;
                mode.push(status);
            }
            else if (identifier == "ELSEIF") {
                // 进入ELSEIF子句
                status = "elseif";
                var o = operation();
                o.name = identifier;
                o.type = status;
                cursor.inner.push(o);
                o.outer = cursor;
                cursor = o;
                mode.push(status);
            }
            else if (identifier == "ELSE") {
                // 进入ELSE子句
                status = "else";
                var o = operation();
                o.name = identifier;
                o.type = status;
                cursor.inner.push(o);
                o.outer = cursor;
                cursor = o;
                mode.push(status);
            }
            else if (identifier == "SHUT" || identifier == "LEFT" || identifier == "RIGHT" || identifier == "UP" || identifier == "DOWN") {
                // 小车指令
                status = "command";
                var o = operation();
                o.name = identifier;
                o.type = status;
                cursor.inner.push(o);
                o.outer = cursor;
                // 最内层
                mode.push(status);
            }
            else {
                status = undefined;
                if (identifier) {
                    alert("非法标识："+identifier+"。");
                    return false;
                }
            }
            identifier = "";
        }
    }
    return true;
}