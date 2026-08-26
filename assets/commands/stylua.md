# TAGLINE

有主见的 Lua 代码格式化工具

# TLDR

**格式化文件**

```stylua [script.lua]```

**格式化多个文件**

```stylua [file1.lua] [file2.lua]```

**格式化目录**

```stylua [src/]```

**检查格式**（不修改）

```stylua --check [script.lua]```

**显示差异**（不修改）

```stylua --diff [script.lua]```

**从 stdin 格式化**

```cat [script.lua] | stylua -```

**使用指定配置**

```stylua --config [stylua.toml] [script.lua]```

# SYNOPSIS

**stylua** [_--check_] [_--diff_] [_--config file_] [_options_] [_files_]

# PARAMETERS

**--check**
> 只检查而不格式化。

**--diff**
> 显示差异而不格式化。

**--config** _FILE_
> 配置文件。

**--search-parent-directories**
> 在父目录中查找配置。

**--stdin-filepath** _PATH_
> stdin 输入对应的路径。

**--column-width** _N_
> 行宽。

**--indent-type** _TYPE_
> 制表符或空格。

**--indent-width** _N_
> 缩进宽度。

**--line-endings** _TYPE_
> Unix 或 Windows。

**--quote-style** _STYLE_
> 字符串引号风格。

**--call-parentheses** _STYLE_
> 调用圆括号风格。

**-g**, **--glob** _PATTERN_
> 用于过滤文件的通配符模式。使用 -- 将通配符模式与文件参数分隔开。

**--verify**
> 通过重新解析格式化后的代码来验证输出，确保没有引入语法错误。

**--syntax** _SYNTAX_
> Lua 语法版本：All（默认）、Lua51、Lua52、Lua53、Lua54、LuaJIT、Luau、CfxLua。

**--respect-ignores**
> 即使文件是直接在命令行传入的，也遵守 .styluaignore 规则。

**-v**, **--verbose**
> 详细输出。

# DESCRIPTION

**stylua** 根据可配置的风格规则格式化 Lua 代码。它自动强制一致的代码格式。

配置写在 stylua.toml 或 .stylua.toml 中，用于设定项目偏好。选项包括缩进、行宽、引号风格等。如果找不到配置文件，StyLua 还会检查 .editorconfig 文件。

检查模式验证格式但不做更改。如果文件需要重新格式化，它返回非零退出码，适合在 CI 中使用。

差异模式显示将要发生的更改。这有助于在应用之前审阅格式调整。

该格式化器支持多种 Lua 版本，并可通过 --syntax 标志或配置文件中的 syntax 选项针对 Roblox Luau 等游戏专用变体进行配置。

与编辑器集成可实现保存时自动格式化。CI 集成确保各贡献者的风格一致。可以使用 .styluaignore 文件（语法类似 .gitignore）将文件排除在格式化之外。

# CONFIGURATION

**stylua.toml** 或 **.stylua.toml**
> 项目配置文件，指定列宽、缩进类型、引号风格和调用圆括号行为等格式化规则。

**.styluaignore**
> 忽略文件，采用类似 .gitignore 的语法，用于将文件排除在格式化之外。

# CAVEATS

某些风格偏好无法配置。复杂表达式的格式化结果可能出乎意料。列宽只是换行的参考值，并非硬性限制。

# HISTORY

**StyLua** 由 **JohnnyMorganz** 于 **2020 年**前后创建。它以 Rust 编写，提供快速、有主见的 Lua 格式化，类似于 JavaScript 界的 Prettier。

# INSTALL

```pacman: sudo pacman -S stylua```

```apk: sudo apk add stylua```

```brew: brew install stylua```

```nix: nix profile install nixpkgs#stylua```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lua](/man/lua)(1), [luacheck](/man/luacheck)(1), [selene](/man/selene)(1)
