# TAGLINE

生成新的 UUID 值

# TLDR

**生成**随机 UUID（v4）

```uuidgen -r```

**生成**基于时间的 UUID（v1）

```uuidgen -t```

**生成**按时间排序的 UUID（v7）

```uuidgen -7```

从命名空间和名称**生成**基于 SHA1 的 UUID（v5）

```uuidgen -s -n @dns -N [example.com]```

从命名空间和名称**生成**基于 MD5 的 UUID（v3）

```uuidgen -m -n @url -N [https://example.com]```

**一次性生成**多个基于时间的 UUID

```uuidgen -t -C [5]```

# SYNOPSIS

**uuidgen** [_options_]

# PARAMETERS

**-r, --random**
> 生成随机 UUID（版本 4）

**-t, --time**
> 生成基于时间的 UUID（版本 1）

**-7, --time-v7**
> 生成基于时间的 UUID（版本 7），可按时间戳进行字典序排序

**-s, --sha1**
> 生成基于 SHA1 的 UUID（版本 5）

**-m, --md5**
> 生成基于 MD5 的 UUID（版本 3）

**-n, --namespace _ns_**
> 基于名称的 UUID 所使用的命名空间（@dns、@url、@oid、@x500）

**-N, --name _name_**
> 基于名称的 UUID 所使用的名称

**-x, --hex**
> 将名称解释为十六进制字符串

**-C, --count _num_**
> 生成多个 UUID

**-h, --help**
> 显示帮助文本并退出

**-V, --version**
> 输出版本信息并退出

# DESCRIPTION

**uuidgen** 用于创建新的通用唯一标识符（UUID）。默认生成随机 UUID（版本 4）。基于时间（v1）的 UUID 包含时间戳和 MAC 地址。基于名称的 UUID（v3/v5）是确定性的，对于相同的命名空间和名称组合总是生成相同的 UUID。

UUID 是 128 位标识符，常用于数据库、分布式系统和文件系统中进行唯一标识。

# UUID VERSIONS

**v1**：基于时间和 MAC 地址
**v3**：命名空间和名称的 MD5 哈希
**v4**：随机
**v5**：命名空间和名称的 SHA1 哈希
**v7**：基于时间，可字典序排序（RFC 9562）

# CAVEATS

基于时间的 UUID 会暴露生成机器的 MAC 地址。出于隐私考虑，建议优先使用随机 UUID。属于 util-linux 软件包。

# INSTALL

```apt: sudo apt install uuid-runtime```

```apk: sudo apk add uuidgen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uuid](/man/uuid)(1)
