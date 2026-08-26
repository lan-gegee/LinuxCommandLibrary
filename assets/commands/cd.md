# TAGLINE

切换当前工作目录

# TLDR

**切换**到目录

```cd [/path/to/directory]```

**前往**主目录

```cd```

**前往上一个目录**

```cd -```

**上移一级目录**

```cd ..```

**上移两级目录**

```cd ../..```

# SYNOPSIS

**cd** [**-L**|**-P** [**-e**] [**-@**]] [_directory_]

# DESCRIPTION

**cd**（change directory）是 Shell 内建命令，用于改变当前工作目录。它会更新 Shell 的当前目录和 PWD 环境变量。

该命令是在 Shell 会话中浏览文件系统的基础。

# PARAMETERS

_directory_
> 要切换到的路径（默认：$HOME）

**-**
> 切换到上一个目录（OLDPWD）

**-L**
> 跟随符号链接（默认）

**-P**
> 使用物理目录结构（不跟随符号链接）

**-e**
> 配合 -P 使用，当无法确定当前目录时以错误退出

**-@**
> 将扩展属性呈现为目录（在支持的系统上）

# SPECIAL DIRECTORIES

**~**
> 主目录（$HOME）

**~user**
> 指定用户的主目录

**.**
> 当前目录

**..**
> 父目录

**-**
> 上一个目录

# ENVIRONMENT VARIABLES

**PWD**
> 当前工作目录

**OLDPWD**
> 上一个工作目录

**HOME**
> 用户的主目录

**CDPATH**
> cd 命令的搜索路径

# CAVEATS

Shell 内建命令（行为因 Shell 而异）。路径中的空格需要加引号。符号链接可能造成困扰（-P 与 -L 的区别）。默认没有 cd 命令历史。只能 cd 到目录，不能 cd 到文件。

# HISTORY

自 **20 世纪 70 年代**最早的 Unix Shell 起，**cd** 就一直是 Shell 内建命令，是目录导航的基础。

# INSTALL

```apk: sudo apk add execline```

```brew: brew install execline```

```nix: nix profile install nixpkgs#execline```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pwd](/man/pwd)(1), [pushd](/man/pushd)(1), [popd](/man/popd)(1), [dirs](/man/dirs)(1)
