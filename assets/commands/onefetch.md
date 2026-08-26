# TAGLINE

以 ASCII 艺术展示仓库摘要的命令行 Git 信息工具

# TLDR

**显示仓库信息**

```onefetch```

**显示特定仓库的信息**

```onefetch [/path/to/repo]```

**以 ASCII 艺术显示信息**

```onefetch --ascii-language [python]```

**禁用 ASCII 艺术**

```onefetch --no-art```

**只显示特定信息**

```onefetch --show-info [project,head,version,size]```

**隐藏特定信息**

```onefetch --hide-info [authors,commits]```

**以 JSON 输出**

```onefetch --output json```

**使用自定义图片**

```onefetch --image [/path/to/image.png]```

# SYNOPSIS

**onefetch** [_path_] [_--ascii-language lang_] [_--image file_] [_--output format_] [_options_]

# PARAMETERS

**-a**, **--ascii-language** _LANG_
> 强制使用指定语言的 ASCII 艺术。

**-i**, **--image** _FILE_
> 使用自定义图片代替 ASCII。

**--image-protocol** _PROTOCOL_
> 图片协议：sixel、kitty、iterm。

**--no-art**
> 禁用 ASCII/图片艺术。

**-o**, **--output** _FORMAT_
> 输出格式：yaml、json。

**--show-info** _FIELDS_
> 只显示指定的信息字段。

**--hide-info** _FIELDS_
> 隐藏指定的信息字段。

**--no-bold**
> 禁用粗体文本。

**--no-color-palette**
> 隐藏调色板。

**--number-of-authors** _NUM_
> 要显示的作者数量。

**--number-of-languages** _NUM_
> 要显示的语言数量。

**-e**, **--exclude** _PATTERNS_
> 忽略匹配模式的文件。

**--no-bots**
> 从统计中排除机器人提交。

**-T**, **--true-color** _WHEN_
> 真彩色：auto、always、never。

**-d**, **--disabled-fields** _FIELDS_
> --hide-info 的已弃用别名。

# DESCRIPTION

**onefetch** 是一款命令行 Git 信息工具，用代表主导编程语言的 ASCII 艺术展示仓库摘要。它专为快速概览仓库而设计，类似于用于系统信息的 neofetch。

显示内容包括：项目名称、描述、HEAD 引用、版本标签、创建日期、语言构成、作者、最近更改、仓库大小、代码行数、许可证和依赖项。

ASCII 艺术根据主导语言自动选择。内置 100 多种语言的标志。自定义图片可在支持的终端中显示（kitty、iTerm2 及支持 Sixel 的终端）。

作者统计信息展示提交数量和行数贡献。可以过滤掉机器人账户。语言检测遵循 .gitignore，还可以排除额外的模式。

输出格式（JSON、YAML）便于与其他工具集成。字段选择让你可以自定义要显示的信息，适用于不同场景或终端尺寸。

# CAVEATS

需要在 Git 仓库内运行。ASCII 艺术需要足够的终端宽度。图片显示需要兼容的终端。大型仓库分析耗时较长。某些统计需要完整的仓库历史。语言检测可能误判部分文件类型。

# HISTORY

**onefetch** 由 **Ossama Hjaji**（o2sh）自 **2019** 年前后开始开发，灵感来自 neofetch 和 screenfetch。它使用 Rust 编写，因提供美观的仓库信息展示方式而广受欢迎。该项目现已支持众多语言和终端。

# INSTALL

```dnf: sudo dnf install onefetch```

```pacman: sudo pacman -S onefetch```

```apk: sudo apk add onefetch```

```zypper: sudo zypper install onefetch```

```brew: brew install onefetch```

```nix: nix profile install nixpkgs#onefetch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[neofetch](/man/neofetch)(1), [tokei](/man/tokei)(1), [git](/man/git)(1), [cloc](/man/cloc)(1)
