# TAGLINE

为终端转换下划线序列

# TLDR

**显示**带下划线的文件

```ul [file.txt]```

用**短横线**作为下划线显示

```ul -i [file.txt]```

# SYNOPSIS

**ul** [_OPTIONS_] [_FILE_...]

# PARAMETERS

**-i, --indicated**
> 使用短横线（-）作为下划线

**-t, --terminal** _TYPE_
> 覆盖终端类型

# DESCRIPTION

**ul** 将文本文件中的下划线序列转换为相应的终端转义序列。它处理包含重叠打印（基于退格符的下划线）的文件，并将其转换为能在现代终端上正常显示的形式。

该工具读取使用传统下划线方式的文件，其中每个加下划线的字符后面跟着退格符和下划线符号。

# CAVEATS

输入必须包含传统的重叠打印下划线序列。输出取决于终端能力。现代文本很少使用这种格式。

# HISTORY

**ul** 是 **util-linux** 的一部分，其历史可追溯到早期 Unix 时代，当时终端使用重叠打印序列来实现格式化效果。

# INSTALL

```apt: sudo apt install bsdextrautils```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[col](/man/col)(1), [colcrt](/man/colcrt)(1)
