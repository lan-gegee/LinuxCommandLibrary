# TAGLINE

Helix 编辑器的命令

# TLDR

**打开文件**

```hx [file]```

在指定行打开文件

```hx [file]:[line]```

**打开多个文件**

```hx [file1] [file2]```

**检查语言支持情况**

```hx --health [language]```

**打开教程**

```hx --tutor```

将所有给定文件**拆分为垂直窗口**

```hx --vsplit [file1] [file2]```

# SYNOPSIS

**hx** [_options_] [_files_]...

# PARAMETERS

_FILES_
> 要编辑的文件，可选地以 **:LINE** 或 **:LINE:COLUMN** 后缀指定位置。

**+**_N_
> 在第 _N_ 行打开第一个给定文件。

**--tutor**
> 打开交互式教程。

**--health** [_CATEGORY_]
> 检查配置问题；_CATEGORY_ 可以是语言名称，或 clipboard、languages、all-languages、all。

**-c**, **--config** _FILE_
> 要使用的配置文件。

**-g**, **--grammar** {**fetch**|**build**}
> 拉取或构建 tree-sitter 语法。

**-w**, **--working-dir** _PATH_
> 初始工作目录。

**--vsplit** / **--hsplit**
> 将所有给定文件垂直/水平拆分到独立窗口。

**--strict**
> 对于可能失败的命令直接报错退出。

**--log** _FILE_
> 用于记录日志的文件。

**-v**
> 增加日志详细程度（可重复使用）。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 打印版本信息。

# DESCRIPTION

**hx** 是 Helix 编辑器的命令。Helix 是一款后现代模态编辑器，内置 LSP 支持和 tree-sitter 集成。

该编辑器采用受 Kakoune 启发的选择优先编辑模型。它开箱即用地提供语法高亮、补全和诊断功能。

# CAVEATS

与 Vim 的模式不同，新用户需要学习曲线。基于 Rust 编写。

# HISTORY

Helix 作为一款现代终端编辑器而诞生，设计灵感来自 **Kakoune** 和 **Neovim**。

# INSTALL

```apt: sudo apt install hx```

```dnf: sudo dnf install helix```

```pacman: sudo pacman -S helix```

```apk: sudo apk add helix```

```zypper: sudo zypper install helix```

```brew: brew install hx```

```nix: nix profile install nixpkgs#helix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[helix](/man/helix)(1), [vim](/man/vim)(1), [nvim](/man/nvim)(1)

# RESOURCES

```[Source code](https://github.com/helix-editor/helix)```

```[Homepage](https://helix-editor.com)```

```[Documentation](https://docs.helix-editor.com)```

<!-- verified: 2026-07-19 -->
