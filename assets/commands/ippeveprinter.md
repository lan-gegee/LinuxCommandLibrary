# TAGLINE

实现符合 IPP Everywhere 标准虚拟打印机的开发与测试工具

# TLDR

**启动一台 IPP Everywhere 打印机**用于测试

```ippeveprinter [TestPrinter]```

**在特定端口上启动打印机**

```ippeveprinter -p [8631] [TestPrinter]```

**用特定命令创建打印机**来处理作业

```ippeveprinter -c '[/usr/bin/cat > /tmp/printjob.pdf]' [TestPrinter]```

**以详细日志启动打印机**

```ippeveprinter -v [TestPrinter]```

**创建通过 DNS-SD 广告的打印机**

```ippeveprinter -d [TestPrinter]```

# SYNOPSIS

**ippeveprinter** [_-c command_] [_-d_] [_-p port_] [_-v_] _service-name_

# PARAMETERS

**-c** _command_
> 为每个打印作业运行的命令（作业数据通过 stdin 传入）

**-d**
> 使用 DNS-SD/Bonjour 广告该打印机

**-p** _port_
> 要监听的端口号（默认：自动分配）

**-v**
> 详细模式；显示详细日志

**-2**
> 支持双面打印

**-M** _manufacturer_
> 打印机的制造商名称

**-m** _model_
> 打印机的型号名称

**-i** _iconfile_
> 打印机的图标文件

**-l** _location_
> 打印机的位置字符串

# DESCRIPTION

**ippeveprinter** 是一个实现符合 IPP Everywhere 标准的虚拟打印机的开发与测试工具。IPP Everywhere 是 PWG（Printer Working Group，打印机工作组）的标准，支持无驱动打印。

该工具创建一个通过网络打印协议（IPP）接受打印作业的网络打印机。作业可以由自定义命令处理，或仅记录下来用于测试。这可用于测试 IPP 客户端、开发打印工作流或调试打印机发现。

# CAVEATS

不适合作为生产环境的打印服务器。打印机只在命令运行期间存在。接受远程连接时需要适当的防火墙规则。属于 CUPS 的一部分，但功能因版本而异。

# HISTORY

**ippeveprinter** 是 **CUPS**（Common Unix Printing System）项目的一部分，最初由 Easy Software Products 的 Michael Sweet 开发，后由 Apple 维护。加入 IPP Everywhere 支持是为了便于进行无驱动打印标准的合规性测试。

# INSTALL

```apt: sudo apt install cups-ipp-utils```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ippfind](/man/ippfind)(1), [ipptool](/man/ipptool)(1), [cupsd](/man/cupsd)(8), [lp](/man/lp)(1)
