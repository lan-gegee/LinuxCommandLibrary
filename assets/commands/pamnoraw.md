# TAGLINE

将二进制 PNM 图像转换为纯文本（ASCII）格式

# TLDR

**将 PNM 图像转换为**纯文本格式

```pamnoraw [input.ppm] > [output.ppm]```

# SYNOPSIS

**pamnoraw** [_file_]

# DESCRIPTION

**pamnoraw** 将二进制（raw）PNM 图像转换为纯文本（ASCII）格式。纯文本格式人类可读，但体积要大得多。效果等同于运行 `pamtopnm -plain`。注意 PAM 图像没有纯文本格式，因此该工具只适用于 PBM、PGM 和 PPM 输入。属于 Netpbm 工具集。

# SEE ALSO

[pamtopnm](/man/pamtopnm)(1), [pnmtoplainpnm](/man/pnmtoplainpnm)(1), [pamfile](/man/pamfile)(1), [netpbm](/man/netpbm)(1)
