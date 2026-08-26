# TAGLINE

从命令行批量处理 RAW 照片

# TLDR

**将 RAW 转换为 JPEG**

```rawtherapee-cli -o [output.jpg] -c [input.raw]```

**应用处理配置文件**

```rawtherapee-cli -p [profile.pp3] -o [output.jpg] -c [input.raw]```

**批量转换目录**

```rawtherapee-cli -o [output_dir/] -c [input_dir/]```

**输出为 TIFF**

```rawtherapee-cli -t -o [output.tif] -c [input.raw]```

# SYNOPSIS

**rawtherapee-cli** [_options_] **-c** _input_files_

# PARAMETERS

**-c** _FILES_
> 指定要转换的输入文件/目录。必须是**最后一个**参数。

**-o** _PATH_
> 输出文件或目录。

**-O** _PATH_
> 与 **-o** 类似，但还会把所应用的 .pp3 配置文件作为附属文件复制到输出旁边。

**-p** _FILE.pp3_
> 应用给定的处理配置文件。

**-d**
> 使用内置的默认处理配置文件。

**-s**, **-S**
> 使用输入文件旁已有的附属 .pp3 文件。**-S** 会跳过没有附属文件的图像；**-s** 则静默回退到默认配置文件。

**-q** _FILE_
> 为每张处理的图像使用替代的附属文件。

**-a**
> 处理所有受支持的文件，包括隐藏文件。

**-j**[_1-100_]
> 输出 JPEG；质量值**紧跟**在选项后面，中间没有空格（例如 `-j95`）。强制 8 位输出。

**-js**_1_|_2_|_3_
> JPEG 色度子采样：**1** = 4:2:0，**2** = 4:2:2，**3** = 4:4:4。

**-t**[**z**]
> 输出 TIFF；追加 **z**（`-tz`）表示 ZIP 压缩。

**-n**
> 输出 PNG（不压缩）。

**-b**_8_|_16_|_16f_|_32_
> TIFF/PNG 的输出位深（JPEG 始终为 8 位）。

**-f**
> 快速导出模式（质量降低，处理更快）。

**-Y**
> 覆盖已存在的输出文件。

**-h**, **-?**
> 显示帮助。

# DESCRIPTION

**rawtherapee-cli** 是 RawTherapee 的命令行界面，用于处理 RAW 图像文件。它在批处理模式下提供与 GUI 版本相同的强大处理能力。

# EXAMPLES

```bash
# Basic conversion
rawtherapee-cli -o output.jpg -c photo.CR2

# With profile
rawtherapee-cli -p default.pp3 -o output.jpg -c input.NEF

# Batch convert folder
rawtherapee-cli -o processed/ -c raw_photos/

# High quality JPEG
rawtherapee-cli -j95 -o high_quality.jpg -c input.raw

# 16-bit TIFF
rawtherapee-cli -t -b16 -o output.tif -c input.raw
```

# PROFILES

处理配置文件（.pp3）可以：
- 在 RawTherapee GUI 中创建
- 位于 /usr/share/rawtherapee/profiles/
- 是附属文件（filename.pp3）

# CONFIGURATION

**/usr/share/rawtherapee/profiles/**
> 系统级处理配置文件（.pp3），为不同风格和校正提供预设的显影设置。

**~/.config/RawTherapee/profiles/**
> 从 RawTherapee GUI 保存的用户自建处理配置文件。

**Sidecar .pp3 files**
> 存储在 RAW 文件旁的每图像处理配置文件（如 photo.CR2.pp3），在没有显式指定配置文件时自动应用。

# CAVEATS

需要安装 RawTherapee。处理过程占用大量 CPU。支持大多数 RAW 格式。

# HISTORY

RawTherapee 由 **Gábor Horváth** 于 2004 年创建，随后加入 CLI 以支持批处理工作流。

# INSTALL

```apt: sudo apt install rawtherapee```

```dnf: sudo dnf install rawtherapee```

```pacman: sudo pacman -S rawtherapee```

```apk: sudo apk add rawtherapee```

```zypper: sudo zypper install rawtherapee```

```nix: nix profile install nixpkgs#rawtherapee```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[darktable-cli](/man/darktable-cli)(1), [dcraw](/man/dcraw)(1), [convert](/man/convert)(1)
