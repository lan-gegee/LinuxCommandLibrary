# TAGLINE

移除不确定性数据，助力可复现构建

# TLDR

**清理文件**

```strip-nondeterminism [file]```

**指定类型清理**

```strip-nondeterminism --type [zip] [file.zip]```

**设置时间戳**

```strip-nondeterminism --timestamp [1234567890] [file]```

**详细输出**

```strip-nondeterminism -v [file]```

**演练运行**

```strip-nondeterminism -n [file]```

# SYNOPSIS

**strip-nondeterminism** [_--type type_] [_--timestamp ts_] [_options_] _files_

# PARAMETERS

**-t**, **--type** _TYPE_
> 强制将输入视为特定文件格式（例如 _zip_、_jar_、_png_、_gzip_、_ar_、_javadoc_），而不是由文件名后缀决定。

**-T**, **--timestamp** _TS_
> 用给定的 Unix epoch 值替换内嵌的时间戳。若未设置，**strip-nondeterminism** 会回退使用 **SOURCE_DATE_EPOCH** 环境变量。

**-v**, **--verbose**
> 打印每处修改。

**-n**, **--dry-run**
> 显示将要进行的更改，但不写入磁盘。

**--help**
> 显示帮助。

# DESCRIPTION

**strip-nondeterminism** 移除文件中不确定性的来源，以实现可复现构建。构建产物通常包含内嵌时间戳、用户 ID、文件顺序差异以及其他元数据，即使源代码完全相同，不同构建之间这些内容也可能不同。该工具会规范化这些元素，使相同源代码的构建总是产生逐位一致的输出。

该工具支持多种文件格式，包括 ZIP 归档、JAR 文件、PNG 图像、gzip 文件和 ar 归档。针对每种格式，它会识别并剥离或规范化引入不确定性的特定元数据字段，例如归档条目中的修改时间戳或 PNG 头中的创建日期。

它是 Debian 可复现构建基础设施的一部分，常作为后处理步骤集成到构建系统中。可以提供固定的时间戳来替换可变的时间戳，通常取自 SOURCE_DATE_EPOCH 环境变量。

# CAVEATS

依赖具体格式。可能需要类型提示。属于 Debian 可复现构建项目的一部分。

# HISTORY

**strip-nondeterminism** 为 **Reproducible Builds** 项目而创建，旨在使构建输出具有确定性。

# INSTALL

```pacman: sudo pacman -S strip-nondeterminism```

```apk: sudo apk add strip-nondeterminism```

```zypper: sudo zypper install strip-nondeterminism```

```brew: brew install strip-nondeterminism```

```nix: nix profile install nixpkgs#strip-nondeterminism```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[touch](/man/touch)(1), [zip](/man/zip)(1), [ar](/man/ar)(1), [diffoscope](/man/diffoscope)(1)
