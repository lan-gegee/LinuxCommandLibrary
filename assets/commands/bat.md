# TAGLINE

支持语法高亮和 Git 集成的 cat 克隆

# TLDR

**查看**文件并显示语法高亮

```bat [file.js]```

**显示**行号

```bat -n [file.py]```

**显示**不可打印字符

```bat -A [file.txt]```

**纯文本**输出（无装饰）

```bat -p [file.log]```

**多个文件**

```bat [file1.rs] [file2.rs]```

**指定语言**

```bat -l [python] [script]```

# SYNOPSIS

**bat** [_options_] [_file_...]

# DESCRIPTION

**bat** 是一个支持语法高亮和 Git 集成的 cat 克隆。它能自动检测语言来显示文件内容，并带有行号和边栏中的 Git diff 指示标记。

该工具为开发者和系统管理员提供了更友好的文件查看体验。

# PARAMETERS

**-n**, **--number**
> 显示行号

**-A**, **--show-all**
> 显示不可打印字符

**-p**, **--plain**
> 纯文本模式（无装饰）

**-l**, **--language** _lang_
> 指定语法高亮的语言

**-H**, **--highlight-line** _n_
> 高亮指定行

**--paging** _when_
> 何时使用分页器（auto、always、never）

**--style** _components_
> 配置输出样式

**--theme** _name_
> 配色主题

**--list-languages**
> 列出支持的语言

**--list-themes**
> 列出可用的主题

# FEATURES

- 支持 200 多种语言的语法高亮
- Git 集成（显示修改状态）
- 行号
- 不可打印字符显示
- 自动分页
- 文件拼接
- 主题支持
- 与 less 分页器集成

# CONFIGURATION

**~/.config/bat/config**
> 自动应用的默认命令行选项。每行一个选项（如 --theme、--style）。

# CAVEATS

在脚本中并非 cat 的即插即用替代品（管道中请使用 cat）。处理大文件时比 cat 慢。主题需要真彩色终端。在 Debian/Ubuntu 上，由于与其他软件包命名冲突，二进制文件安装为 **batcat**。

# HISTORY

**bat** 由 David Peter（sharkdp）于 **2018** 年创建，作为 cat 的现代替代品，提供语法高亮和 Git 感知能力。

# INSTALL

```apt: sudo apt install bat```

```dnf: sudo dnf install bat```

```pacman: sudo pacman -S bat```

```apk: sudo apk add bat```

```zypper: sudo zypper install bat```

```brew: brew install bat```

```nix: nix profile install nixpkgs#bat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cat](/man/cat)(1), [less](/man/less)(1), [highlight](/man/highlight)(1)
