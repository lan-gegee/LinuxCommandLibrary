# TLDR

# TAGLINE

生成全局唯一标识符

# TLDR

生成 **UUIDv1**

```uuid```

生成 **UUIDv4**

```uuid -v 4```

生成**多个** UUID

```uuid -v 4 -n [number_of_uuids]```

指定输出**格式**

```uuid -v 4 -F [BIN|STR|SIV]```

写入**文件**

```uuid -v 4 -o [path/to/file]```

带命名空间生成 **UUIDv5**

```uuid -v 5 ns:[DNS|URL|OID|X500] [object_name]```

**解析** UUID

```uuid -d [uuid]```

# SYNOPSIS

**uuid** [_OPTIONS_]

# PARAMETERS

**-v** _VERSION_
> UUID 版本（1、3、4 或 5）

**-n** _COUNT_
> 一次生成多个 UUID

**-F** _FORMAT_
> 输出格式（BIN、STR 或 SIV）

**-o** _FILE_
> 将输出写入文件

**ns:** _NAMESPACE_
> v3/v5 所用的命名空间前缀

**-d**
> 解析 UUID

# DESCRIPTION

**uuid** 用于生成和解析全局唯一标识符。它支持多个 UUID 版本：v1（基于时间）、v3（MD5 哈希）、v4（随机）和 v5（SHA-1 哈希）。

UUID 是一种 128 位标识符，常用于在分布式系统中唯一标识信息。

# CAVEATS

UUIDv1 可能暴露系统相关信息。UUIDv4 需要有良好的随机源。基于命名空间的 UUID 必须指定对象名称。

# INSTALL

```apt: sudo apt install uuid```

```dnf: sudo dnf install uuid```

```apk: sudo apk add ossp-uuid```

```zypper: sudo zypper install ossp-uuid```

```brew: brew install ossp-uuid```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uuidgen](/man/uuidgen)(1), [uuidparse](/man/uuidparse)(1)
