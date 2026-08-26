# TAGLINE

显示内核检测到的已安装硬件信息，数据读取自

# TLDR

列出**已安装的硬件**

```lsdev```

# SYNOPSIS

**lsdev**

# DESCRIPTION

**lsdev** 显示内核检测到的已安装硬件信息，读取自 /proc/interrupts、/proc/ioports 和 /proc/dma。它展示设备名称及其关联的 IRQ、DMA 和 I/O 端口范围。

# CAVEATS

属于 procinfo 软件包的一部分。仅提供简单概览；详细硬件信息请使用 lspci、lsusb 或 lshw。

# INSTALL

```apt: sudo apt install procinfo```

```dnf: sudo dnf install procinfo```

```zypper: sudo zypper install procinfo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lspci](/man/lspci)(8), [lsusb](/man/lsusb)(8), [lshw](/man/lshw)(1), [hwinfo](/man/hwinfo)(8)
