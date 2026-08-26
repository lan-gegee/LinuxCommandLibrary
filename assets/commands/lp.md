# TAGLINE

将文件发送到打印机打印

# TLDR

**打印文件**

```lp [file.pdf]```

**用指定打印机打印**

```lp -d [printer_name] [file]```

**打印多份**

```lp -n [3] [file]```

**双面打印**

```lp -o sides=two-sided-long-edge [file]```

**打印指定页**

```lp -o page-ranges=[1-5] [file]```

**从标准输入打印**

```cat [file] | lp```

# SYNOPSIS

**lp** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要打印的文件。

**-d** _PRINTER_
> 目标打印机。

**-n** _COPIES_
> 打印份数。

**-o** _OPTION_
> 打印机选项。

**-P** _PAGES_
> 要打印的页面列表。

**-q** _PRIORITY_
> 任务优先级（1-100）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lp** 将文件发送到打印机打印。它是 System V 打印命令，与 CUPS 配合使用。

该工具将打印任务提交到打印队列。选项可控制份数、页面范围和打印质量。

# CAVEATS

需要 CUPS。打印机必须已配置。具体选项因打印机而异。

# HISTORY

lp 是 **System V** 的打印命令，现由 CUPS 实现，作为 Linux/macOS 的标准打印接口。

# INSTALL

```apt: sudo apt install lprng```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lpr](/man/lpr)(1), [lpq](/man/lpq)(1), [lprm](/man/lprm)(1), [lpoptions](/man/lpoptions)(1)
