# TAGLINE

Lua 语言的即时编译器

# TLDR

**启动交互式解释器**

```luajit```

**运行 Lua 脚本**

```luajit [script.lua]```

**执行一段 Lua 代码**

```luajit -e "[print('Hello')]"```

**带参数运行脚本**

```luajit [script.lua] [arg1] [arg2]```

**保存字节码**到文件

```luajit -b [script.lua] [script.out]```

**在运行脚本前加载库**

```luajit -l [library] [script.lua]```

**运行脚本后进入交互模式**

```luajit -i [script.lua]```

# SYNOPSIS

**luajit** [_options_] [_script_ [_args_]]

# PARAMETERS

**-e** _chunk_
> 运行给定的 Lua 代码块。

**-l** _library_
> 加载指定名称的库，等价于 require("library")。

**-b** _..._
> 保存或列出字节码。不带参数运行可查看选项帮助。

**-j** _command_
> 执行 LuaJIT 控制命令（例如 -jv 显示详细的跟踪信息，-jdump 输出详细的跟踪转储）。

**-O**[_opt_]
> 控制 LuaJIT 优化。-O0 禁用所有优化，-O（默认）等价于 -O3。

**-i**
> 执行脚本或代码后进入交互模式。

**-v**
> 显示 LuaJIT 版本号。

**-E**
> 忽略环境变量。

**--**
> 停止处理选项。

# DESCRIPTION

**luajit** 是 Lua 编程语言的即时（JIT）编译器。它通过基于跟踪的 JIT 编译、高效的解释器以及内置的 FFI（外部函数接口），提供比标准 Lua 解释器显著更快的执行速度。

LuaJIT 与 Lua 5.1 完全兼容，并包含若干扩展。脚本参数通过全局 `arg` 表传递。当未提供脚本或 `-e` 选项时，会自动激活交互模式。

# CAVEATS

LuaJIT 仅兼容 Lua 5.1，不兼容 Lua 5.2 及更高版本。使用 FFI 库需要了解 C 类型和原生代码。JIT 编译并非在所有架构上都可用。`-b` 字节码格式与标准 Lua 字节码不兼容。

# HISTORY

LuaJIT 由 **Mike Pall** 自 2005 年起开发。具有当前跟踪编译器架构的 LuaJIT 2.0 于 2012 年发布。

# INSTALL

```apt: sudo apt install luajit```

```dnf: sudo dnf install luajit```

```pacman: sudo pacman -S luajit```

```apk: sudo apk add luajit```

```zypper: sudo zypper install luajit```

```brew: brew install luajit```

```nix: nix profile install nixpkgs#luajit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lua](/man/lua)(1), [luac](/man/luac)(1)
