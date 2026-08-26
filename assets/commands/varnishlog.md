# TAGLINE

显示 Varnish HTTP 请求日志

# TLDR

**实时显示日志**

```varnishlog```

**只显示特定标签**

```varnishlog -i [ReqURL]```

**按查询过滤**

```varnishlog -q "[RespStatus == 500]"```

**仅客户端请求**

```varnishlog -c```

**仅后端请求**

```varnishlog -b```

**按请求分组**

```varnishlog -g request```

# SYNOPSIS

**varnishlog** [_-c_] [_-b_] [_-q query_] [_-i tag_] [_options_]

# PARAMETERS

**-c**
> 只显示客户端侧事务。

**-b**
> 只显示后端侧事务。

**-q** _QUERY_
> 用于过滤事务的 VSL 查询表达式。

**-i** _TAGLIST_
> 只包含具有指定标签的记录（逗号分隔）。

**-I** _TAGREGEX_
> 只包含匹配指定标签和正则表达式的记录。

**-x** _TAGLIST_
> 排除具有指定标签的记录。

**-X** _TAGREGEX_
> 排除匹配指定标签和正则表达式的记录。

**-g** _MODE_
> 分组模式（raw、vxid、request、session）。

**-d**
> 先处理旧的日志条目。

**-w** _FILENAME_
> 将输出写入文件。

# DESCRIPTION

**varnishlog** 读取 Varnish 共享内存日志（VSL），实时显示详细的请求和响应信息。它展示 HTTP 事务的完整生命周期，包括客户端请求、后端抓取、缓存决策和响应头。

该工具通过 VSL 查询语言提供强大的过滤功能，可以按状态码、URL 模式或任何已记录的字段隔离特定事务。客户端侧（-c）和后端侧（-b）视图可以独立显示，分组模式则可按请求、会话或原始日志条目组织输出。这使它成为理解 Varnish 缓存行为的主要调试工具。

# CAVEATS

需要正在运行的 Varnish 实例。熟悉 VSL 查询语言有助于进行有效过滤。不加过滤时输出可能非常冗长。

# HISTORY

**varnishlog** 是 **Varnish Cache** 的一部分，用于显示 Varnish 共享内存日志以辅助调试。

# INSTALL

```apt: sudo apt install varnish```

```dnf: sudo dnf install varnish```

```apk: sudo apk add varnish```

```brew: brew install varnish```

```nix: nix profile install nixpkgs#varnish```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[varnishhist](/man/varnishhist)(1), [varnishstat](/man/varnishstat)(1), [varnishd](/man/varnishd)(1)
