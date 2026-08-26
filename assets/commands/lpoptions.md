# TAGLINE

显示或设置打印机选项与默认值

# TLDR

**显示默认选项**

```lpoptions```

**显示打印机选项**

```lpoptions -p [printer] -l```

**设置默认打印机**

```lpoptions -d [printer]```

**设置打印机选项**

```lpoptions -p [printer] -o [option=value]```

**移除选项**

```lpoptions -p [printer] -r [option]```

**列出默认打印机的选项**

```lpoptions -l```

**删除打印机实例的所有选项**

```lpoptions -x [printer/instance]```

# SYNOPSIS

**lpoptions** [_options_]

# PARAMETERS

**-d** _destination[/instance]_
> 将用户默认打印机设置为指定的目的地。

**-p** _destination[/instance]_
> 为其后的选项设置目的地和实例。

**-l**
> 列出打印机专属选项及其当前设置。

**-o** _option[=value]_
> 为指定目的地设置新选项。

**-r** _option_
> 从指定目的地移除指定选项。

**-x** _destination[/instance]_
> 移除指定目的地和实例的所有选项。

**-E**
> 与 CUPS 服务器通信时启用加密。

**-h** _server[:port]_
> 连接到指定的服务器。

# DESCRIPTION

**lpoptions** 显示或设置打印机选项与默认值。不带参数运行时，会显示默认打印机的选项。

用户级设置保存在 **~/.cups/lpoptions** 中。以 root 身份运行时，则使用 **/etc/cups/lpoptions** 中的系统级默认值。纸张尺寸、介质类型、打印质量等选项可以按打印机或按实例配置。

# CAVEATS

选项因打印机而异，不同设备之间可能不同。/etc/cups/lpoptions 中的系统级选项需要 root 权限。实例机制允许为同一台打印机定义多组命名的选项集合。

# HISTORY

lpoptions 属于 **CUPS**，用于配置默认的打印机选项和打印目的地。

# INSTALL

```apt: sudo apt install cups-client```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lp](/man/lp)(1), [lpadmin](/man/lpadmin)(8), [lpstat](/man/lpstat)(1), [lpr](/man/lpr)(1), [lpq](/man/lpq)(1), [cups](/man/cups)(1)
