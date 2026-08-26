# TAGLINE

快速的域名可注册性调研工具

# TLDR

**跨 TLD 检查域名可用性**

```tldx [myapp] --tlds com,io,dev```

**配合前缀/后缀只显示可注册的域名**

```tldx [cloud] --prefixes get,my --suffixes hub,ly --available```

**JSON 输出并带最大长度过滤**

```tldx [startup] --format json --max-length 15```

# SYNOPSIS

**tldx** _keywords_ [_flags_] [_options_]

# PARAMETERS

**--tlds** _LIST_
> 要检查的 TLD 列表，逗号分隔。

**--prefixes** _LIST_
> 要前置的前缀列表，逗号分隔。

**--suffixes** _LIST_
> 要追加的后缀列表，逗号分隔。

**--available**
> 只显示可注册的域名。

**--format** _FORMAT_
> 输出格式：text、json、csv 或 grouped。

**--max-length** _N_
> 域名最大长度。

# DESCRIPTION

**tldx** 从关键字、前缀和后缀生成域名组合，然后使用并发 goroutine 通过 WHOIS 查询检查其可注册性。它支持多种输出格式和 TLD 预设，便于快速检索。

# HISTORY

**tldx** 由 **Brandon Young**（brandonyoungdev）创建，使用 **Go** 编写。

# INSTALL

```brew: brew install tldx```

```nix: nix profile install nixpkgs#tldx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[whois](/man/whois)(1), [dog](/man/dog)(1), [dig](/man/dig)(1)
