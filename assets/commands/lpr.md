# TAGLINE

提交打印任务

# TLDR

**打印文件**

```lpr [file]```

**用指定打印机打印**

```lpr -P [printer] [file]```

**打印多份**

```lpr -# [3] [file]```

**从标准输入打印**

```cat [file] | lpr```

**打印后删除文件**

```lpr -r [file]```

**为任务指定标题**

```lpr -T "[title]" [file]```

# SYNOPSIS

**lpr** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要打印的文件。

**-P** _PRINTER_
> 目标打印机。

**-#** _COPIES_
> 打印份数。

**-r**
> 打印后删除文件。

**-T** _TITLE_
> 任务标题。

**-o** _OPTION_
> 打印机选项。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lpr** 提交文件进行打印。它将一个或多个文件发送到默认打印机或用 **-P** 指定的打印机。文件按提交顺序排队打印。

在现代 Linux 系统上，lpr 由 **CUPS**（Common Unix Printing System）提供。不带参数时它会读取标准输入，因此适合在管道中使用（如 `ls | lpr`）。纸张尺寸和双面打印等打印机选项可用 **-o** 设置。

# CAVEATS

需要 CUPS。System V 风格请使用 lp。选项因打印机而异。

# HISTORY

lpr 起源于 **BSD Unix** 的行式打印机假脱机程序，现由 CUPS 实现。

# INSTALL

```apt: sudo apt install lpr```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lp](/man/lp)(1), [lpq](/man/lpq)(1), [lprm](/man/lprm)(1)
