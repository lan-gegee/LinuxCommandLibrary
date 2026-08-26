# TAGLINE

显示当前 locale 设置的信息或列出可用项

# TLDR

显示当前 **locale 设置**

```locale```

列出**所有可用** locale

```locale --all-locales```

列出带**元数据**的 locale

```locale --all-locales --verbose```

显示**日期格式**

```locale date_fmt```

# SYNOPSIS

**locale** [_options_] [_name_...]

# DESCRIPTION

**locale** 显示当前 locale 设置的信息或列出可用的 locale。它显示控制语言、字符编码、日期/时间格式和其他区域设置的各类环境变量。

# PARAMETERS

**-a, --all-locales**
> 列出所有可用的 locale

**-v, --verbose**
> 显示详细的 locale 信息

**-c, --category-name**
> 打印类别名称

**-k, --keyword-name**
> 打印关键字名称

**-m, --charmaps**
> 列出可用的字符映射表

# LOCALE CATEGORIES

**LC_CTYPE**
> 字符分类与大小写转换

**LC_COLLATE**
> 字符串排序规则

**LC_MESSAGES**
> 消息翻译

**LC_MONETARY**
> 货币格式

**LC_NUMERIC**
> 数字格式

**LC_TIME**
> 日期和时间格式

# INSTALL

```apt: sudo apt install libc-bin```

```apk: sudo apk add musl-locales```

```nix: nix profile install nixpkgs#locale```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[localectl](/man/localectl)(1), [locale-gen](/man/locale-gen)(8), [localedef](/man/localedef)(1)
