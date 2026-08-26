# TAGLINE

将 PAM 图像转换为 PNM 格式

# TLDR

**将 PAM 转换为 PNM 格式**

```pamtopnm [input.pam] > [output.pnm]```

**使用 -assume 跳过元组类型检查进行转换**

```pamtopnm -assume [input.pam] > [output.pnm]```

**静默转换，不输出提示信息**

```pamtopnm -quiet [input.pam] > [output.pnm]```

# SYNOPSIS

**pamtopnm** [**-assume**] [**-quiet**] [_file_]

# PARAMETERS

**-assume**
> 覆盖对元组类型的要求。无论 PAM 的元组类型是什么，都断言其元组包含有效的 PBM、PGM 或 PPM 数据。深度仍必须符合目标格式。

**-quiet**
> 抑制输出到标准错误的提示信息。

# DESCRIPTION

**pamtopnm** 读取 PAM 图像作为输入，并生成等价的 PBM、PGM 或 PPM（即 PNM）图像作为输出。输出格式根据输入自动选择：BLACKANDWHITE 变为 PBM，GRAYSCALE 变为 PGM，RGB 变为 PPM。

如果输入的 PAM 不具备合适的元组类型（BLACKANDWHITE、GRAYSCALE 或 RGB）和深度，除非指定 **-assume**，否则 pamtopnm 会失败。要强制转换带有额外通道的图像，请先用 **pamchannel** 处理输入以选出所需的通道。

属于 Netpbm 工具集。

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

[pamtopam](/man/pamtopam)(1), [netpbm](/man/netpbm)(1)
