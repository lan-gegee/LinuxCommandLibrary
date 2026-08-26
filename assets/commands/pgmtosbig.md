# TAGLINE

将 PGM 图像转换为天文 CCD 相机使用的 SBIG Type 3 格式

# TLDR

**将 PGM 文件转换为 SBIG 格式**

```pgmtosbig [input.pgm] > [output.sbig]```

**从 stdin 转换为 SBIG 格式**

```pgmtosbig < [input.pgm] > [output.sbig]```

# SYNOPSIS

**pgmtosbig** [_pgmfile_]

# DESCRIPTION

**pgmtosbig** 将 PGM（Portable Graymap）图像转换为 SBIG Type 3 格式，这是 Santa Barbara Instrument Group（SBIG）天文 CCD 相机使用的未压缩图像格式。

输出是未压缩的图像数据，其头部将来源标识为 ST-6 相机，并包含相机类型、图像尺寸和饱和度等级等元数据。

注意，SBIG Type 3 与较旧的 SBIG ST-4 格式不同，后者由 [pgmtost4](/man/pgmtost4)(1) 处理。反向转换由 [sbigtopgm](/man/sbigtopgm)(1) 完成。

该程序接受文件参数或标准输入作为输入，写入标准输出。除 Netpbm 通用选项外没有其他专属选项。属于 Netpbm 工具集（自 Netpbm 10.70 起）。

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

[sbigtopgm](/man/sbigtopgm)(1), [pgmtost4](/man/pgmtost4)(1), [fitstopnm](/man/fitstopnm)(1), [netpbm](/man/netpbm)(1)
