# TAGLINE

**pacman --files** 的简写形式，查询文件数据库

# TLDR

从已配置的镜像源**刷新**文件数据库

```sudo pacman -Fy```

**查找给定文件路径所属的软件包**

```pacman -F [bin/ls]```

**列出给定软件包安装的所有文件**

```pacman -Fl [pacman]```

**搜索匹配正则表达式的文件**

```pacman -Fx '[\.so\.1$]'```

输出适合脚本的**机器可读结果**

```pacman -F [pattern] --machinereadable```

# SYNOPSIS

**pacman** **-F** [_options_] [_file_...]

# PARAMETERS

**-y**, **--refresh**
> 从服务器下载每个仓库 **.files** 数据库的最新副本。传入两次可强制下载，即使本地副本看似最新。

**-l**, **--list**
> 列出给定软件包拥有的文件。

**-x**, **--regex**
> 将查询视为 POSIX 正则表达式。

**-q**, **--quiet**
> 显示更少的输出（便于脚本处理）。

**--machinereadable**
> 以制表符分隔、适合脚本的格式输出结果。

# DESCRIPTION

**pacman -F**（等价于 **pacman --files**）查询 Arch 文件数据库，该数据库将软件包中的每个文件映射到其所属的软件包。即使软件包未安装，它也能回答经典的"哪个软件包提供 **/usr/bin/foo**？"这一问题。

文件数据库必须先用 **pacman -Fy** 下载。直接运行 **pacman -F** _pattern_ 会隐式执行文件名搜索，因此无需显式指定 **-s**。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8)
