# TAGLINE

解析并显示 UUID 信息

# TLDR

**解析** UUID

```uuidparse [uuid1] [uuid2]```

从**标准输入**解析

```[command] | uuidparse```

**JSON** 输出

```uuidparse -J [uuid1] [uuid2]```

**不打印表头**行

```uuidparse -n [uuid1] [uuid2]```

**原始格式**输出

```uuidparse -r [uuid1] [uuid2]```

选择输出**列**

```uuidparse -o [UUID,VARIANT,TYPE,TIME]```

# SYNOPSIS

**uuidparse** [_OPTIONS_] [_UUID_...]

# PARAMETERS

**-J, --json**
> JSON 输出格式

**-n, --noheadings**
> 不打印表头行

**-r, --raw**
> 原始输出格式

**-o, --output** _COLUMNS_
> 选择输出列（支持：UUID、VARIANT、TYPE、TIME）。

**-V, --version**
> 显示版本信息并退出。

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**uuidparse** 解析并显示 UUID 的相关信息。它会显示变体（如 DCE）、类型（如随机、基于时间），以及基于时间的 UUID 中嵌入的时间戳。

该工具可以从命令行参数或标准输入解析 UUID。

# CAVEATS

只能解析标准 UUID 格式。时间提取仅对基于时间（v1）的 UUID 有效。属于 util-linux 软件包。

# INSTALL

```apt: sudo apt install uuid-runtime```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uuidgen](/man/uuidgen)(1), [uuid](/man/uuid)(1), [uuidd](/man/uuidd)(8)
