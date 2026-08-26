# TAGLINE

在软件包中搜索文件。

# TLDR

**更新**元数据数据库

```sudo apt update```

**搜索**包含某个文件或路径的软件包

```apt-file search [path/to/file]```

**列出**特定软件包的内容

```apt-file show [package]```

搜索匹配**正则表达式**的软件包

```apt-file search -x [regex]```

# SYNOPSIS

**apt-file** [_options_] _command_ [_pattern_]

# DESCRIPTION

**apt-file** 在 apt 软件包中搜索文件，包括尚未安装的软件包。这对于查找哪个软件包提供了特定的文件或命令很有用。

# PARAMETERS

**search, find pattern**
> 搜索包含与 pattern 匹配文件的软件包

**show, list package**
> 列出特定软件包的内容

**update**
> 更新软件包内容缓存（通常通过 apt update 完成）

**-x, --regexp**
> 将 pattern 视为正则表达式

**-l, --package-only**
> 只显示软件包名称，不显示文件路径

**-F, --fixed-string**
> 不将 pattern 视为正则表达式（更快）

**-i, --ignore-case**
> 不区分大小写地搜索

**-a, --architecture arch**
> 搜索特定架构

**-D, --dummy**
> 空运行，不执行实际操作（用于测试）

**-N, --non-interactive**
> 不提示输入；适合脚本使用

# CONFIGURATION

**/etc/apt/apt-file.conf**
> 控制缓存位置和默认选项的配置文件。

# CAVEATS

需要安装 apt-file 软件包。搜索前必须先更新数据库。

# HISTORY

属于面向基于 Debian 系统的 **APT**（Advanced Package Tool）生态系统的一部分。

# INSTALL

```aur: yay -S apt-file```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt](/man/apt)(8), [apt-cache](/man/apt-cache)(8), [dpkg](/man/dpkg)(1)
