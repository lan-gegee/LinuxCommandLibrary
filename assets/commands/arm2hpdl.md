# TAGLINE

用 HP 下载头/尾包装 ARM ELF 打印机固件镜像

# TLDR

**将 ARM 固件镜像转换**为 HP `.dl` 下载文件

```arm2hpdl [sihp1005.img] > [sihp1005.dl]```

**启用调试输出**

```arm2hpdl -D [1] [firmware.img] > [firmware.dl]```

**将结果直接通过管道发送到打印机设备**

```arm2hpdl [firmware.img] | lp -d [printer]```

# SYNOPSIS

**arm2hpdl** [**-D** _level_] _arm-binary.img_ > _hpdl.dl_

# DESCRIPTION

**arm2hpdl** 读取 HP 激光打印机的 ARM ELF 二进制固件镜像（通常是 HP 发布的名为 `sihpXXXX.img` 的文件），并向标准输出写入同一镜像加上打印机固件加载器所要求的 HP 下载头和下载尾。如果输入已带有 HP 头，则文件原样复制输出。

生成的 `.dl` 文件可以通过 USB、并口或网络作为普通打印任务发送到打印机，以刷写固件。

# PARAMETERS

_arm-binary.img_
> 输入的 ARM ELF 固件镜像。

**-D** _level_
> 设置调试级别（默认 `0`）。更高的级别会向 stderr 打印解析细节。

# CAVEATS

仅适用于由 **foo2zjs**/QPDL 工具族驱动的 HP 激光打印机。刷入错误或不匹配的固件可能导致打印机变砖——发送 `.dl` 文件前请核对型号和版本。输出为二进制数据；务必重定向到文件（或直接通过管道送往打印机设备），切勿输出到终端。

# HISTORY

**arm2hpdl** 由 **Rick Richardson** 编写，是 **foo2zjs** 打印机驱动项目的一部分，该项目为 Linux 逆向工程了 HP/三星的 QPDL 和 ZjStream 协议。

# INSTALL

```apt: sudo apt install printer-driver-foo2zjs```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[foo2zjs](/man/foo2zjs)(1), [foo2zjs-wrapper](/man/foo2zjs-wrapper)(1), [lp](/man/lp)(1), [lpr](/man/lpr)(1)
