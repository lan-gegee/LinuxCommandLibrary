# TAGLINE

管理 kiterunner 知识库

# TLDR

**列出知识库**

```kr kb list```

**下载知识库**

```kr kb download [kbname]```

**使用指定知识库**

```kr scan [url] -A [kbname]```

**查看知识库信息**

```kr kb info [kbname]```

# SYNOPSIS

**kr kb** _command_ [_options_]

# PARAMETERS

**list**
> 列出可用的知识库。

**download** _NAME_
> 下载知识库。

**info** _NAME_
> 显示知识库详情。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kr kb** 管理 kiterunner 知识库。知识库中包含用于扫描的 API 路由模式。

该工具从 Assetnote 下载预构建的字典。不同的 KB 面向不同类型的 API。

# CAVEATS

kiterunner 的子命令。下载需要联网。知识库占用磁盘空间。

# HISTORY

kr kb 是 Assetnote 出品的 **kiterunner** 的一部分，为安全测试提供精选的 API 端点字典。

# INSTALL

```nix: nix profile install nixpkgs#kiterunner```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kiterunner](/man/kiterunner)(1), [kiterunner-scan](/man/kiterunner-scan)(1)
