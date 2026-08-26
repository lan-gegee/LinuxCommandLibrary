# TAGLINE

直接作用于软件包数据库，允许修改软件包属性

# TLDR

标记为**依赖**

```sudo pacman -D --asdeps package```

标记为**显式**安装

```sudo pacman -D --asexplicit package```

**检查**依赖

```pacman -Dk```

检查**同步**数据库

```pacman -Dkk```

以**安静**模式检查

```pacman -Dkq```

# SYNOPSIS

**pacman -D** [_OPTIONS_] [_PACKAGE_...]

# DESCRIPTION

**pacman -D**（database）直接作用于软件包数据库，无需重新安装即可修改软件包属性。它可以更改安装原因并验证数据库完整性。

# PARAMETERS

**-D, --database**
> 作用于软件包数据库

**--asdeps**
> 将软件包标记为作为依赖安装

**--asexplicit**
> 将软件包标记为显式安装

**-k, --check**
> 检查本地数据库的一致性

**-kk**
> 同时检查同步数据库

**-q, --quiet**
> 抑制正常输出，仅显示错误

# CAVEATS

错误的标记会影响孤儿软件包检测。使用 **--asdeps** 时要小心，这些软件包在清理孤儿时可能被移除。双重的 **-k** 会执行更彻底的检查（包括同步数据库）。

# HISTORY

**pacman** 是 **Arch Linux** 及其衍生发行版的软件包管理器。

# SEE ALSO

[pacman](/man/pacman)(8), [pacman-query](/man/pacman-query)(8)
