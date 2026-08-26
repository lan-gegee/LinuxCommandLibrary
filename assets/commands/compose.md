# TAGLINE

使用 mailcap 配置的编辑器打开文件

# TLDR

**用默认的 mailcap 编辑器撰写**文件

```compose [filename]```

直接使用 **run-mailcap**

```run-mailcap --action=compose [filename]```

# SYNOPSIS

**compose** _filename_

# DESCRIPTION

**compose** 是 run-mailcap 的 compose 动作的便捷包装器，属于 mailcap 系统的一部分——该系统在 Unix 上提供基于 MIME 类型的文件处理能力。调用时，它会检查文件的 MIME 类型，并按照系统 mailcap 文件中的配置启动相应的编辑器或撰写工具。

mailcap 机制最初用于处理电子邮件附件，后来演变为通用的文件处理系统。它将 MIME 类型（如 text/plain、image/png 或 application/pdf）映射到可以查看、编辑、撰写或打印这些文件的具体命令。compose 动作特指创建或编辑文件，与 view（只读）或 print 动作相区分。

该工具在邮件用户代理（MUA）及其他需要根据内容类型启动外部编辑器的应用中特别有用，避免了硬编码特定应用程序。不同的 MIME 类型可自动交给不同的专用工具处理。

# PARAMETERS

_filename_
> 要撰写/编辑的文件

# CONFIGURATION

**~/.mailcap**
> 用户级的 MIME 类型与应用程序映射。

**/etc/mailcap**
> 系统级 MIME 类型映射。

# CAVEATS

依赖 mailcap 配置。实际使用的编辑器取决于文件的 MIME 类型和系统配置。为 Debian/Ubuntu 特有工具。

# INSTALL

```aur: yay -S compose```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[run-mailcap](/man/run-mailcap)(1), [edit](/man/edit)(1), [view](/man/view)(1)

# RESOURCES

```[Source code](https://salsa.debian.org/debian/mime-support)```

<!-- verified: 2026-06-22 -->
