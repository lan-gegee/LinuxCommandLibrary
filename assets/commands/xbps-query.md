# TAGLINE

查询 Void Linux 软件包信息

# TLDR

**在远程仓库中搜索**软件包

```xbps-query -Rs [keyword]```

**显示**已安装软件包的信息

```xbps-query -S [package]```

**显示**远程仓库中软件包的信息

```xbps-query -RS [package]```

**列出所有已安装**的软件包

```xbps-query -l```

**列出显式安装**的软件包（非依赖项）

```xbps-query -m```

**列出软件包安装的文件**

```xbps-query -f [package]```

**显示已安装软件包的依赖**

```xbps-query -x [package]```

**显示软件包的反向依赖**

```xbps-query -X [package]```

**查找某个文件属于哪个软件包**

```xbps-query -o [/path/to/file]```

**列出孤立软件包**（不再使用的依赖）

```xbps-query -O```

# SYNOPSIS

**xbps-query** [_options_] [_package_]

# PARAMETERS

**-s** _pattern_
> 搜索匹配模式的软件包。

**-S** _package_
> 显示软件包的详细信息。

**-l**
> 列出所有已安装的软件包。

**-m**
> 列出显式安装的软件包（非依赖项）。

**-L**
> 列出已配置的软件仓库。

**-f** _package_
> 列出软件包安装的文件。

**-x** _package_
> 显示软件包的依赖。

**-X** _package_
> 显示反向依赖。

**-R**, **--repository**
> 查询远程仓库而不是本地。

**-o** _PATTERN_
> 搜索其文件匹配 PATTERN 的软件包。

**-O**
> 列出孤立软件包（作为依赖安装、现已不需要）。

**--regex**
> 为搜索启用扩展正则表达式匹配。

**-p** _property_
> 显示特定属性（如版本、描述）。

**-v**, **--verbose**
> 启用详细输出。

# DESCRIPTION

**xbps-query** 从 XBPS 包管理系统查询软件包信息。它可以搜索仓库、显示软件包详情、列出已安装的软件包以及查看依赖信息。

该工具是在 Void Linux 上探索可用软件包和了解当前系统状态的必备工具。

# CAVEATS

仓库查询需要网络访问和最新的仓库索引（运行 **xbps-install -S** 同步）。一次只能使用一种查询模式。属于 Void Linux 的 XBPS 包管理系统的一部分。

# INSTALL

```apk: sudo apk add xbps```

```nix: nix profile install nixpkgs#xbps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xbps-install](/man/xbps-install)(1), [xbps-remove](/man/xbps-remove)(1)
