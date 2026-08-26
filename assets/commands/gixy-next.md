# TAGLINE

gixy 的持续维护分支，用于 nginx 安全分析

# TLDR

**分析 nginx 配置**

```gixy-next [/etc/nginx/nginx.conf]```

只运行特定检查

```gixy-next --tests [ssrf,host_spoofing] [config.conf]```

跳过特定检查

```gixy-next --skips [http_splitting] [config.conf]```

以 JSON 格式输出

```gixy-next -f json [config.conf]```

只显示中等严重程度及以上的问题

```gixy-next -ll [config.conf]```

# SYNOPSIS

**gixy-next** [_options_] _config_

# PARAMETERS

_CONFIG_
> Nginx 配置文件。

**--tests** _RULES_
> 只运行特定检查（逗号分隔）。

**--skips** _RULES_
> 跳过特定检查（逗号分隔）。

**-f**, **--format** _FORMAT_
> 输出格式（text、json）。

**-l**
> 按严重程度过滤。-l 表示 LOW 及以上，-ll 表示 MEDIUM 及以上，-lll 表示仅 HIGH。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gixy-next** 是 gixy 的持续维护分支，用于 nginx 安全分析。它在原工具的基础上继续开发，提供更新、错误修复以及对较新 nginx 特性的支持。

该工具分析 nginx 配置中的安全问题，检测可能导致 SSRF、主机欺骗等漏洞的错误配置。

# CAVEATS

原版 gixy 的分支，增加了额外检查和性能特性。未指定路径时默认分析 /etc/nginx/nginx.conf。也可以从 stdin 读取配置。

# HISTORY

在原 **gixy** 项目活跃度下降后，gixy-next 接续其开发。

# INSTALL

```brew: brew install gixy```

```nix: nix profile install nixpkgs#gixy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gixy](/man/gixy)(1), [nginx](/man/nginx)(1)
