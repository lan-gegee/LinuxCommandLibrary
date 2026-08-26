# TAGLINE

系统 hosts 文件的命令行编辑器

# TLDR

**列出**所有 hosts 条目

```hosts```

**搜索**匹配字符串或正则表达式的条目

```hosts [localhost]```

**添加**条目

```hosts add [127.0.0.1] [example.com]```

**移除**条目

```hosts remove [example.com]```

**屏蔽**域名（IPv4 和 IPv6）

```hosts block [example.com]```

**取消屏蔽**域名

```hosts unblock [example.com]```

**禁用**（注释掉）条目

```hosts disable [example.com]```

**启用**已禁用的条目

```hosts enable [example.com]```

**创建备份**

```hosts backups create```

# SYNOPSIS

**hosts** [*command*] [*args*]

# DESCRIPTION

**hosts** 是一个可移植的 Shell 脚本，用于管理 **/etc/hosts**（或系统 hosts 文件）：列出和搜索条目、添加/删除映射、屏蔽/解除屏蔽域名、通过注释启用/禁用行，以及维护备份。它在现有 hosts 文件的基础上工作，而不是替换它们。

可通过 Homebrew（**xwmx/taps**）、npm（**hosts.sh**）、bpkg、**make install**、AUR 安装，或将脚本放入 **PATH**。许多操作需要 root 权限才能写入系统 hosts 文件。

# PARAMETERS

*(no args)* / **list**

> 列出 hosts 文件条目。

*pattern*

> 搜索匹配字符串或正则表达式的条目。

**add** *ip* *hostname*...

> 添加映射。

**remove** *ip|host|regex*

> 删除匹配的条目（会提示确认）。

**block** / **unblock** *domain*

> 为域名添加或移除屏蔽条目。

**disable** / **enable** *entry*

> 注释或取消注释条目。

**backups** create|show|compare|...

> hosts 文件的备份管理。

**completions install**

> 安装 Shell 补全（通常需要 sudo）。

# CAVEATS

编辑系统 hosts 文件通常需要 **sudo**。错误的条目可能破坏名称解析；请保留备份。在某些系统上 hosts 路径不同；该脚本针对平台默认路径。仅安装脚本时补全是可选的。

# INSTALL

```aur: yay -S hosts```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hostess](/man/hostess)(1), [getent](/man/getent)(1), [dig](/man/dig)(1)

# RESOURCES

```[Source code](https://github.com/xwmx/hosts)```

<!-- verified: 2026-07-19 -->
