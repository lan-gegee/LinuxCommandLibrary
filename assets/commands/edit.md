# TAGLINE

感知 MIME 类型的文件编辑器启动器

# TLDR

**编辑文件**，根据其 MIME 类型选择合适的编辑器

```edit [filename]```

**以显式 MIME 类型编辑**

```edit [text/html]:[filename]```

**只显示编辑器命令而不执行**

```edit --norun [filename]```

**直接使用 run-mailcap 的 edit 动作**

```run-mailcap --action=edit [filename]```

# SYNOPSIS

**edit** _filename_

# DESCRIPTION

**edit** 是 run-mailcap 的 edit 动作的别名。它根据 mailcap 文件中的 MIME 类型配置，用合适的编辑器打开文件。

实际使用的编辑器取决于文件类型和系统的 mailcap 配置。

# PARAMETERS

_filename_
> 要编辑的文件。可以在前面加上 MIME 类型和可选的编码，格式为 `MIME-TYPE:[ENCODING:]FILE`。

**--debug**
> 打印关于当前操作的额外诊断信息。

**--nopager**
> 忽略任何 `copiousoutput` 指令，将输出直接发送到 stdout。

**--norun**
> 显示将要运行的命令但不执行它。

# CONFIGURATION

**/etc/mailcap**
> 系统级的 MIME 类型到应用程序的映射。

**~/.mailcap**
> 用户级的 MIME 类型覆盖配置。

# CAVEATS

Debian/Ubuntu 特有。所使用的编辑器取决于 mailcap 配置和 MIME 类型检测。

# INSTALL

```nix: nix profile install nixpkgs#edit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[run-mailcap](/man/run-mailcap)(1), [sensible-editor](/man/sensible-editor)(1), [view](/man/view)(1), [compose](/man/compose)(1), [file](/man/file)(1)
