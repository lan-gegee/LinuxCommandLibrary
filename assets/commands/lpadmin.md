# TAGLINE

配置 CUPS 打印机

# TLDR

**添加打印机**

```lpadmin -p [printer] -v [device://uri] -m [driver.ppd]```

**设置默认打印机**

```lpadmin -d [printer]```

**删除打印机**

```lpadmin -x [printer]```

**启用打印机**

```lpadmin -p [printer] -E```

**设置打印机选项**

```lpadmin -p [printer] -o [option=value]```

**添加网络打印机**

```lpadmin -p [printer] -v ipp://[host]/printers/[name] -m everywhere```

# SYNOPSIS

**lpadmin** [_options_]

# PARAMETERS

**-p** _PRINTER_
> 打印机名称。

**-v** _URI_
> 设备 URI。

**-m** _MODEL_
> 型号/PPD 文件。

**-d** _PRINTER_
> 设置默认打印机。

**-x** _PRINTER_
> 删除打印机。

**-E**
> 启用打印机。

**-o** _OPTION_
> 设置选项。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lpadmin** 用于配置 CUPS 打印机，可以添加、修改和移除打印机定义。

该工具管理打印队列、选项和驱动程序，需要管理员权限。

# CAVEATS

需要 root 权限。CUPS 必须处于运行状态。驱动程序的可用性因设备而异。

# HISTORY

lpadmin 属于 **CUPS**（Common Unix Printing System），负责 Linux 和 macOS 上的打印机管理。

# INSTALL

```apt: sudo apt install cups-client```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lp](/man/lp)(1), [lpinfo](/man/lpinfo)(8), [cupsd](/man/cupsd)(8)
