# TAGLINE

将 Lua 源代码编译为字节码

# TLDR

**将 Lua 脚本编译为字节码**

```luac -o [output.luac] [script.lua]```

**编译多个脚本**

```luac -o [combined.luac] [script1.lua] [script2.lua]```

**仅解析并做语法检查**

```luac -p [script.lua]```

**列出编译后的字节码**

```luac -l [script.lua]```

**列出并附完整调试信息**

```luac -l -l [script.lua]```

**从输出中剥离调试信息**

```luac -s -o [stripped.luac] [script.lua]```

**显示版本号**

```luac -v```

# SYNOPSIS

**luac** [_-o output_] [_-l_] [_-p_] [_-s_] [_files_]

# PARAMETERS

**-o** _FILE_
> 将编译后的字节码输出到文件。

**-l**
> 列出字节码（使用两次可获得更多细节）。

**-p**
> 仅解析，不生成输出。

**-s**
> 剥离调试信息。

**-v**
> 打印版本号。

**--**
> 停止处理选项。

# DESCRIPTION

**luac** 将 Lua 源代码编译为字节码。编译后的输出加载更快，并且可以在不发布源代码的情况下分发。

使用 -p 进行语法检查可以在不生成输出的情况下验证脚本。这在构建流程和 CI 流水线中可用于尽早发现错误。

列表选项（-l）会显示字节码指令，有助于理解 Lua 的虚拟机以及调试编译问题。双重 -l 还会添加局部变量和 upvalue 信息。

剥离调试信息（-s）可减小文件体积，但会移除行号和局部变量名，使调试更困难。适合在对体积敏感的生产部署中使用。

多个输入文件会合并为单个输出块。执行时，每个文件的代码按顺序运行。

字节码格式与特定版本绑定，在不同 Lua 版本之间不可移植。Lua 5.1、5.2、5.3 和 5.4 的字节码格式互不兼容。

# CAVEATS

字节码在 Lua 版本间不可移植。剥离调试信息会导致无法生成有意义的栈回溯。字节序和整数大小可能影响可移植性。LuaJIT 使用不同的字节码格式。

# HISTORY

**luac** 自早期版本起就是 **Lua** 的一部分，由巴西的 **PUC-Rio**（里约热内卢天主教大学）开发。Lua 由 **Roberto Ierusalimschy**、**Waldemar Celes** 和 **Luiz Henrique de Figueiredo** 自 **1993 年**起创建。该编译器至今仍是预编译 Lua 代码的标准工具。

# INSTALL

```apk: sudo apk add lua5.1```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lua](/man/lua)(1), [luajit](/man/luajit)(1)
