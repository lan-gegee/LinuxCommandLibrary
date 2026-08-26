# TAGLINE

Android 资源打包工具

# TLDR

**列出** APK 文件的**内容**

```aapt list [app.apk]```

从 APK 中**导出** AndroidManifest.xml

```aapt dump xmltree [app.apk] AndroidManifest.xml```

从 APK 中**提取包名**和版本号

```aapt dump badging [app.apk]```

将资源**打包**进 APK

```aapt package -f -M [AndroidManifest.xml] -S [res/] -I [android.jar] -F [output.apk]```

# SYNOPSIS

**aapt** _command_ [_options_] [_file_]

# DESCRIPTION

**aapt**（Android Asset Packaging Tool）是 Android 开发中使用的构建工具，用于把应用资源打包成 APK 文件。它编译资源、生成包含资源标识符的 R.java 文件，还能检查现有的 APK 文件。

该工具负责资源编译、XML 处理、资产打包和 APK 创建。它读取 AndroidManifest.xml，处理 drawable、layout 等资源文件，并把它们打包进最终的应用包。虽然在现代 Android 开发中已基本被 aapt2 取代，aapt 在检查 APK 和维护旧项目时仍然有用。

# PARAMETERS

**list**
> 列出一个 ZIP 兼容归档（APK）的内容

**dump**
> 从 APK 中导出特定信息：badging、permissions、resources、configurations、xmltree、xmlstrings

**package**
> 将资源和资产打包为 APK

**-f**
> 强制覆盖已有文件

**-M** _file_
> 指定 AndroidManifest.xml 的位置

**-S** _dir_
> 指定资源目录

**-I** _jar_
> 向基础 include 集合添加一个已有的包（通常是 android.jar）

**-F** _file_
> 指定输出的 APK 文件

**-v**
> 详细输出

# CAVEATS

自 Android Gradle Plugin 3.0 起，**aapt** 已被 **aapt2** 取代。旧工具缺乏增量编译支持，在大项目上性能也较慢。混用两种工具时，资源处理差异可能导致问题。

# HISTORY

**aapt** 于 **2008 年**作为 Android SDK 的一部分随 Android 首次公开发布推出。它一直是主要的资源打包工具，直到 **2017 年** Google 推出了性能更好、支持增量构建的 aapt2。出于兼容性考虑，原版 aapt 仍保留在 SDK 中。

# INSTALL

```apt: sudo apt install aapt```

```nix: nix profile install nixpkgs#aapt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aapt2](/man/aapt2)(1), [apksigner](/man/apksigner)(1), [apktool](/man/apktool)(1), [zipalign](/man/zipalign)(1), [adb](/man/adb)(1)

# RESOURCES

```[Source code](https://android.googlesource.com/platform/frameworks/base/+/refs/heads/main/tools/aapt)```

```[Documentation](https://developer.android.com/tools/aapt2)```

<!-- verified: 2026-06-10 -->
