# TAGLINE

基于 frecency 的文件与目录快速导航

# TLDR

跳转到最常使用的目录

```z [pattern]```

编辑常用文件

```f [pattern]```

列出常用目录

```d```

列出常用文件

```f```

显示所有常用路径

```fasd```

交互式选择

```fasd -si [pattern]```

将路径加入数据库

```fasd -A [path]```

# SYNOPSIS

**fasd** [_options_] [_patterns_...]

# DESCRIPTION

**fasd** 提供对经常和最近使用的文件与目录的快速访问。它跟踪访问模式，并结合频率和新鲜度使用"frecency"算法排序。

该工具与 shell 集成，跟踪 cd 和文件访问行为，只需极少输入即可快速导航。z（目录）和 f（文件）等别名提供了快捷方式。

# PARAMETERS

**-s**
> 显示排名和路径。

**-l**
> 只列出路径。

**-i**
> 交互式选择。

**-e** _cmd_
> 对结果执行命令。

**-a**
> 匹配文件和目录。

**-d**
> 只匹配目录。

**-f**
> 只匹配文件。

**-r**
> 仅按排名匹配。

**-t**
> 仅按新鲜度匹配。

**-A**
> 将路径加入数据库。

**-D**
> 从数据库移除路径。

# ALIASES (shell init)

**z**: 跳转到目录 (fasd_cd -d)
**zz**: 交互式选择目录
**f**: 选择文件
**v**: 用 $EDITOR 打开常用文件

# CONFIGURATION

**~/.fasd**
> 数据库文件，记录文件和目录的 frecency 得分。

# CAVEATS

需要 shell 集成。数据库随时间积累。模式为子串匹配。可能需要手动清理旧条目。

# HISTORY

**fasd** 由 **Wei Dai**（clvv）受 autojump 和 z 启发而创建。它结合了两者特性，并增加了文件跟踪和可扩展性。该项目凭借在 shell 导航中的速度和灵活性而广受欢迎。

# INSTALL

```pacman: sudo pacman -S fasd```

```zypper: sudo zypper install fasd```

```nix: nix profile install nixpkgs#fasd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[z](/man/z)(1), [autojump](/man/autojump)(1), [zoxide](/man/zoxide)(1), [fzf](/man/fzf)(1)

# RESOURCES

```[Source code](https://github.com/clvv/fasd)```

<!-- verified: 2026-07-15 -->
