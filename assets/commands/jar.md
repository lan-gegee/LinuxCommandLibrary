# TAGLINE

Java 归档工具

# TLDR

**创建 JAR 文件**

```jar cf [output.jar] [files...]```

**创建带 manifest 的 JAR**

```jar cfm [output.jar] [MANIFEST.MF] [files...]```

**解压 JAR 文件**

```jar xf [archive.jar]```

**列出内容**

```jar tf [archive.jar]```

**创建可执行 JAR**

```jar cfe [output.jar] [MainClass] [files...]```

**更新 JAR 文件**

```jar uf [archive.jar] [newfiles...]```

**提取指定文件**

```jar xf [archive.jar] [path/to/file]```

**详细列出内容**

```jar tvf [archive.jar]```

使用 -C 切换基目录后**从目录创建 JAR**

```jar cf [output.jar] -C [build/classes] .```

# SYNOPSIS

**jar** [_options_] [_manifest_] _destination_ _input-files_

# PARAMETERS

**c**
> 创建新归档。

**x**
> 解压归档。

**t**
> 列出内容表。

**u**
> 更新现有归档。

**f** _file_
> 指定归档文件名。

**m** _manifest_
> 包含 manifest 文件。

**e** _class_
> 设置入口点（主类）。

**v**
> 详细输出。

**0**
> 仅存储（不压缩）。

**M**
> 不创建 manifest 文件。

**i**
> 为指定的 JAR 文件生成索引信息。

**C** _dir_
> 在包含后续文件之前先切换到指定目录。

**--release** _VERSION_
> （Java 9+）将后续文件放入带版本号的目录，用于 multi-release JAR。

# DESCRIPTION

**jar** 是 Java 归档工具。它将 Java 类文件、资源和元数据打包成单个 JAR 文件，用于分发和部署。

JAR 文件采用 ZIP 格式，并带有包含元数据的 manifest（META-INF/MANIFEST.MF）。可执行 JAR 会在 manifest 中指定主类。

# MANIFEST EXAMPLE

```
Manifest-Version: 1.0
Main-Class: com.example.Main
Class-Path: lib/dependency.jar
```

# CAVEATS

使用旧式（不带连字符）语法时，标志的顺序很重要。manifest 文件必须以换行符结尾。除非使用 -C，否则路径都相对于当前目录。在 Java 9+ 中，`--module-version` 和 `--release` 标志增加了模块/multi-release 支持。

# HISTORY

jar 工具自 Java 1.1（1997 年）起就是 **JDK** 的一部分。它是 Java 部署的关键工具，后来演进为支持 Java 9+ 的模块和 multi-release JAR。

# SEE ALSO

[java](/man/java)(1), [javac](/man/javac)(1), [jarsigner](/man/jarsigner)(1), [zip](/man/zip)(1), [unzip](/man/unzip)(1), [tar](/man/tar)(1)
