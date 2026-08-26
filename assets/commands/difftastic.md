# TAGLINE

具备语法感知能力的结构化 diff 工具

# TLDR

**比较**两个文件（语法感知 diff）

```difft [file1] [file2]```

**递归比较**文件或目录

```difft [dir1] [dir2]```

**显示**来自 git 的特定文件的变更

```difft --git [file]```

**用作** git difftool

```git difftool --tool=difftastic```

# SYNOPSIS

**difft** [_options_] [_path1_] [_path2_]

# PARAMETERS

**--color** _MODE_
> 颜色模式：auto、always、never

**--display** _MODE_
> 显示模式：side-by-side、inline 或 json

**--syntax-highlight** _MODE_
> 语法高亮：on、off

**--check-only**
> 文件不同时以状态码 1 退出

**--strip-cr**
> 比较前剥离回车符

**--context** _N_
> 显示的上下文行数

**--tab-width** _N_
> 制表符显示宽度（默认：4）

**--width** _N_
> 输出的最大显示宽度

**--list-languages**
> 打印所有支持的语言

**-h, --help**
> 显示帮助并退出

**-V, --version**
> 显示版本并退出

# DESCRIPTION

**difftastic** 是一个理解语法的结构化 diff 工具。与传统的基于行的 diff 工具不同，它按编程语言解析代码，并基于代码的实际结构展示变更。

该工具支持 20 多种编程语言，通过区分代码是被移动还是被修改来提供更准确的 diff。它既可以独立使用，也可以作为 difftool 与 git 集成。

# GIT INTEGRATION

配置为 git difftool：

```git config --global diff.tool difftastic```
```git config --global difftool.difftastic.cmd 'difft "$LOCAL" "$REMOTE"'```

配合 git 使用：

```git difftool```

# CAVEATS

处理超大文件时可能比传统 diff 工具慢。依赖的语言文法未必覆盖所有边缘情况。不支持二进制文件。嵌套极深的结构可能出现显示问题。

# HISTORY

**difftastic** 由 Wilfred Hughes 创建，旨在解决处理代码时基于行的 diff 的局限。它使用 tree-sitter 解析器构建语法树并进行结构化比较。该项目因提供更清晰、更有意义的 diff 而广受欢迎。

# INSTALL

```dnf: sudo dnf install difftastic```

```pacman: sudo pacman -S difftastic```

```zypper: sudo zypper install difftastic```

```brew: brew install difftastic```

```nix: nix profile install nixpkgs#difftastic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [git](/man/git)(1), [delta](/man/delta)(1), [diffnav](/man/diffnav)(1)
