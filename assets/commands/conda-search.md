# TAGLINE

软件包仓库搜索器

# TLDR

**搜索软件包**

```conda search [package_name]```

**使用版本模式搜索**

```conda search "[package_name]>=[version]"```

**在特定频道中搜索**

```conda search -c [conda-forge] [package_name]```

**显示详细信息**

```conda search --info [package_name]```

**搜索特定平台**

```conda search --platform [linux-64] [package_name]```

# SYNOPSIS

**conda** **search** [_options_] [_query_]

# PARAMETERS

**-c**, **--channel** _channel_
> 在特定频道中搜索。

**--info**
> 显示详细的软件包信息。

**--platform** _subdir_
> 搜索指定的平台（如 osx-64、linux-64、win-64）。默认为当前平台。

**-O**, **--override-channels**
> 不搜索默认频道或 .condarc 中的频道；只搜索指定的频道。

**--json**
> 以 JSON 格式输出。

**-v**, **--verbose**
> 使用一次显示 info，两次为 debug，三次为 trace。

# CONFIGURATION

**~/.condarc**
> 用户级 conda 配置，涵盖频道、软件包设置和求解器选项。

**/opt/conda/.condarc**
> 系统级 conda 配置。

# DESCRIPTION

**conda search** 在已配置的频道中搜索与查询匹配的软件包。它会显示可用版本及构建变体。

软件包规格可以包含 **>=**、**<=**、**==** 等版本约束。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-install](/man/conda-install)(1), [conda-repoquery](/man/conda-repoquery)(1)
