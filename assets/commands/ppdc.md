# TAGLINE

编译 CUPS PPD 打印机驱动文件

# TLDR

**编译 PPD 文件**

```ppdc [driver.drv]```

**编译到指定目录**

```ppdc -d [output_dir] [driver.drv]```

**详细输出**

```ppdc -v [driver.drv]```

# SYNOPSIS

**ppdc** [_options_] _source_

# PARAMETERS

_SOURCE_
> 驱动源文件。

**-d** _DIR_
> 输出目录。

**-v**
> 详细输出。

**-I** _DIR_
> 包含目录（include 目录）。

# DESCRIPTION

**ppdc** 将 CUPS 打印机驱动源文件（.drv）编译为 PPD（PostScript Printer Description）文件。PPD 文件描述打印机的功能，包括支持的纸张尺寸、分辨率、彩色模式和可选特性，CUPS 用它来生成相应的打印作业数据。

驱动源格式提供了一种紧凑的方式，可在单个文件中定义多款打印机型号，共享选项并针对具体型号进行覆盖。编译出的 PPD 文件可以放入 CUPS 的 model 目录，用于自动检测和设置打印机。

# CAVEATS

仅适用于 CUPS。PPD 文件用于打印机支持。

# HISTORY

ppdc 是 **CUPS** 的组成部分，用于编译 PPD 文件。

# INSTALL

```apt: sudo apt install cups-ppdc```

```dnf: sudo dnf install cups-client```

```apk: sudo apk add cups-client```

```zypper: sudo zypper install cups-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ppdhtml](/man/ppdhtml)(1), [ppdi](/man/ppdi)(1), [cups](/man/cups)(1)
