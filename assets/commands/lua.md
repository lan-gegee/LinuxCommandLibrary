# TAGLINE

编程语言解释器

# TLDR

**启动交互式解释器**

```lua```

**运行脚本**

```lua [script.lua]```

**执行代码**

```lua -e "[print('Hello')]"```

**带参数运行**

```lua [script.lua] [arg1] [arg2]```

**显示版本号**

```lua -v```

**脚本执行后进入交互模式**

```lua -i [script.lua]```

# SYNOPSIS

**lua** [_options_] [_script_] [_args_]

# PARAMETERS

_SCRIPT_
> Lua 脚本文件。

_ARGS_
> 脚本参数。

**-e** _CODE_
> 执行字符串。

**-i**
> 脚本执行后进入交互模式。

**-l** _MODULE_
> 加载（require）模块。

**-v**
> 显示版本信息。

**-W**
> 开启警告。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lua** 是 Lua 编程语言的解释器。Lua 是一种轻量、高性能、可嵌入的脚本语言，专为扩展应用程序而设计。它具有自动内存管理、一等函数以及简单而强大的数据组织机制（表）。

解释器可以运行 Lua 脚本，并提供用于测试代码的交互式 REPL。Lua 广泛用于游戏脚本（魔兽世界、Roblox）、嵌入式系统、配置文件（Neovim、经 OpenResty 的 Nginx），以及 Redis 和 Wireshark 等应用的扩展语言。

# CAVEATS

存在多个版本（5.1–5.4）。版本之间存在部分不兼容。各处的嵌入方式也不尽相同。

# HISTORY

Lua 于 1993 年诞生于巴西的 **PUC-Rio**，被设计为轻量的可嵌入脚本语言。

# INSTALL

```dnf: sudo dnf install lua```

```pacman: sudo pacman -S lua```

```apk: sudo apk add lua5.1```

```brew: brew install lua```

```nix: nix profile install nixpkgs#lua```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[luajit](/man/luajit)(1), [luac](/man/luac)(1)
