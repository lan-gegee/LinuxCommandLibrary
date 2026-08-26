# TAGLINE

计算软件包归档的哈希摘要

# TLDR

**计算软件包哈希**

```pip hash [package.whl]```

**计算 SHA256 哈希**

```pip hash -a sha256 [package.tar.gz]```

**计算多个哈希**

```pip hash -a sha256 -a sha384 [package.whl]```

# SYNOPSIS

**pip** **hash** [_options_] _files_...

# PARAMETERS

**-a**, **--algorithm** _algo_
> 哈希算法（sha256、sha384、sha512）。

# DESCRIPTION

**pip hash** 计算软件包归档的哈希摘要。输出的哈希采用适用于启用哈希校验模式的 requirements 文件的格式。支持 SHA256、SHA384 和 SHA512 算法。

# INSTALL

```apk: sudo apk add py3-pip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [pip-download](/man/pip-download)(1)
