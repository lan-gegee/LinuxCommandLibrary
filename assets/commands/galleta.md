# TAGLINE

Internet Explorer cookie 取证解析器

# TLDR

**解析 IE cookie**

```galleta [index.dat]```

**输出到文件**

```galleta [index.dat] > [cookies.txt]```

**以分隔符格式解析**

```galleta -d [index.dat]```

# SYNOPSIS

**galleta** [_options_] _file_

# PARAMETERS

_FILE_
> Internet Explorer cookie 文件（index.dat）。

**-d**
> 输出带分隔符的格式，便于电子表格使用。

**--help**
> 显示帮助信息。

# DESCRIPTION

**galleta** 是一款数字取证工具，用于解析 Internet Explorer 的 cookie 文件。它从 index.dat 文件中提取 cookie 数据，包括域名、路径、值和时间戳。

该工具可生成人类可读或带分隔符的输出供分析使用。它被用于取证调查，检查网页浏览历史和用户活动。

galleta 处理旧版 Internet Explorer 所使用的二进制 index.dat 格式。

# CAVEATS

仅适用于 IE 的 index.dat 格式。现代浏览器使用不同的格式。文件必须可访问（未被锁定）。

# HISTORY

galleta（西班牙语"饼干"，即 cookie）是分析 Internet Explorer 残留数据的取证工具集的一员。它解析 IE 用于存储 cookie 的专有 index.dat 格式。

# INSTALL

```apt: sudo apt install galleta```

```nix: nix profile install nixpkgs#galleta```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[strings](/man/strings)(1)
