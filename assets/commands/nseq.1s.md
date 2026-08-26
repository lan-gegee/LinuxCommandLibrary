# TAGLINE

生成数字序列

# TLDR

**生成序列号**

```nseq [10]```

**指定起始值的序列**

```nseq [5] [10]```

**指定步长的序列**

```nseq [0] [2] [10]```

# SYNOPSIS

**nseq** [_first_] [_increment_] _last_

# PARAMETERS

_FIRST_
> 起始数字。

_INCREMENT_
> 步长值。

_LAST_
> 结束数字。

**--help**
> 显示帮助信息。

# DESCRIPTION

**nseq** 生成数字序列，是 OpenSSL 工具的一个变体。

该工具输出数字序列，属于 OpenSSL 工具集的一部分。

# CAVEATS

OpenSSL 实用工具。与 seq 类似，但不如标准 seq 常用。

# HISTORY

nseq 属于 **OpenSSL** 工具集，提供序列生成功能。

# SEE ALSO

[seq](/man/seq)(1), [openssl](/man/openssl)(1)
