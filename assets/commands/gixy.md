# TAGLINE

Nginx 配置安全分析器

# TLDR

**分析 nginx 配置**

```gixy [/etc/nginx/nginx.conf]```

只运行特定测试

```gixy --tests [http_splitting,ssrf] [/etc/nginx/nginx.conf]```

以 JSON 格式输出

```gixy -f json [/etc/nginx/nginx.conf]```

跳过特定测试

```gixy --skips [host_spoofing,low_keepalive_requests] [/etc/nginx/nginx.conf]```

只报告高严重程度的问题

```gixy -lll [/etc/nginx/nginx.conf]```

# SYNOPSIS

**gixy** [_options_] _config_

# PARAMETERS

_CONFIG_
> Nginx 配置文件。

**--tests** _TESTS_
> 要运行的测试的逗号分隔列表。

**--skips** _TESTS_
> 要跳过的测试的逗号分隔列表。

**-l, --level**
> 报告给定严重程度及以上的问题。-l 表示 LOW，-ll 表示 MEDIUM，-lll 表示 HIGH。

**-f** _FORMAT_, **--format** _FORMAT_
> 输出格式：text、json、console。

**-o** _FILE_, **--output** _FILE_
> 将报告写入文件。

**-c** _FILE_, **--config** _FILE_
> 配置文件的路径。

**-d, --debug**
> 启用调试模式。

**--disable-includes**
> 禁用对 include 指令的处理。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gixy** 分析 nginx 配置文件中的安全问题。它检测可能导致 SSRF、主机欺骗和路径穿越等漏洞的常见错误配置。

该工具内置多种安全检查插件，并为发现的问题提供详细说明。它被用于安全审计和 CI 流水线中，以便在部署前发现 nginx 配置错误。

# CAVEATS

Python 工具。原始 yandex/gixy 项目已无人维护；gixy-next 是持续维护的分支。可能需要更新才能支持最新的 nginx 特性。可能出现误报。部分插件提供额外选项，可通过 CLI 标志或配置文件设置。

# HISTORY

gixy 由 **Yandex** 创建，用于自动化 nginx 安全配置审查。

# INSTALL

```brew: brew install gixy```

```nix: nix profile install nixpkgs#gixy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nginx](/man/nginx)(1)
