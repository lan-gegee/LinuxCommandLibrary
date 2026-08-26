# TAGLINE

将 PNM 转换为 plain ASCII 格式（已过时）

# TLDR

**将 PNM 图像转换为 plain ASCII 格式**

```pnmtoplainpnm [input.pnm] > [output.pnm]```

**从标准输入读取并把 plain 格式写入文件**

```cat [input.pnm] | pnmtoplainpnm > [output.pnm]```

# SYNOPSIS

**pnmtoplainpnm** [_file_]

# DESCRIPTION

**pnmtoplainpnm** 读取一幅 PNM 图像作为输入，并以 plain（ASCII）PNM 格式写出等价的图像。plain 格式便于人阅读，但体积明显大于二进制（raw）格式。属于 Netpbm 工具集。

**pnmtoplainpnm** 在 Netpbm 10.23（2004 年 7 月）中被 **pamtopnm** 取代。它仅为向后兼容而保留；其全部功能就是调用 `pamtopnm -plain`。现代推荐的做法是在任意 Netpbm 程序上使用 **-plain** 这个通用选项。

# HISTORY

**pnmtoplainpnm** 首次出现于 Netpbm 8.2（2000 年 3 月），是对 **pnmnoraw** 的更名；后者于 1989 年 11 月随 Pbmplus 推出。它在 Netpbm 10.23（2004 年 7 月）中被 **pamtopnm** 取代。

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

[pamtopnm](/man/pamtopnm)(1), [pnmtopnm](/man/pnmtopnm)(1), [pnm](/man/pnm)(1)
