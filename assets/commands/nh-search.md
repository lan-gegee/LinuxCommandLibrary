# TAGLINE

交互式搜索 Nix 软件包

# TLDR

**搜索软件包**

```nh search [query]```

**以 JSON 格式输出搜索结果**

```nh search --json [query]```

# SYNOPSIS

**nh search** [_options_] _query_

# PARAMETERS

_query_
> 搜索关键词。

**--json**
> 以 JSON 格式输出。

**--channel** _channel_
> Nixpkgs channel（频道）。

# DESCRIPTION

**nh search** 交互式搜索 Nix 软件包。提供快速的模糊搜索并附带预览。属于 nh（nix helper）工具集。

# INSTALL

```nix: nix profile install nixpkgs#nh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nh](/man/nh)(1), [nix-search](/man/nix-search)(1)
