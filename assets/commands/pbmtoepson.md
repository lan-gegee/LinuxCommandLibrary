# TAGLINE

将 PBM 位图转换为 Epson 打印机控制码以便直接打印

# TLDR

**将 PBM 转换为 Epson 打印机格式**

```pbmtoepson [input.pbm] | lpr```

**指定协议**

```pbmtoepson -protocol [escp] [input.pbm] > [output.escp]```

# SYNOPSIS

**pbmtoepson** [_options_] [_file_]

# PARAMETERS

**-protocol** _TYPE_
> 输出协议：**escp**（较新的 ESC/P）或 **escp9**（较旧的 9 针 ESC/P）。默认为 escp。

**-dpi** _N_
> 水平打印密度，单位为每英寸点数。允许的值：60、72、80、90、120、144、240。

**-adjacent**
> 强制相邻点打印。

**-nonadjacent**
> 强制非相邻点打印。

# DESCRIPTION

**pbmtoepson** 读取 PBM 图像作为输入，输出 Epson 打印机图形指令流。支持 ESC/P 和 ESC/P 9 针协议。对于较新的 ESC/P2 协议，请改用 **pbmtoescp2**。属于 Netpbm 工具集。

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

[pbmtoescp2](/man/pbmtoescp2)(1), [pbmtolj](/man/pbmtolj)(1)
