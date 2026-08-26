# TAGLINE

Android DEX 文件反汇编器

# TLDR

**反汇编** DEX 文件

```baksmali disassemble [classes.dex]```

反汇编到**指定目录**

```baksmali disassemble -o [output/] [classes.dex]```

**指定**反汇编使用的 API 级别

```baksmali disassemble -a [28] [classes.dex]```

**列出**可用子命令

```baksmali --help```

不反汇编直接**列出 DEX 类**

```baksmali list classes [classes.dex]```

带代码偏移注释进行**反汇编**

```baksmali disassemble --code-offsets [classes.dex]```

# SYNOPSIS

**baksmali** _command_ [_options_] _dex-file_

# DESCRIPTION

**baksmali** 是 Android DEX（Dalvik 可执行文件）的反汇编器。它将 DEX 字节码转换为 smali 汇编语言，可用于分析、修改和逆向工程 Android 应用。

该工具是 smali 的对应工具，二者共同构成一套完整的 Android 汇编/反汇编套件。自 2.0 版本起，baksmali 采用基于子命令的接口。

# PARAMETERS

**disassemble**（或 **d**）
> 将 DEX 文件反汇编为 smali 文件。

**list** _type_
> 列出 DEX 文件中的条目（类、方法、字段等）。

**deodex**（或 **x**）
> 对 odex/oat 文件进行 deodex 处理。

**-o**, **--output** _dir_
> 输出目录（默认：out/）。

**-a**, **--api-level** _level_
> 反汇编使用的 API 级别。

**-j**, **--jobs** _num_
> 并行处理的线程数。

**-b**, **--bootclasspath** _classpath_
> 用于分析的引导类路径 jar，冒号分隔。

**-d**, **--bootclasspath-dir** _dir_
> 包含框架文件的目录。

**--debug-info**, **--di**
> 在输出中包含调试元数据（默认：true）。

**--use-locals**
> 使用 .locals 指令而不是 .registers。

**--code-offsets**, **--off**
> 在每条指令前添加其代码偏移的注释。

**--accessor-comments**, **--ac**
> 为合成访问器生成辅助注释（默认：true）。

**--sequential-labels**, **--sl**
> 标签使用顺序编号。

**--classes** _LIST_
> 要反汇编的类列表，逗号分隔。

# FEATURES

- DEX 到 smali 的转换
- Multi-DEX 支持
- API 级别感知
- 并行处理
- 保留调试信息
- 局部变量名

# WORKFLOW

```bash
# Disassemble DEX
baksmali disassemble classes.dex

# Reassemble with smali
smali assemble out/ -o new-classes.dex
```

# CAVEATS

需要 Java 运行时。混淆后的代码会产生难以阅读的输出。API 级别会影响指令解释。仅供研究和学习用途。请尊重软件许可证和服务条款。

# HISTORY

**baksmali**（冰岛语意为"反汇编器"）由 Ben Gruver (JesusFreke) 于 **2010** 年前后创建，是面向 Android 逆向工程的 smali 项目的一部分。

# SEE ALSO

[apktool](/man/apktool)(1), [dex2jar](/man/dex2jar)(1), [jadx](/man/jadx)(1)
