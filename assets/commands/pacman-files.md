# TAGLINE

查询文件数据库以找出哪些软件包拥有特定文件

# TLDR

**更新**文件数据库

```sudo pacman -Fy```

**查找**拥有某文件的软件包

```pacman -F filename```

用**正则表达式**查找

```pacman -Fx 'regex'```

仅列出软件包**名称**

```pacman -Fq filename```

**列出**软件包内的文件

```pacman -Fl package```

# SYNOPSIS

**pacman -F** [_OPTIONS_] [_FILE_...]

# DESCRIPTION

**pacman -F**（files）查询文件数据库以找出哪些软件包拥有特定文件，或列出软件包中包含的文件。这对尚未安装的软件包同样有效。

# PARAMETERS

**-F, --files**
> 查询文件数据库

**-y, --refresh**
> 从服务器下载最新的文件数据库

**-l, --list**
> 列出指定软件包拥有的文件

**-x, --regex**
> 将搜索模式解释为正则表达式

**-q, --quiet**
> 只显示软件包名称而不显示仓库

# CAVEATS

文件数据库需要用 **-Fy** 与同步数据库分开更新。该数据库可能很大，更新可能耗时。要查找已安装软件包中的文件，请改用 **pacman -Qo**。

# HISTORY

**pacman** 是 **Arch Linux** 及其衍生发行版的软件包管理器。文件数据库功能支持在所有可用软件包中搜索文件。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pacman-query](/man/pacman-query)(8), [pkgfile](/man/pkgfile)(1)
