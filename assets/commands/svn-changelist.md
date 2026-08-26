# TAGLINE

对 Subversion 工作副本文件进行分组

# TLDR

**将文件添加到 changelist**

```svn changelist [mychangelist] [file1] [file2]```

**从 changelist 中移除文件**

```svn changelist --remove [file1]```

**列出 changelist 中的文件**

```svn status --changelist [mychangelist]```

**提交指定的 changelist**

```svn commit --changelist [mychangelist]```

# SYNOPSIS

**svn changelist** _name_ _targets_...

# PARAMETERS

_name_
> Changelist 名称。

_targets_
> 要加入 changelist 的文件。

**--remove**
> 从 changelist 中移除。

**--depth** _depth_
> 操作深度：empty、files、immediates、infinity。

**--targets** _file_
> 从文件读取目标路径，每行一个。

**--quiet**, **-q**
> 抑制常规输出。

# DESCRIPTION

**svn changelist**（别名：**cl**）将工作副本中的文件组织成名为 changelist 的命名分组。这样可以针对文件子集执行选择性提交等操作，而不影响其他已修改的文件。一个文件同一时间只能属于一个 changelist。

Changelist 纯粹是客户端侧的组织机制，不影响软件仓库。它们在工作副本操作中持续存在，直到被显式移除。

# CAVEATS

Changelist 只适用于文件，不适用于目录。一个文件最多属于一个 changelist。Changelist 仅存在于本地工作副本中，不会与其他用户共享。

# INSTALL

```apt: sudo apt install subversion```

```dnf: sudo dnf install subversion```

```pacman: sudo pacman -S subversion```

```apk: sudo apk add subversion```

```zypper: sudo zypper install subversion```

```brew: brew install subversion```

```nix: nix profile install nixpkgs#subversion```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[svn](/man/svn)(1), [svnadmin](/man/svnadmin)(1)
