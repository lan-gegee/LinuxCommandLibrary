# TAGLINE

Android DEX 文件分析与反汇编工具

# TLDR

**转储一个 DEX 文件**

```dexdump [classes.dex]```

**带反汇编地转储**

```dexdump -d [classes.dex]```

**转储文件头**摘要

```dexdump -f [classes.dex]```

仅**转储导出项**

```dexdump -e -d [classes.dex]```

**输出到文件**

```dexdump [classes.dex] -o [output.txt]```

# SYNOPSIS

**dexdump** [_options_] _dexfile_

# PARAMETERS

**-d**
> 反汇编代码段。

**-f**
> 显示文件头的摘要信息。

**-h**
> 显示文件头详情。

**-e**
> 仅显示导出项。

**-a**
> 显示注解（annotation）。

**-c**
> 校验校验和后退出。

**-g**
> 为方法转储 CFG（Graphviz dot 格式）。

**-l** _layout_
> 输出布局：plain、xml。

**-o** _file_
> 输出到文件而不是标准输出。

# DESCRIPTION

**dexdump** 显示 Android DEX（Dalvik 可执行文件）的详细信息。它可以转储类定义、方法签名、字段信息，并将字节码反汇编为人类可读的形式。

该工具是 Android SDK 构建工具的一部分，可用于洞察编译后的 Android 应用的内部结构。它能以纯文本或 XML 格式输出信息，便于进一步处理。

DEX 文件包含面向 Dalvik 虚拟机或 Android Runtime (ART) 的编译后 Java 字节码。dexdump 帮助开发者和安全研究人员了解应用内部结构、调试编译问题以及进行逆向工程分析。

# INSTALL

```apt: sudo apt install dexdump```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apktool](/man/apktool)(1), [jadx](/man/jadx)(1), [dex2jar](/man/dex2jar)(1)

# RESOURCES

```[Source code](https://android.googlesource.com/platform/art/+/refs/heads/main/dexdump/)```

<!-- verified: 2026-07-11 -->
