# TAGLINE

将 HP ThinkJet 格式转换为 PBM 格式

# TLDR

**将 HP ThinkJet 转换为 PBM**

```thinkjettopbm [input.thinkjet] > [output.pbm]```

**转换并输出调试信息**

```thinkjettopbm -debug [input.thinkjet] > [output.pbm]```

# SYNOPSIS

**thinkjettopbm** [**-debug**] [_thinkjet_file_]

# PARAMETERS

**-debug**
> 在标准错误上输出诊断信息。

# DESCRIPTION

**thinkjettopbm** 从指定文件（或标准输入）读取 HP ThinkJet 打印机命令，并在标准输出生成 PBM 图像。它会静默忽略文本及非图形命令序列。

该程序仅处理 ThinkJet 命令序列的一小部分子集，但已足以转换老旧 HP 测试设备生成的屏幕图像。它是 **Netpbm** 工具包的一部分。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pbmtolj](/man/pbmtolj)(1), [ppmtolj](/man/ppmtolj)(1), [ppmtopj](/man/ppmtopj)(1), [pjtoppm](/man/pjtoppm)(1), [pnmtopclxl](/man/pnmtopclxl)(1), [netpbm](/man/netpbm)(1)
