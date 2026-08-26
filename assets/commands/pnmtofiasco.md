# TAGLINE

将 PNM 转换为 FIASCO 小波格式

# TLDR

**将 PNM 转换为 FIASCO 格式**

```pnmtofiasco [input.pnm] -o [output.fco]```

**指定质量**（1=最差，100=最好，默认 20）

```pnmtofiasco -q [50] [input.pnm] -o [output.fco]```

**设置优化级别**（0=最快，3=最慢）

```pnmtofiasco -z [2] [input.pnm] -o [output.fco]```

**详细**的压缩统计信息

```pnmtofiasco -V [2] [input.pnm] -o [output.fco]```

# SYNOPSIS

**pnmtofiasco** [_options_] [_file_]

# PARAMETERS

**-o, --output-name=**_file_
> 将 FIASCO 输出写入指定的文件。默认写到标准输出。

**-q, --quality=**_N_
> 压缩质量（1=最差，100=最好）。默认为 20。

**-z, --optimize=**_N_
> 优化级别（0=最快，3=最慢）。默认为 0。

**-b, --basis-name=**_name_
> 预加载压缩基（如 small.fco、medium.fco、large.fco）。

**-V, --verbose=**_N_
> 输出详细程度：0（无输出）、1（进度条）、2（详细统计）。默认为 1。

**-v, --version**
> 打印版本号并退出。

**-h, --info**
> 打印简要帮助。

**-P, --prediction**
> 为视频序列启用预测编码。

# DESCRIPTION

**pnmtofiasco** 压缩 PBM、PGM 或 PPM 图像（未指定文件时读取标准输入），并在标准输出上生成 FIASCO（Fractal Image And Sequence COdec）文件。FIASCO 采用基于分形与小波的压缩技术。属于 Netpbm 工具集。

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

[fiascotopnm](/man/fiascotopnm)(1), [pnmtojpeg](/man/pnmtojpeg)(1)
