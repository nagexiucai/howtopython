function SyntaxPaser(text) {
    var code = text || "";
    function operation() {
        return {
            "__version__": "0.0.1",
            "name": undefined,
            "type": undefined,
            "level": undefined,
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
            o.level = level;
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
                o.level = level;
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
                o.level = level;
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
                o.level = level;
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
                o.level = level;
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
                o.level = level;
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
                o.level = level;
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
    return ast;
}

function CarVM() {
    return {
        __version__: "0.0.1",
        __count__: 0,
        __trace__: [],
        __thelast__: {},
        IsHole: function(side) {},
        IsWall: function(side) {},
        IsEnd: function() {},
        Echo: function(message) {},
        LEFT: function() {},
        RIGHT: function() {},
        UP: function() {},
        DOWN: function() {},
        $: function(what) {},
        interpret: function(ast) {
            if (ast.type == "module") { /* 命名空间 */ }
            else if (ast.type == "command") {
                if (ast.name == "LEFT") {
                    console.log("LEFT");
                    return true;
                }
                else if (ast.name == "RIGHT") {
                    console.log("RIGHT");
                    return true;
                }
                else if (ast.name == "UP") {
                    console.log("UP");
                    return true;
                }
                else if (ast.name == "DOWN") {
                    console.log("DOWN");
                    return true;
                }
                else if (ast.name == "SHUT") {
                    return null;
                }
                else {
                    alert("不支持的指令："+ast.name+"！");
                    return undefined;
                }
            }
            else if (ast.type == "goon") {
                return "revolve"; // 找最近的REVOLVE标识
            }
            else if (ast.type == "revolve") {
                var i = 0;
                while (i<ast.inner.length) {
                    var how = this.interpret(ast.inner[i]);
                    i += 1;
                    if (how == "revolve") {
                        i = 0;
                        return "fuck";
                        // continue; // 破除独占
                    }
                    if (how == null) return null;
                    if (how == undefined) return undefined;
                }
            }
            else if (ast.type == "function") {
                // 函数调用
                console.log(ast.name+"("+ast.parameters.toString()+")");
                // 嵌套
                return false;
            }
            else if (ast.type == "if") {
                // 条件判断：真则递归、假则返回。
                if (ast.parameters) {
                    if (this.interpret(ast.parameters[0])) {
                        this.__thelast__[ast.level] = true;
                        // 交给兜底处理
                    }
                    else {
                        this.__thelast__[ast.level] = false;
                        return false; // 分支不符
                    }
                }
                else {
                    alert("不支持的语法：IF {...}！");
                    return undefined;
                }
            }
            else if (ast.type == "elseif") {
                // 上次判断结果：真则按兵不动、假则条件判断。
                if (this.__thelast__[ast.level] == undefined || this.__thelast__[ast.level]) {
                    return false; // 跳过
                }
                else {
                    if (ast.parameters) {
                        if (this.interpret(ast.parameters[0])) {
                            this.__thelast__[ast.level] = true;
                            // 交给兜底处理
                        }
                        else {
                            this.__thelast__[ast.level] = false;
                            return false; // 分支不符
                        }
                    }
                    else {
                        alert("不支持的语法：IF {...}！");
                        return undefined;
                    }
                }
            }
            else if (ast.type == "else") {
                // 交给兜底处理
            }
            else {
                alert("不支持的操作："+ast.type+"！");
                return undefined;
            }
            // 兜底
            for (var i=0; i<ast.inner.length; i++) {
                var how = this.interpret(ast.inner[i]);
                if (how == "revolve") return how; // 溯源
                if (how == null) return null;
                if (how == undefined) return undefined;
            }
            return true; // 分支复合并已执行
        }
    };
}