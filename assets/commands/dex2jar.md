# TAGLINE

Android DEX 转 JAR 文件转换器

# TLDR

**将 DEX 转换为 JAR**

```d2j-dex2jar [classes.dex]```

**将 APK 转换为 JAR**

```d2j-dex2jar [app.apk]```

**指定输出文件**

```d2j-dex2jar -o [output.jar] [classes.dex]```

**强制覆盖**

```d2j-dex2jar -f [classes.dex]```

**将 JAR 转换为 DEX**

```d2j-jar2dex [file.jar]```

# SYNOPSIS

**d2j-dex2jar** [_options_] _dex-file_

# DESCRIPTION

**dex2jar** 将 Android DEX（Dalvik 可执行文件）转换为 Java JAR 文件。这样就能用标准 Java 反编译器分析 Android 应用。

该工具常用于 Android 逆向工程、安全分析和应用行为研究。它负责处理 Dalvik 字节码与 JVM 字节码之间的差异。

# PARAMETERS

**-o** _file_
> 输出 JAR 文件名。

**-f**, **--force**
> 覆盖已有的输出文件。

**-e** _file_
> 将异常详情输出到文件。

**-n**, **--not-handle-exception**
> 不处理异常。

**-nc**, **--no-code**
> 不转换代码。

**-d**, **--debug-info**
> 包含调试信息。

**-r**, **--reuse-reg**
> 复用寄存器。

# RELATED TOOLS

**d2j-jar2dex**: 将 JAR 转换为 DEX
**d2j-apk-sign**: 为 APK 文件签名
**d2j-asm-verify**: 校验 ASM 代码
**d2j-dex-recompute-checksum**: 修复 DEX 校验和

# CAVEATS

转换结果可能并不完美。经过混淆的代码依然是混淆状态。部分 Dalvik 特性在 JVM 中没有对应实现。逆向工程可能受法律限制约束。

# HISTORY

**dex2jar** 由 **Bob Pan** (pxb1988) 为 Android 逆向工程而创建。它已成为 Android 安全研究社区的标配工具，经常与 jd-gui 配合使用，对生成的 JAR 文件进行反编译。

# INSTALL

```brew: brew install dex2jar```

```nix: nix profile install nixpkgs#dex2jar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apktool](/man/apktool)(1), [jadx](/man/jadx)(1)
