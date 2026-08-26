# TAGLINE

学习目录使用习惯的更智能 cd 命令

# TLDR

**跳转到匹配模式的排名最高的目录**

```z [pattern]```

**跳转到匹配多个模式的目录**

```z [foo] [bar]```

**用 fzf 交互式选择**

```zi [pattern]```

**向数据库添加目录**

```zoxide add [/path/to/dir]```

**从数据库移除目录**

```zoxide remove [/path/to/dir]```

**列出所有条目**

```zoxide query -l```

**显示条目得分**

```zoxide query -ls```

**生成 Shell 初始化代码（加入 shell 配置）**

```eval "$(zoxide init [bash|zsh|fish])"```

# SYNOPSIS

**zoxide** _subcommand_ [_options_] [_arguments_]

**z** [_pattern_...]

**zi** [_pattern_...]

# SUBCOMMANDS

**add** _path_
> 将目录加入数据库

**edit**
> 交互式编辑数据库

**import** _file_
> 从 autojump/z 数据库导入

**init** _shell_
> 生成 Shell 初始化代码

**query** [_pattern_...]
> 搜索数据库

**remove** _path_
> 从数据库移除目录

# 参数（query）

**-l**, **--list**
> 列出所有匹配而不是选择最佳匹配

**-s**, **--score**
> 在结果中显示得分

**-i**, **--interactive**
> 交互式选择（需要 fzf）

**--exclude** _path_
> 从结果中排除指定路径

# DESCRIPTION

**zoxide** 是一个会学习你使用习惯的更智能 cd 命令。它记录目录访问情况，并按 frecency（频率 + 新近度）为目录排序，只需极少输入即可快速跳转。

完成 shell 集成后，**z foo** 会跳转到最可能包含 "foo" 的目录。多个模式可以收窄结果：**z foo bar** 会按顺序查找同时包含这两个模式的路径。

当存在多个匹配时，**zi** 命令会打开 fzf 进行交互式选择。

Shell 初始化：将 **eval "$(zoxide init bash)"**（或 zsh、fish 等）加入你的 shell 配置文件。

zoxide 是 **autojump** 和 **z.sh** 更快、更现代的替代品，用 Rust 编写。

# CAVEATS

必须先完成 shell 初始化，才能记录目录并提供 z/zi 命令。

数据库需要时间学习你的行为模式。刚安装时效果有限。

交互模式需要已安装 fzf。

与 **z** shell 插件不是同一个东西，但可以导入它的数据库。

# INSTALL

```apt: sudo apt install zoxide```

```dnf: sudo dnf install zoxide```

```pacman: sudo pacman -S zoxide```

```apk: sudo apk add zoxide```

```zypper: sudo zypper install zoxide```

```brew: brew install zoxide```

```nix: nix profile install nixpkgs#zoxide```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cd](/man/cd)(1), [z](/man/z)(1), [autojump](/man/autojump)(1), [fzf](/man/fzf)(1)
