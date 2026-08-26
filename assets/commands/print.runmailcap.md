# TAGLINE

使用 MIME 类型处理程序打印文件

# TLDR

使用默认的 run-mailcap 工具**打印**任意文件

```print filename```

直接通过 **run-mailcap** 打印

```run-mailcap --action=print filename```

# SYNOPSIS

**print** _file_

# DESCRIPTION

**print** 是 **run-mailcap** 的别名，默认执行 `print` 动作。它根据文件的 MIME 类型进行处理，并将其发送给 mailcap 配置（通常是 `/etc/mailcap` 和 `~/.mailcap`）中定义的相应打印处理程序。

相关的别名 **see**、**edit** 和 **compose** 分别默认执行 view、edit 和 compose 动作。它们都接受与 run-mailcap 相同的选项，包括 `--action`、`--debug`、`--nopager` 和 `--norun`。

# CAVEATS

需要为文件的 MIME 类型正确配置 mailcap。打印行为取决于系统打印配置。

# HISTORY

属于 **mime-support** 软件包的一部分，为类 Unix 系统提供 MIME 类型处理工具。

# SEE ALSO

[run-mailcap](/man/run-mailcap)(1), [lpr](/man/lpr)(1)
