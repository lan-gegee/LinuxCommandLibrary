# TAGLINE

批量转换相机 RAW 照片

# TLDR

**将 RAW 转换为 JPEG**

```ufraw-batch --out-type=jpeg [image.raw]```

**转换为 TIFF**

```ufraw-batch --out-type=tiff [image.raw]```

**设置输出目录**

```ufraw-batch --out-path=[output/] [image.raw]```

**应用白平衡**

```ufraw-batch --wb=camera [image.raw]```

**批量处理**

```ufraw-batch --out-type=jpeg [*.raw]```

# SYNOPSIS

**ufraw-batch** [_--out-type format_] [_--out-path dir_] [_options_] _files_

# PARAMETERS

**--out-type** _FORMAT_
> 输出格式（jpeg、tiff、png）。

**--out-path** _DIR_
> 输出目录。

**--wb** _MODE_
> 白平衡。

**--exposure** _STOPS_
> 曝光调整。

**--compression** _N_
> JPEG 质量。

# DESCRIPTION

**ufraw-batch** 是 UFRaw（Unidentified Flying Raw）的批处理模式。UFRaw 是一个读取和转换相机 RAW 图像文件的工具。它以非交互方式处理多个 RAW 文件，在转换为 JPEG、TIFF 或 PNG 输出格式之前，应用白平衡、曝光补偿和色彩校正等调整。

该工具通过 dcraw 库支持大多数主要相机制造商的 RAW 格式。调整可以通过命令行选项指定，也可以从先前保存的 UFRaw 设置文件中加载，从而在大批量图像上实现一致的处理。

输出质量、压缩率和位深均可配置。该工具还可作为 GIMP 插件集成，用于交互式 RAW 编辑。

# CAVEATS

老旧工具。可考虑 darktable-cli。RAW 格式繁多。

# HISTORY

**UFRaw**（Unidentified Flying Raw）为读取和处理相机 RAW 图像而创建。

# SEE ALSO

[darktable-cli](/man/darktable-cli)(1), [dcraw](/man/dcraw)(1), [rawtherapee-cli](/man/rawtherapee-cli)(1)
