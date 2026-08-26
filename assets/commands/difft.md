# TAGLINE

理解语法的结构化 diff 工具

# TLDR

**比较两个文件**（结构化 diff）

```difft [old_file] [new_file]```

**以并排方式**比较文件

```difft --display side-by-side [old_file] [new_file]```

**只显示变更的行**（inline 显示）

```difft --display inline [old_file] [new_file]```

使用指定的语言进行解析并**比较**

```difft --language [rust] [old.rs] [new.rs]```

**比较目录**

```difft [old_directory] [new_directory]```

**配合 git diff 使用**

```git diff --external-diff difft```

**设为默认的 git diff 工具**

```git config --global diff.external difft```

**比较并跳过未变更的部分**

```difft --skip-unchanged [old_file] [new_file]```

# SYNOPSIS

**difft** [_options_] _old_path_ _new_path_

# PARAMETERS

**--display** _mode_
> 输出格式：side-by-side、side-by-side-show-both、inline（默认）。

**--language** _lang_
> 强制使用指定的语言解析器（默认自动检测）。

**--list-languages**
> 显示所有支持的语言。

**--skip-unchanged**
> 不显示文件中未变更的部分。

**--context** _n_
> 上下文行数（默认：3）。

**--width** _n_
> 最大显示宽度（默认：终端宽度）。

**--color** _when_
> 彩色输出：always、never、auto。

**--background** _type_
> 背景色：light、dark（默认：dark）。

**--syntax-highlight** _on|off_
> 启用或禁用语法高亮。

**--tab-width** _n_
> 制表符显示宽度（默认：4）。

**--parse-error-limit** _n_
> 回退到文本 diff 前允许的最大解析错误数。

**--byte-limit** _n_
> 跳过超过此大小的文件。

**--graph-limit** _n_
> 结构化 diff 算法的最大图规模。

**--exit-code**
> 存在语法层面的变更时将退出码设为 1（脚本中很有用）。

# DESCRIPTION

**difft**（Difftastic）是一个理解编程语言语法的结构化 diff 工具。与基于行的 diff 工具不同，它解析源代码并比较实际结构，显示有意义的变更而忽略格式差异。

该工具为文件的两个版本分别构建抽象语法树（AST），然后计算最小的结构差异。这意味着当代码只是被移动或重构而没有实质改变时，它不会标记差异；纯空白或格式变化也会被忽略。

Difftastic 支持 30 多种编程语言，使用 tree-sitter 提供专用解析器。对于不支持的文件，它会回退到基于文本的 diff。语言检测基于文件扩展名自动完成。

并排显示以并行列展示新旧版本，用颜色表示新增（绿色）、删除（红色）和修改。inline 显示则以更紧凑的方式呈现变更。Git 集成允许将 difft 用作外部 diff 工具。

# CAVEATS

大文件或差异极大的结构可能触及性能上限。解析错误会导致回退到文本 diff。某些语言特性可能无法完美解析。极其复杂的结构性变更可能产生难以阅读的输出。

# HISTORY

**Difftastic** 由 Wilfred Hughes 于 **2020** 年起开发。其目的是解决基于行的 diff 的局限——这类工具在处理重构或重排格式的变更时常常产生大量噪音。该工具使用 tree-sitter 解析器进行语言感知的结构比较，作为 git diff 替代品广受欢迎。

# INSTALL

```dnf: sudo dnf install difftastic```

```pacman: sudo pacman -S difftastic```

```apk: sudo apk add difftastic```

```zypper: sudo zypper install difftastic```

```brew: brew install difftastic```

```nix: nix profile install nixpkgs#difftastic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [git-diff](/man/git-diff)(1), [delta](/man/delta)(1), [colordiff](/man/colordiff)(1)
