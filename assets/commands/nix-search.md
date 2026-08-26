# TAGLINE

在 Nix flakes 中搜索软件包

# TLDR

**在 Nixpkgs 中搜索软件包**

```nix search nixpkgs [query]```

**以 JSON 格式输出搜索结果**

```nix search nixpkgs [query] --json```

**搜索指定的 flake**

```nix search [github:owner/repo] [query]```

**搜索并排除匹配的软件包**

```nix search nixpkgs [query] --exclude [regex]```

**使用多个关键词搜索（AND 逻辑）**

```nix search nixpkgs [python] [http]```

# SYNOPSIS

**nix search** _flake_ [_query..._] [_options_]

# PARAMETERS

_flake_
> 要搜索的 flake 引用（例如 nixpkgs、github:owner/repo）。

_query_
> 搜索词，按正则表达式处理。多个搜索词之间是 AND 关系。

**--json**
> 以 JSON 格式输出结果。

**-e**, **--exclude** _regex_
> 排除属性路径、名称或描述匹配该正则表达式的软件包。

**--impure**
> 允许访问可变路径和外部仓库。

**-I**, **--include** _path_
> 向 Nix 搜索路径中添加路径，用于解析查找路径。

**--offline**
> 在无网络连接的情况下运行。

**--refresh**
> 搜索前强制刷新 flake 注册表及其输入。

# DESCRIPTION

**nix search** 通过匹配软件包名称、属性路径和描述来搜索 Nix flakes 中的软件包。多个搜索词之间为 AND 关系。它属于实验性的新版 Nix CLI（需要启用 `nix-command` 和 `flakes` 实验特性）。

# CAVEATS

需要启用 **nix-command** 和 **flakes** 实验特性。首次搜索某个 flake 时可能较慢，因为要先求值并缓存整个软件包集。搜索结果取决于 flake 锁文件的版本。

# INSTALL

```nix: nix profile install nixpkgs#nix-search```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1), [nix-env](/man/nix-env)(1), [nix-profile](/man/nix-profile)(1), [nix-shell](/man/nix-shell)(1)
