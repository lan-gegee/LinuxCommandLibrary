# TAGLINE

将 Android DEX 字节码反编译为 Java 源代码

# TLDR

**反编译 APK**

```jadx [app.apk]```

**反编译到指定目录**

```jadx -d [output_dir] [app.apk]```

**打开 GUI**

```jadx-gui [app.apk]```

**反编译 DEX 文件**

```jadx [classes.dex]```

**显示反编译问题信息**

```jadx --show-bad-code [app.apk]```

**导出为 Gradle 项目**

```jadx -e [output_dir] [app.apk]```

# SYNOPSIS

**jadx** [_options_] _file_

# PARAMETERS

_FILE_
> 要反编译的 APK、DEX 或 AAR 文件。

**-d** _DIR_
> 输出目录。

**-e** _DIR_
> 导出为 Gradle 项目。

**--show-bad-code**
> 在输出中显示反编译出错的部分。

**-r**, **--no-res**
> 跳过资源反编译。

**-j** _N_
> 线程数。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jadx** 将 Android DEX 字节码反编译为 Java 源代码。它可以直接处理 APK 文件，包括资源文件。

该工具同时提供 CLI 和 GUI 两种界面。它能从编译后的 Android 应用生成可读性较好的 Java 代码。

# CAVEATS

反编译并不完美。经过混淆的代码更难处理。需注意法律方面的问题。

# HISTORY

jadx 的创建目的是改进旧款 Android 反编译器，专注于生成更干净、更易读的 Java 输出。

# INSTALL

```pacman: sudo pacman -S jadx```

```brew: brew install jadx```

```nix: nix profile install nixpkgs#jadx```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apktool](/man/apktool)(1), [dex2jar](/man/dex2jar)(1)
