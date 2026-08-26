# TAGLINE

优化 Android APK 文件对齐

# TLDR

**对齐 APK 文件**，使用 4 字节对齐以及共享库 16 KiB 页面对齐

```zipalign -P 16 -f -v 4 [input.apk] [output.apk]```

**验证** APK 的**对齐**

```zipalign -c -P 16 -v 4 [path/to/file.apk]```

**仅进行基本的 4 字节对齐**

```zipalign -v 4 [input.apk] [output.apk]```

**强制覆盖**已有的输出文件

```zipalign -f 4 [input.apk] [output.apk]```

**检查对齐而不输出详细信息**

```zipalign -c 4 [path/to/file.apk]```

# SYNOPSIS

**zipalign** [_-c_] [_-f_] [_-P_ _pagesize_kb_] [_-v_] [_-z_] _alignment_ _input.apk_ [_output.apk_]

# PARAMETERS

**-c**
> 仅检查对齐（确认模式）。不修改文件。

**-f**
> 强制覆盖已有的输出文件。

**-P** _pagesize_kb_
> 将未压缩的 .so 文件按指定的页大小（KiB）进行页面对齐。有效值为 **4**、**16** 或 **64**。使用 **-P 16** 可同时兼容 4 KiB 和 16 KiB 页面大小的设备。

**-p**
> 已弃用。针对 .so 文件的旧式 4 KiB 页面对齐。请改用 **-P 16**。

**-v**
> 详细输出，显示归档中每个文件的对齐状态。

**-z**
> 使用 Zopfli 重新压缩以获得更小的文件体积（较慢）。

**-h**
> 显示帮助信息。

_alignment_
> 字节对齐边界。APK 文件始终使用 **4**。

_input.apk_
> 要处理的输入 APK 文件。

_output.apk_
> 对齐后的输出 APK 文件（使用 -c 时可省略）。

# DESCRIPTION

**zipalign** 是 Android SDK 提供的归档对齐工具，通过确保所有未压缩数据相对于文件起始位置按特定字节边界对齐来优化 APK 文件。这项优化使 Android 能够直接从 APK 内存映射文件，降低 RAM 占用并提升应用启动性能。

该工具通过调整 ZIP 条目中的 extra field 填充，使文件数据边界对齐到指定值（APK 恒为 4 字节）。这使 Android 运行时可以用 **mmap()** 访问未压缩资源，而不是将其复制到堆中。

正确的操作顺序取决于所用的签名工具。使用 **apksigner** 时，应在签名**之前**运行 zipalign。使用 **jarsigner** 时，应在签名**之后**运行 zipalign。对于 Android App Bundle（AAB），无需 zipalign，因为 Google Play 会在生成 APK 时处理优化。

该工具位于 Android SDK 的 **build-tools** 目录中（例如 `$ANDROID_HOME/build-tools/34.0.0/zipalign`）。

# CAVEATS

与签名的先后顺序取决于工具：在 apksigner **之前**运行 zipalign，但在 jarsigner **之后**运行。面向 Android 15+ 的应用必须使用 **-P 16**，以便为 16 KiB 页面大小的设备正确对齐原生库。不适用于 Android App Bundle（AAB）。APK 的对齐值应始终为 4。Zipalign 不执行签名。小写的 **-p** 标志已弃用，请改用 **-P**。

# HISTORY

**zipalign** 由 Google 作为 Android SDK 工具的一部分推出。它成为标准 Android 构建流程的一环，以确保最佳的运行时性能。自 **2025 年 11 月**起，Google Play 要求所有面向 Android 15+ 的应用在 64 位设备上支持 16 KiB 页面大小，这使得 **-P 16** 标志对带原生库的应用至关重要。

# INSTALL

```apt: sudo apt install zipalign```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apksigner](/man/apksigner)(1), [aapt](/man/aapt)(1), [aapt2](/man/aapt2)(1), [adb](/man/adb)(1), [bundletool](/man/bundletool)(1)
