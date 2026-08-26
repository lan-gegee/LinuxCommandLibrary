# TAGLINE

MATE 桌面环境的图形化文件搜索工具

# TLDR

按文件名包含**指定字符串**搜索文件

```mate-search-tool --named=[string] --path=[path/to/directory]```

**无需等待**用户确认即开始搜索文件

```mate-search-tool --start --named=[string] --path=[path/to/directory]```

按文件名匹配**指定正则表达式**搜索文件

```mate-search-tool --start --regex=[string] --path=[path/to/directory]```

为搜索结果设置**排序方式**

```mate-search-tool --start --named=[string] --path=[path/to/directory] --sortby=[name|folder|size|type|date]```

设置**降序排序**

```mate-search-tool --start --named=[string] --path=[path/to/directory] --descending```

搜索属于**指定用户/组**的文件

```mate-search-tool --start --user=[value] --path=[path/to/directory]```

# SYNOPSIS

**mate-search-tool** [_options_]

# PARAMETERS

**--named _string_**
> 搜索名称中包含该字符串的文件

**--regex _pattern_**
> 搜索匹配该正则表达式的文件

**--path _directory_**
> 要在其中搜索的目录

**--start**
> 无需确认立即开始搜索

**--sortby _field_**
> 结果排序依据：name、folder、size、type 或 date

**--descending**
> 按降序排序

**--user _name_**
> 搜索属于指定用户的文件

**--group _name_**
> 搜索属于指定组的文件

# DESCRIPTION

**mate-search-tool** 是 MATE 桌面环境的图形化文件搜索工具。它提供易用的界面，可按名称模式、内容、所有者、修改时间及其他条件查找文件。

该工具可以递归搜索目录，同时支持简单的通配符匹配和完整的正则表达式。结果显示为可排序列表，并附带文件详情。

命令行选项允许预先配置搜索参数，适合创建桌面快捷方式或启动特定搜索的脚本。

# CAVEATS

搜索大型目录树可能较慢。该工具不建立索引；每次搜索都会实时扫描文件系统。若要在大型系统上更快地搜索，建议使用数据库已更新的 **locate**。

# INSTALL

```apt: sudo apt install mate-utils```

```dnf: sudo dnf install mate-utils```

```pacman: sudo pacman -S mate-utils```

```apk: sudo apk add mate-utils```

```zypper: sudo zypper install mate-search-tool```

```nix: nix profile install nixpkgs#mate-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[find](/man/find)(1), [locate](/man/locate)(1)
