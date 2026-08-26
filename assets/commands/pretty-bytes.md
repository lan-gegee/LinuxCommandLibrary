# TAGLINE

将字节数值转换为人类可读的字符串

# TLDR

**将字节转换为人类可读格式**

```pretty-bytes [1024]```

**从 stdin 转换**

```echo [1048576] | pretty-bytes```

**转换大数值**

```pretty-bytes [1099511627776]```

# SYNOPSIS

**pretty-bytes** _bytes_

# PARAMETERS

_BYTES_
> 要转换的字节值。

# DESCRIPTION

**pretty-bytes** 将原始字节值转换为带有合适单位后缀（kB、MB、GB、TB 等）的人类可读字符串。它会自动选择最易读的单位，使大数字一目了然。

这个 Node.js CLI 工具适用于脚本和管道中需要以用户友好格式（而非原始数字）显示文件大小或数据量的场景。

# CAVEATS

使用二进制前缀。Node.js 软件包。

# HISTORY

pretty-bytes 是为字节格式化而创建的 **Node.js 工具**。

# INSTALL

```dnf: sudo dnf install pretty-bytes```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[numfmt](/man/numfmt)(1)
