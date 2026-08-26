# TAGLINE

快速跳转到常用目录

# TLDR

**跳转**到目录

```j [project]```

跳转到**子目录**

```jc [src]```

在**文件管理器**中打开目录

```jo [downloads]```

显示**统计信息**

```j --stat```

**增加**目录权重

```j -i [+10]```

# SYNOPSIS

**j** [_-i weight_] [_-d weight_] [_--stat_] [_directory_]

# DESCRIPTION

**autojump** 是一个能学习你导航习惯的 cd 替代品。它维护一个你访问过的目录数据库，让你能用部分名称快速跳转。

不必输入完整路径，只需简短易记的模式即可跳转到常用目录。

# PARAMETERS

**directory**
> 用于匹配的部分目录名。

**-a** _path_, **--add** _path_
> 手动将一个路径添加到数据库。

**-i** [_weight_], **--increase** [_weight_]
> 增加当前目录的权重。

**-d** [_weight_], **--decrease** [_weight_]
> 降低当前目录的权重。

**--complete**
> 内部使用，用于 Tab 补全。

**--purge**
> 从数据库中移除不存在的路径。

**-s**, **--stat**
> 显示数据库条目及其关键权重。

**-v**, **--version**
> 显示版本信息。

# ALIASES

- **j**: 主命令
- **jc**: 跳转到子目录
- **jo**: 在文件管理器中打开
- **jco**: 在文件管理器中打开子目录

# CAVEATS

需要 shell 集成（添加到 .bashrc/.zshrc）。数据库随使用逐步积累，新目录起初无法跳转。类似工具：z、zoxide。

# HISTORY

**autojump** 由 Joël Schaerer 于 **2009 年**前后创建，是最早面向 shell 的"frecency"（频率 + 近期度）目录跳转工具之一。

# INSTALL

```dnf: sudo dnf install autojump```

```aur: yay -S autojump```

```zypper: sudo zypper install autojump```

```brew: brew install autojump```

```nix: nix profile install nixpkgs#autojump```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[z](/man/z)(1), [zoxide](/man/zoxide)(1), [cd](/man/cd)(1)

# RESOURCES

```[Source code](https://github.com/wting/autojump)```

<!-- verified: 2026-06-17 -->
