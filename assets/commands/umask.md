# TAGLINE

设置默认的文件创建权限掩码

# TLDR

**显示当前掩码**

```umask```

**以符号形式显示**

```umask -S```

**设置掩码**

```umask [022]```

**严格的掩码**

```umask [077]```

**宽松的掩码**

```umask [000]```

**设置符号掩码**

```umask u=rwx,g=rx,o=rx```

# SYNOPSIS

**umask** [_-S_] [_mode_]

# PARAMETERS

**-S**
> 以符号形式输出。

_mode_
> 八进制掩码值。

# DESCRIPTION

**umask** 是一个 shell 内建命令，用于设置或显示文件创建掩码，该掩码控制新建文件和目录所分配的默认权限。掩码指定从最大默认权限（文件为 666，目录为 777）中移除哪些权限位。

例如，umask 为 022 会移除组和其他用户的写权限，使创建的文件权限为 644、目录为 755。更严格的 umask 077 则移除组和其他用户的所有权限。

umask 可以用八进制表示法（如 022）或符号表示法（如 u=rwx,g=rx,o=rx）指定。除非在 shell 配置文件（如 ~/.bashrc）中设置，否则更改仅对当前 shell 会话生效。

# COMMON VALUES

- **022** - 标准（文件 644，目录 755）
- **077** - 私有（文件 600，目录 700）
- **002** - 组可写

# CAVEATS

shell 内建命令。跨会话不持久。逻辑是反向的。

# HISTORY

**umask** 是标准的 Unix 命令，用于设置文件模式创建掩码，自早期 Unix 起就存在。

# INSTALL

```apk: sudo apk add execline```

```brew: brew install execline```

```nix: nix profile install nixpkgs#execline```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chmod](/man/chmod)(1), [chown](/man/chown)(1), [stat](/man/stat)(1)
