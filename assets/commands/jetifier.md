# TAGLINE

将 Android 库从 Support Library 迁移到 AndroidX

# TLDR

**将 AAR 转换为 AndroidX**

```jetifier-standalone -i [lib.aar] -o [lib-androidx.aar]```

**转换 JAR**

```jetifier-standalone -i [lib.jar] -o [lib-androidx.jar]```

**反向转换**

```jetifier-standalone -r -i [lib-androidx.aar] -o [lib.aar]```

**列出映射关系**

```jetifier-standalone -l```

**详细模式**

```jetifier-standalone -v -i [input] -o [output]```

# SYNOPSIS

**jetifier-standalone** [_options_] **-i** _input_ **-o** _output_

# PARAMETERS

**-i** _FILE_
> 输入的 AAR/JAR 文件。

**-o** _FILE_
> 输出文件。

**-r**, **--reversed**
> 反向转换（AndroidX 转 Support Library）。

**-l**
> 列出类映射。

**-c** _FILE_
> 自定义映射配置文件。

**-v**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jetifier** 将 Android 库从 Support Library 迁移到 AndroidX。它会重写字节码和资源以使用新的包名。

该工具让旧库可以在 AndroidX 项目中使用。它会自动处理 AAR 和 JAR 文件。

# CAVEATS

是 Android SDK 的一部分。优先选择正向迁移（Support 转 AndroidX）。部分库可能不完全兼容。由于大多数库已原生迁移到 AndroidX，Jetifier 已被视为遗留工具。

# HISTORY

jetifier 由 **Google** 创建，用于协助 2018 年推出的 Android Support Library 向 AndroidX 的迁移。

# SEE ALSO

[gradle](/man/gradle)(1)
