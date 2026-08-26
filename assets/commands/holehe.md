# TAGLINE

检查某个邮箱是否在各类网站上注册过

# TLDR

**检查邮箱注册情况**

```holehe [email@example.com]```

**以 CSV 输出**

```holehe [email@example.com] --csv```

**只输出命中的结果**

```holehe --only-used [email@example.com]```

**禁用彩色输出**

```holehe --no-color [email@example.com]```

**设置请求超时**

```holehe --timeout [10] [email@example.com]```

# SYNOPSIS

**holehe** [_options_] _email_

# PARAMETERS

_EMAIL_
> 要检查的邮箱地址。

**--csv**
> 以 CSV 格式输出。

**--only-used**
> 只显示命中的结果。

**--no-color**
> 禁用彩色输出。

**-t**, **--timeout** _SEC_
> 请求超时时间。

**--help**
> 显示帮助信息。

# DESCRIPTION

**holehe** 检查某个邮箱是否在各类网站上注册过。它利用密码重置和注册功能来检测账号是否存在。

该工具适用于 OSINT（开源情报）和安全测试。它会检查数百个网站的邮箱注册状态。

# CAVEATS

这是需要授权使用的 OSINT 工具。可能受到速率限制。结果可能存在误报。

# HISTORY

holehe 是作为一个跨众多平台检查邮箱注册情况的 OSINT 工具而创建的。

# INSTALL

```nix: nix profile install nixpkgs#holehe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sherlock](/man/sherlock)(1), [theHarvester](/man/theHarvester)(1)
