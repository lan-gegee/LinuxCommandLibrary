# TAGLINE

对 Android 应用进行逆向工程和分析

# TLDR

**分析** APK 文件

```androguard analyze [app.apk]```

**反编译**为 Java 源码

```androguard decompile -o [output_dir] [app.apk]```

显示 APK 的 **manifest 权限**

```androguard axml [app.apk] | grep permission```

将 DEX **反汇编**为 smali

```androguard disassemble [app.apk]```

检查**签名**问题

```androguard sign [app.apk]```

# SYNOPSIS

**androguard** _command_ [_options_] _apk_file_

# DESCRIPTION

**androguard** 是一款 Python 工具，用于 Android 应用的逆向工程、恶意软件分析和安全评估。它可以分析 APK 文件、反编译 DEX 代码、解析 Android manifest，并提取权限和组件信息。

该工具既提供命令行实用程序，也提供用于编程分析的 Python API，因此对手动审查和自动化安全扫描都很有用。

# PARAMETERS

**analyze**
> 打开 IPython Shell，以交互方式开始逆向工程

**decompile**
> 将 APK 反编译为 Java 源码并创建控制流图

**disassemble**
> 反汇编 Dalvik（DEX）字节码

**axml**
> 解析并显示 AndroidManifest.xml 或其他 AXML 文件

**arsc**
> 解码 resources.arsc

**apkid**
> 打印 APK 的软件包名称、版本号和版本名称

**sign**
> 打印 APK 内所有证书的指纹

**cg**
> 生成调用图并将其导出为图形格式

**-o** _dir_
> 输出目录（decompile 必需）

**-i** _file_
> 输入 APK（旧式用法；通常 APK 直接作为位置参数给出）

**-f** _format_
> 控制流图格式（png、jpg、raw）

**-d** _name_
> 要使用的反编译器（默认：DAD）

**-l** _regex_
> 将处理范围限制在匹配正则表达式的方法

# CAVEATS

反编译结果并不总是完美；经过混淆的代码可能难以阅读。某些原生代码无法分析。分析大型 APK 可能占用大量内存。

# HISTORY

**androguard** 由 Anthony Desnos 自 **2012** 年前后开始开发。它已成为 Android 应用安全分析领域最主要的开源工具之一。

# INSTALL

```aur: yay -S androguard```

```nix: nix profile install nixpkgs#androguard```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apktool](/man/apktool)(1), [jadx](/man/jadx)(1), [dex2jar](/man/dex2jar)(1)

# RESOURCES

```[Source code](https://github.com/androguard/androguard)```

```[Documentation](https://androguard.readthedocs.io)```

<!-- verified: 2026-06-11 -->
