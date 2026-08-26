# TAGLINE

Android DEX 文件操作与分析工具

# TLDR

**打印 DEX 文件的统计信息**

```dexter -s [classes.dex]```

**列出 DEX 文件中定义的类**

```dexter -l [classes.dex]```

**反汇编**方法体

```dexter -d [classes.dex]```

**将单个类提取**到新的 DEX 文件

```dexter -e [com.example.MyClass] -o [out.dex] [classes.dex]```

**生成控制流图**

```dexter --cfg [compact] [classes.dex]```

# SYNOPSIS

**dexter** [_flags_...] [**-e** _classname_] [**-o** _outfile_] _dexfile_

# PARAMETERS

**-s**
> 打印 DEX 各部分的统计信息。

**-l**
> 列出 DEX 文件中定义的类。

**-d**
> 反汇编方法体。

**-e** _classname_
> 提取单个类。

**-o** _file_
> 输出新的 .dex 文件。

**-m**
> 打印 .dex 布局映射。

**-v**
> 详细输出。

**--cfg** _compact_|_verbose_
> 生成控制流图。

**-h**
> 显示帮助。

# DESCRIPTION

**dexter** 是 Android 开源项目（tools/dexter）中的 DEX（Dalvik 可执行文件）操作工具。它构建于 dexter/slicer 库之上，可以检查、反汇编和重写 DEX 文件。

除了只读分析（统计、类列表、反汇编、布局映射）之外，dexter 还能生成修改后的 .dex 文件，例如提取单个类。其控制流图输出有助于研究编译后的 Android 代码的方法级结构。

底层的 slicer 库也被 Android 工具链用于字节码插桩。

# CAVEATS

dexter 处理的是 .dex 文件而非 APK；请先用 unzip 等工具从 APK 中取出 classes.dex。它需要从 AOSP 源码树构建，Linux 发行版通常不提供软件包。

# INSTALL

```brew: brew install dexter```

```nix: nix profile install nixpkgs#dexter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dexdump](/man/dexdump)(1), [apktool](/man/apktool)(1)

# RESOURCES

```[Source code](https://android.googlesource.com/platform/tools/dexter/)```

<!-- verified: 2026-07-11 -->
