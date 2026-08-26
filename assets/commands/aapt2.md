# TAGLINE

新一代 Android 资源编译与打包工具

# TLDR

**编译单个资源文件**

```aapt2 compile [path/to/resource.xml] -o [output_directory]```

**编译目录中的所有资源**

```aapt2 compile --dir [path/to/res] -o [resources.zip]```

**链接编译后的资源生成 APK**

```aapt2 link -o [output.apk] -I [android.jar] [compiled_resources.flat] --manifest [AndroidManifest.xml]```

**导出 APK 信息**

```aapt2 dump [badging|permissions|resources] [path/to/app.apk]```

**在 APK 格式之间转换**

```aapt2 convert -o [output.apk] [input.apk]```

**优化 APK**

```aapt2 optimize -o [optimized.apk] [input.apk]```

# SYNOPSIS

**aapt2** _command_ [_options_] [_files_]

# PARAMETERS

**compile**
> 把单个资源文件编译为二进制格式（.flat 文件）。

**link**
> 合并编译后的资源，生成最终的 APK 或资源表。

**dump**
> 打印 APK 信息（badging、permissions、resources、configurations）。

**diff**
> 比较两个 APK 并显示差异。

**optimize**
> 从体积和性能角度优化 APK 资源。

**convert**
> 在 APK 的二进制与 proto 格式之间转换。

**-o** _file_
> 指定输出文件或目录。

**-I** _path_
> 向 include 路径添加一个 Android JAR 或 APK（通常为 android.jar）。

**--dir** _path_
> 编译指定目录中的所有资源。

**--manifest** _file_
> 链接时指定 AndroidManifest.xml 文件。

**-v**
> 启用详细输出。

**--help**
> 显示某个具体命令的帮助。

# DESCRIPTION

**aapt2**（Android Asset Packaging Tool 2）是 Google 用于编译和打包 Android 应用资源的下一代工具。它以更快的增量编译方式取代了原版 aapt 工具。

该工具分两个主要阶段工作：**compile** 将单个资源文件（XML、PNG 等）转换为中间二进制格式（.flat 文件），**link** 则把这些编译好的资源与清单合并，产出最终的 APK 或资源归档。这种分离机制支持增量构建——只有发生变化的资源才需要重新编译。

aapt2 通常由 Gradle 等构建系统自动调用，但也可以直接用于自定义构建流水线、调试资源问题或检查 APK 内容。

# CAVEATS

aapt2 的校验比原版 aapt 更严格，对于 aapt 默默接受的畸形资源会直接报错。资源文件名必须为小写，且只能包含 **a-z**、**0-9** 和下划线。该工具随 Android SDK Build Tools 分发，并且需要与目标 API 级别对应的 android.jar。

# HISTORY

**aapt2** 由 Google 于 **2017 年**随 Android Studio 3.0 和 Android Gradle Plugin 3.0 推出。其开发目的是解决原版 aapt 工具的性能局限，尤其是拥有大量资源的大型项目的构建速度。增量编译模型避免了重新处理未变化的资源，显著缩短了构建时间。

# INSTALL

```apt: sudo apt install aapt```

```nix: nix profile install nixpkgs#aapt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aapt](/man/aapt)(1), [apksigner](/man/apksigner)(1), [zipalign](/man/zipalign)(1), [adb](/man/adb)(1), [bundletool](/man/bundletool)(1)

# RESOURCES

```[Source code](https://android.googlesource.com/platform/frameworks/base/+/refs/heads/main/tools/aapt2)```

```[Documentation](https://developer.android.com/tools/aapt2)```

<!-- verified: 2026-06-10 -->
