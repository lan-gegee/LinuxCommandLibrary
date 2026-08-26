# TAGLINE

支持 Lua 脚本与结构化管道的 Linux shell

# TLDR

**启动交互式 wisp 会话**

```wisp```

**执行一条 shell 命令字符串后退出**

```wisp -c "[ls | wc -l]"```

**执行一个 Lua 表达式后退出**

```wisp -e "[for i=1,5 do print(i) end]"```

**运行 Lua 脚本文件**

```wisp -f [script.lua]```

**在提示符中求值 Lua**（前导冒号）

```:print(42 * 10)```

**将任务放入后台并列出任务**（在 wisp 内）

```sleep 30 &```

```jobs```

# SYNOPSIS

**wisp** [_-c command_] [_-e lua_] [_-f file_]

# PARAMETERS

**-c** _command_
> 执行一条 shell 语法的命令行后退出。前导 **:** 会把字符串切换为 Lua。

**-e** _lua_
> 执行一个 Lua 表达式或代码块后退出。

**-f** _file_
> 运行 Lua 脚本文件（也可通过 shebang `#!/usr/bin/env wisp` 使用）。

# CONFIGURATION

**~/.config/wisp/init.lua**
> 启动时加载的用户配置。在此定义的任何全局 Lua 函数都可以按名称作为 shell 命令调用。定义 **prompt()** 可定制交互式提示符。可复制仓库中的 **example-init.lua** 作为起点。

# DESCRIPTION

**wisp** 是一个 Linux shell，它使用 **Lua**（而非自定义 DSL）进行配置和脚本编写，并且可以在相邻的管道阶段之间传递结构化数据（Lua 表），而不仅仅是文本。

裸提示符行使用普通的 shell 语法：外部命令、管道、重定向（`<` `>` `>>` `2>` `2>&1` `&>`）、后台任务（`&`）、环境变量赋值、引号、花括号展开和通配符匹配。支持作业控制（`Ctrl-Z`、`fg`、`bg`、`jobs`、`kill %N`、`disown`、`wait`）。Tab 补全覆盖内建命令、Lua 函数、`$PATH` 可执行文件和文件名；**Ctrl-R** 为反向历史搜索。

以 **:** 开头的行会按 Lua 求值。构成"原生运行"的用户自定义 Lua 函数和内建命令会留在进程内，直接串联 Lua 值（例如表列表）而不 fork。当管道阶段是真正的外部二进制程序时，wisp 会 fork，并在该边界处进行结构化值与字节之间的转换。

内建命令包括 **cd**、**pwd**、**echo**、**export**、**command**、**type**、**source**、**jobs**、**fg**、**bg**、**kill**、**disown**、**wait**、**exit** 和 **pkg**（LuaRocks 的轻量前端，需要 `$PATH` 中有 **luarocks**）。

构建需要 **Lua 5.4** 开发头文件（Debian/Ubuntu 上为 `liblua5.4-dev`，Arch 上为 `lua5.4`）。安装方式为 `make && sudo make install`（默认 `/usr/local/bin/wisp`），或 `lua bootstrap.lua build`。

# CAVEATS

专注 Linux；不是完整的 POSIX shell。没有 shell 语法的 `if`/`while`/`for`、heredoc 或 `$1`..`$9` 位置参数——控制流应写在 Lua 中。对展开结果的分词不是 POSIX 风格（带空格的非引用 `$VAR` 仍是一个参数）。不对 `init.lua` 做沙箱隔离（信任模型与 `.bashrc` 相同）。将全原生管道放入后台是无效操作。可选的 **pkg** 需要单独安装 LuaRocks。

# HISTORY

**wisp** 是一个 Lua 原生的 Linux shell，强调结构化管道和真正的作业控制。上游维护于 **github.com/Hinikaa/wisp**，采用 MIT 许可证（内置的 **linenoise** 为 BSD-2-Clause）。

# SEE ALSO

[bash](/man/bash)(1), [zsh](/man/zsh)(1), [fish](/man/fish)(1), [nushell](/man/nushell)(1), [lua](/man/lua)(1)

# RESOURCES

```[Source code](https://github.com/Hinikaa/wisp)```

<!-- verified: 2026-08-01 -->
