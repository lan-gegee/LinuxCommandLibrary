# TAGLINE

将多图像 PAM/PNM 流拆分为单独的文件

# TLDR

**拆分多图像 PAM/PNM 流**为带编号的文件

```pamsplit [input.pam] "[image%d.pam]"```

**填充**序列号至固定宽度

```pamsplit -padname [4] [input.pam] "[image%d.pam]"```

**使用默认文件名**（image0.pam、image1.pam 等）

```pamsplit [input.pam]```

**从标准输入读取**并写出带编号的文件

```cat [stream.pnm] | pamsplit - "[frame%d.pnm]"```

# SYNOPSIS

**pamsplit** [**-padname** _digits_] [_inputfile_] [_outputpattern_]

# PARAMETERS

_inputfile_
> 多图像 PAM/PNM 输入文件。使用 **-** 或省略该参数则从标准输入读取。

_outputpattern_
> 输出文件名模式，其中包含一个 **%d**，会被替换为（从 0 开始的）图像索引。默认为 **image%d**。

**-padname** _digits_
> 用前导零把序列号填充到至少 _digits_ 位（例如 **-padname 3** 会生成 image000、image001 等）。有助于确保输出文件按字典序排列。

# DESCRIPTION

**pamsplit** 读取包含多个串联的 PAM、PNM、PBM、PGM 或 PPM 图像的 Netpbm 流，并将每个图像写入单独的文件。输出文件名由 printf 风格的模式生成，其中的 **%d** 代表图像索引。

该工具是 **pnmcat** / **pamcat** 的逆操作，属于 **Netpbm** 软件包。

# CAVEATS

输出模式必须恰好包含一个 **%d** 说明符。生成路径上已存在的文件会被静默覆盖。对于没有 Alpha 通道的 PBM/PGM/PPM 流，**pamsplit** 会保留每一帧的原始格式。

# HISTORY

**pamsplit** 是由 Bryan Henderson 等人开发的 **Netpbm** 软件包的一部分，取代了 PBMplus 中较旧的 **pnmsplit** 工具。

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

[pamundice](/man/pamundice)(1), [pnmcat](/man/pnmcat)(1), [netpbm](/man/netpbm)(1)
