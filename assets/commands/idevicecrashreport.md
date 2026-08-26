# TAGLINE

将崩溃报告从设备转移到本地目录

# TLDR

**转移崩溃报告**：从设备到本地目录（会从设备上删除）

```idevicecrashreport [output-dir]```

**复制崩溃报告**但保留在设备上

```idevicecrashreport -k [output-dir]```

**提取原始崩溃报告**为独立的 .crash 文件

```idevicecrashreport -e [output-dir]```

**按名称过滤崩溃报告**（区分大小写）

```idevicecrashreport -f [app-name] [output-dir]```

**删除设备上的所有崩溃日志**而不复制

```idevicecrashreport --remove-all```

**按 UDID 指定目标设备**

```idevicecrashreport -u [device-udid] [output-dir]```

**连接网络设备**

```idevicecrashreport -n [output-dir]```

# SYNOPSIS

**idevicecrashreport** [_OPTIONS_] _DIRECTORY_

# PARAMETERS

**-u**, **--udid** _UDID_
> 按 UDID 指定目标设备。

**-n**, **--network**
> 连接到网络设备。

**-e**, **--extract**
> 将原始崩溃报告提取为独立的 '.crash' 文件。

**-k**, **--keep**
> 复制但不从设备上移除崩溃报告。

**-f**, **--filter** _NAME_
> 按 NAME 过滤崩溃报告（区分大小写）。

**--remove-all**
> 不复制而直接移除所有崩溃日志文件。可与 -f 组合，仅移除匹配的文件。

**-d**, **--debug**
> 启用通信调试。

**-h**, **--help**
> 打印用法信息。

**-v**, **--version**
> 打印版本信息。

# DESCRIPTION

**idevicecrashreport** 是一个将崩溃报告从 iOS 设备转移到本地目录的简单工具，属于 libimobiledevice 套件。默认会移动报告（即从设备上删除）；使用 **-k** 可改为复制。它下载 .crash、.ips 及相关诊断文件。无需 iTunes 或 Xcode 即可调试应用崩溃。

输出行根据是创建了符号链接、复制了文件还是从设备上移动了文件，分别以 "Link:"、"Copy:" 或 "Move:" 作为前缀。

# INSTALL

```apt: sudo apt install libimobiledevice-utils```

```dnf: sudo dnf install libimobiledevice-utils```

```apk: sudo apk add libimobiledevice-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ideviceinfo](/man/ideviceinfo)(1), [idevicediagnostics](/man/idevicediagnostics)(1), [idevicesyslog](/man/idevicesyslog)(1)

