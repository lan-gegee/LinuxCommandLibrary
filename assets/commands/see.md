# TAGLINE

使用 mailcap MIME 处理程序查看文件

# TLDR

使用文件的 MIME 类型处理程序**查看**文件

```see [filename]```

以显式 MIME 类型**查看**文件

```see [mime/type]:[filename]```

**显示**将要使用的命令但不执行

```see --norun [filename]```

# SYNOPSIS

**see** [**--norun**] [**--nopager**] [**--debug**] [_mime-type_**:**[_encoding_**:**]_filename_]

# PARAMETERS

**--debug**
> 开启额外信息以了解发生了什么

**--nopager**
> 忽略任何 "copiousoutput" 指令，将输出发送到 STDOUT

**--norun**
> 显示找到的命令而不实际执行

# DESCRIPTION

**see** 是 **run-mailcap --action=view** 的别名。它根据 mailcap 数据库（~/.mailcap 和 /etc/mailcap）中的配置，按 MIME 类型使用合适的查看器打开文件。

每个文件可以将其 mime-type、编码（例如压缩方式）和文件名一起指定，以冒号分隔。若未指定 mime-type，则使用 mime.types 数据库根据文件扩展名确定。

# CAVEATS

行为取决于 mailcap 配置。某些 MIME 类型可能没有配置查看器。属于 **mailcap**（或 **mime-support**）软件包。

# INSTALL

```nix: nix profile install nixpkgs#see```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[run-mailcap](/man/run-mailcap)(1), [edit](/man/edit)(1), [compose](/man/compose)(1), [print](/man/print)(1), [xdg-open](/man/xdg-open)(1)
