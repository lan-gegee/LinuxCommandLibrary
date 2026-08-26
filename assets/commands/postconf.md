# TAGLINE

显示和修改 Postfix 配置

# TLDR

使用备用的**配置目录**

```postconf -c [path/to/config_dir]```

**编辑**配置参数

```postconf -e```

显示**默认**设置

```postconf -d```

显示**特定类别**的参数

```postconf -C [builtin|service|user|all]```

列出 **SASL** 插件类型

```postconf -a```

列出**查找表**类型

```postconf -m```

# SYNOPSIS

**postconf** [**-c** _dir_] [**-d**] [**-e**] [**-C** _class_] [_parameters_...]

# PARAMETERS

**-c _directory_**
> 备用配置目录

**-d**
> 显示默认参数值

**-e**
> 以 name=value 对的形式编辑 main.cf

**-C _class_**
> 按参数类别过滤

**-a**
> 列出可用的 SASL 插件类型

**-m**
> 列出可用的查找表类型

**-n**
> 仅显示非默认值的参数

# DESCRIPTION

**postconf** 用于显示和修改 Postfix 邮件服务器的配置。它可以读写 main.cf 参数、显示默认值，并报告配置警告。

该工具会校验参数名并对拼写错误发出警告。对于无需手动编辑配置文件的 Postfix 管理工作而言，它是必不可少的工具。

# CAVEATS

通过 -e 所做的更改需要 postfix reload 才能生效。某些参数需要重启。修改运行中服务器的配置须谨慎。重大变更前请备份配置。

# HISTORY

**postconf** 是 **Postfix** 的组成部分。Postfix 是由 **Wietse Venema** 创建的邮件传输代理，作为 Sendmail 的安全替代方案。它为复杂的邮件系统提供安全的配置管理。

# INSTALL

```apt: sudo apt install postfix```

```dnf: sudo dnf install postfix```

```pacman: sudo pacman -S postfix```

```apk: sudo apk add postfix```

```zypper: sudo zypper install postfix```

```nix: nix profile install nixpkgs#postfix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[postfix](/man/postfix)(1), [postqueue](/man/postqueue)(1), [postmap](/man/postmap)(1)
