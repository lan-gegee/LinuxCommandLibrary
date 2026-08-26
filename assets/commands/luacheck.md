# TAGLINE

Lua 的静态分析器和 linter

# TLDR

**检查一个 Lua 文件**

```luacheck [file.lua]```

**递归检查目录中的所有 Lua 文件**

```luacheck [directory]```

**使用特定的 Lua 标准进行检查**

```luacheck --std [lua53] [file.lua]```

**忽略特定的警告代码**

```luacheck --ignore [211] [file.lua]```

**检查并在输出中显示警告代码**

```luacheck --codes [file.lua]```

**以指定格式输出**

```luacheck --formatter [TAP|JUnit|plain|visual_studio] [file.lua]```

**并行检查多个文件**

```luacheck -j [4] [file1.lua] [file2.lua]```

**从标准输入检查并使用自定义文件名**

```cat [file.lua] | luacheck --filename [file.lua] -```

# SYNOPSIS

**luacheck** [_options_] _files_...

# PARAMETERS

**--std** _std_
> 设置标准全局变量集（lua51、lua52、lua53、lua54、luajit、ngx_lua、love、busted、min、max、none）。

**-g**, **--no-global**
> 排除关于全局变量的警告。

**-u**, **--no-unused**
> 排除关于未使用变量和值的警告。

**-r**, **--no-redefined**
> 排除关于重复定义变量的警告。

**-a**, **--no-unused-args**
> 排除关于未使用参数和循环变量的警告。

**-s**, **--no-unused-secondaries**
> 排除关于与已用变量一同设置却未使用的变量的警告。

**-d**, **--allow-defined**
> 允许通过赋值隐式定义全局变量。

**-t**, **--allow-defined-top**
> 仅允许在顶层作用域隐式定义全局变量。

**-i**, **--ignore** _patt_ ...
> 过滤掉匹配模式的警告。

**-o**, **--only** _patt_ ...
> 只显示匹配模式的警告。

**-e**, **--enable** _patt_ ...
> 重新启用匹配模式的警告。

**--globals** _names_ ...
> 添加自定义的允许全局变量。

**--read-globals** _names_ ...
> 添加只读全局变量。

**--max-line-length** _length_
> 设置最大行长度（默认：120）。使用 **--no-max-line-length** 可禁用。

**--max-cyclomatic-complexity** _limit_
> 设置函数的最大圈复杂度。

**--formatter** _fmt_
> 输出格式（default、TAP、JUnit、visual_studio、plain）。

**--codes**
> 在输出中显示警告代码。

**--ranges**
> 显示警告的列范围。

**-q**, **--quiet**
> 抑制无警告文件的输出。使用 **-qq** 或 **-qqq** 可进一步减少输出。

**-j**, **--jobs** _num_
> 并行检查文件（需要 LuaLanes）。

**--cache** [_file_]
> 启用结果缓存（默认：.luacheckcache）。

**--config** _file_
> 自定义配置文件路径（默认：.luacheckrc）。

**--no-config**
> 禁用配置文件加载。

**--no-color**
> 禁用彩色输出。

**--exclude-files** _glob_ ...
> 跳过匹配这些 glob 模式的文件。

**--include-files** _glob_ ...
> 只检查匹配这些 glob 模式的文件。

# DESCRIPTION

**luacheck** 是 Lua 的静态分析器和 linter。它能检测多种问题，包括未定义的全局变量、未使用的变量、不可达代码以及风格问题。

luacheck 支持多个 Lua 版本，可以通过项目内的 **.luacheckrc** 文件或行内注释进行配置。

# CONFIGURATION

```lua
-- .luacheckrc
std = "lua53"
globals = {"myGlobal"}
ignore = {"212"}  -- unused argument
max_line_length = 120
```

# CAVEATS

仅为静态分析；无法捕获运行时错误。对动态代码可能产生误报。使用 **-j** 并行检查需要 LuaLanes 库。

# HISTORY

luacheck 由 **Peter Melnichenko** 创建，是一个全面的 Lua 静态分析工具，填补了 Lua 缺乏 linting 工具的空白。

# INSTALL

```pacman: sudo pacman -S luacheck```

```apk: sudo apk add luacheck```

```brew: brew install luacheck```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lua](/man/lua)(1), [luac](/man/luac)(1), [selene](/man/selene)(1), [stylua](/man/stylua)(1)
