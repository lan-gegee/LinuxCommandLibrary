# TAGLINE

受 Kakoune 和 Vim 启发的后现代模态文本编辑器

# TLDR

**打开文件**

```hx [file]```

**在指定行打开**

```hx [file]:[line]```

**打开多个文件**

```hx [file1] [file2]```

**检查健康状态**

```hx --health```

**打开教程**

```hx --tutor```

**在指定工作目录中打开文件**

```hx -w [path/to/project] [file]```

# SYNOPSIS

**hx** [_options_] [_files_]...

# PARAMETERS

_FILES_
> 要编辑的文件，可选择以 **:LINE** 或 **:LINE:COLUMN** 作为后缀。

**+**_N_
> 在第 _N_ 行打开第一个给定的文件（若省略 _N_ 则为最后一行）。

**--health** [_CATEGORY_]
> 检查潜在的配置问题；_CATEGORY_ 可以是语言名称，或 clipboard、languages、all-languages、all 之一。

**--tutor**
> 打开交互式教程。

**-g**, **--grammar** {**fetch**|**build**}
> 获取或构建 languages.toml 中列出的 tree-sitter 语法。

**-c**, **--config** _FILE_
> 指定要使用的配置文件。

**--log** _FILE_
> 指定用于记录日志的文件。

**-w**, **--working-dir** _PATH_
> 指定初始工作目录。

**--vsplit**
> 将所有给定文件垂直拆分到独立窗口。

**--hsplit**
> 将所有给定文件水平拆分到独立窗口。

**--strict**
> 对可能失败的命令直接报错退出。

**-v**
> 提高日志详细程度（可重复使用，最多 3 次）。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 输出版本信息。

# DESCRIPTION

**Helix** 是一款受 Kakoune 和 Vim 启发的后现代模态文本编辑器。它具有多重选区、内置 LSP 支持以及 tree-sitter 集成等特性。

该编辑器开箱即用地提供语法高亮、自动补全和诊断功能。它采用"先选区后操作"的模型，而不是"动词—宾语"模式。

# CAVEATS

按键绑定与 Vim 不同。选区模型存在学习曲线。基于 Rust 编写，需要编译。

# HISTORY

**Helix** 由 **Blaž Hrastnik** 于 2020 年启动，2021 年首次公开发布。与 Vim/Neovim 不同，它自带合理的默认配置，内置基于 tree-sitter 的语法分析和 LSP 支持（而非通过插件添加），并采用 Kakoune 的"选区优先"（先选择、后操作）的编辑模型。

# INSTALL

```dnf: sudo dnf install helix```

```pacman: sudo pacman -S helix```

```zypper: sudo zypper install helix```

```brew: brew install helix```

```nix: nix profile install nixpkgs#helix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hx](/man/hx)(1), [vim](/man/vim)(1), [nvim](/man/nvim)(1), [kakoune](/man/kakoune)(1)

# RESOURCES

```[Source code](https://github.com/helix-editor/helix)```

```[Homepage](https://helix-editor.com)```

```[Documentation](https://docs.helix-editor.com)```

<!-- verified: 2026-07-19 -->
