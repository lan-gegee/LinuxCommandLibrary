# TAGLINE

将主机名解析为 IP 地址

# TLDR

将主机名**解析**为 IP 地址

```resolveip [example.org]```

将 IP 地址**解析**为主机名

```resolveip [1.1.1.1]```

以**较少输出**进行解析

```resolveip -s [example.org]```

# SYNOPSIS

**resolveip** [_options_] _hostname_or_ip_...

# PARAMETERS

**-s**, **--silent**
> 安静模式；只打印 IP 地址或主机名

**-h**, **--help**
> 显示帮助信息

**-v**, **--version**
> 显示版本信息

# DESCRIPTION

**resolveip** 将主机名解析为 IP 地址，并对 IP 地址执行反向查询以获得主机名。它是 MariaDB/MySQL 附带的实用工具，用于基础 DNS 解析，常见于数据库配置脚本中。

该命令接受多个参数并依次解析。对于主机名，它返回所有关联的 IP 地址；对于 IP 地址，它返回反向 DNS 得到的主机名。

# CAVEATS

依赖系统 DNS 配置（/etc/resolv.conf）。由于本地 DNS 缓存或 hosts 文件条目，结果可能与网页浏览器的不同。如需更全面的 DNS 查询，请考虑使用 **dig** 或 **host** 命令。

# HISTORY

随 **MariaDB** 和 **MySQL** 一同提供，作为在数据库管理场景下解析主机名的简单工具。虽然与 dig 等工具相比功能有限，但其输出直接明了，适合脚本使用。

# INSTALL

```apt: sudo apt install mariadb-server-core```

```dnf: sudo dnf install mariadb```

```pacman: sudo pacman -S mariadb```

```apk: sudo apk add mariadb```

```zypper: sudo zypper install mariadb```

```brew: brew install mariadb```

```nix: nix profile install nixpkgs#mariadb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[host](/man/host)(1), [dig](/man/dig)(1), [nslookup](/man/nslookup)(1), [getent](/man/getent)(1)
