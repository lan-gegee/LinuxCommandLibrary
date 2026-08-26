# TAGLINE

解码 min12xxw 打印机驱动输出以便调试

# TLDR

**解码从标准输入管道传入的驱动数据流**

```min12xxw < [document.pbm] | esc-m```

**检查捕获到的**打印机数据文件

```esc-m < [captured.prn]```

# SYNOPSIS

**esc-m**

# DESCRIPTION

**esc-m** 是随 **min12xxw** 打印机驱动附带的一个小型调试过滤器。它从标准输入读取驱动数据流，并将其中的 ESC-M（压缩页）命令以人类可读的形式打印到标准输出。

该工具不接受任何参数或选项：它的用途只是帮助开发者和用户了解 min12xxw 驱动为 KonicaMinolta PagePro 1200W 一类打印机生成的数据内容，例如诊断打印问题或校验压缩光栅输出时。

# CAVEATS

esc-m 是诊断辅助工具，不是打印命令；它不会与打印机通信。它只认识 min12xxw 驱动产生的数据格式，喂入任意文件只会得到无意义的输出。它与 min12xxw 一起打包发行（Debian 的 printer-driver-min12xxw），而非独立工具。

# INSTALL

```apt: sudo apt install printer-driver-min12xxw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[min12xxw](/man/min12xxw)(1)

# RESOURCES

```[Homepage](http://www.hinterbergen.de/mala/min12xxw/)```

<!-- verified: 2026-07-14 -->
