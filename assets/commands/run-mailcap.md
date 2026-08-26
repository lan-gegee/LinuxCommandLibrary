# TAGLINE

使用 mailcap MIME 类型条目打开文件

# TLDR

使用 mailcap 条目**查看**文件

```run-mailcap --action=view [path/to/file]```

使用 mailcap 条目**编辑**文件

```run-mailcap --action=edit [path/to/file]```

使用 mailcap 条目**打印**文件

```run-mailcap --action=print [path/to/file]```

使用 copiousoutput 规则将文件 **cat** 到 stdout

```run-mailcap --action=cat [path/to/file]```

带 **debug** 信息运行

```run-mailcap --action=view --debug [path/to/file]```

只**显示命令**而不执行

```run-mailcap --action=view --norun [path/to/file]```

# SYNOPSIS

**run-mailcap** [_--action=action_] [_--option[=value]_] [_MIME-TYPE:_[_ENCODING:_]]_FILE_ [...]

# PARAMETERS

**--action=**_action_
> 要执行的动作：view、cat、compose、composetyped、edit、print。cat 动作仅使用 copiousoutput 规则并将输出发送到 stdout。

**--debug**
> 显示诊断输出以便排查问题

**--nopager**
> 忽略 copiousoutput 指令，将输出直接发送到 stdout

**--norun**
> 显示将要执行的命令但不实际运行

# DESCRIPTION

**run-mailcap** 根据 MIME 类型通过 mailcap 文件中的条目来执行程序。它为查看、编辑、打印或撰写文件选择合适的处理程序。

mailcap 数据库将 MIME 类型映射到应用程序，从而能够根据内容类型自动处理文件。命令 **see**、**edit**、**compose** 和 **print** 是别名，分别默认对应 view、edit、compose 和 print 动作。

# CAVEATS

行为取决于 mailcap 的配置。某些 MIME 类型可能没有配置处理程序。

# HISTORY

属于 **mime-support** 软件包，基于 RFC 1524 mailcap 规范提供 MIME 类型处理工具。

# INSTALL

```aur: yay -S run-mailcap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[see](/man/see)(1), [edit](/man/edit)(1), [compose](/man/compose)(1), [print](/man/print)(1), [xdg-open](/man/xdg-open)(1), [file](/man/file)(1)
