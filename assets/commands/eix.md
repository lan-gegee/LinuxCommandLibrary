# TAGLINE

Gentoo 快速软件包搜索工具

# TLDR

按**名称**搜索 Portage 软件包缓存

```eix [query]```

将结果限定为**已安装**的软件包

```eix --installed [query]```

匹配软件包**描述**文本

```eix --description "[text]"```

按**许可证**名称过滤

```eix --license [license]```

反转过滤条件（例如查找**不**在某许可证之下的软件包）

```eix --not --license [license]```

# SYNOPSIS

**eix** [_options_] [_query_]

# DESCRIPTION

**eix** 使用预构建的缓存快速搜索本地 Gentoo 软件包。它提供快速的软件包查询，并附带详细的版本和 USE 标志信息。

搜索前先运行 `eix-update` 更新本地软件包缓存。

# PARAMETERS

**--installed**
> 只显示已安装的软件包

**--description** _text_
> 在软件包描述中搜索

**--license** _license_
> 按许可证搜索

**--not**
> 取反其后的条件

**-c, --compact**
> 紧凑输出格式

**-e, --exact**
> 精确名称匹配

# CAVEATS

Gentoo Linux 特有。需要运行 eix-update 构建缓存。执行 emerge --sync 后必须更新缓存。

# SEE ALSO

[emerge](/man/emerge)(1), [equery](/man/equery)(1)
