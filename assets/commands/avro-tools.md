# TAGLINE

处理 Apache Avro 数据文件的工具集

# TLDR

**将 JSON 转换为 Avro**

```avro-tools fromjson --schema-file [schema.avsc] [input.json] > [output.avro]```

**将 Avro 转换为 JSON**

```avro-tools tojson [input.avro] > [output.json]```

**显示 Avro 文件的 schema**

```avro-tools getschema [file.avro]```

**显示文件元数据**

```avro-tools getmeta [file.avro]```

**拼接多个 Avro 文件**

```avro-tools concat [file1.avro] [file2.avro] [output.avro]```

**将 Avro schema 编译为 Java**

```avro-tools compile schema [schema.avsc] [output_directory]```

**根据 schema 生成随机数据**

```avro-tools random --schema-file [schema.avsc] --count [100] [output.avro]```

# SYNOPSIS

**avro-tools** _command_ [_options_] [_arguments_]

# PARAMETERS

**fromjson**
> 将 JSON 转换为 Avro 格式。

**tojson**
> 将 Avro 转换为 JSON 格式。

**getschema**
> 从 Avro 文件中提取并打印 schema。

**getmeta**
> 打印 Avro 文件中的元数据。

**concat**
> 拼接多个具有兼容 schema 的 Avro 文件。

**compile**
> 将 schema 编译为 Java 源文件。

**idl**
> 将 Avro IDL 编译为 schema。

**random**
> 根据 schema 生成随机数据。

**recodec**
> 更改 Avro 文件的编解码器。

**--schema-file** _file_
> Avro schema 文件（.avsc）的路径。

**--count** _n_
> 要生成的记录数（用于 random）。

**--codec** _name_
> 压缩编解码器（null、deflate、snappy、bzip2、zstd、xz）。

# DESCRIPTION

**avro-tools** 是一组用于处理 Apache Avro 数据文件的工具。Avro 是一种数据序列化系统，提供丰富的数据结构、紧凑的二进制格式以及 schema 演进能力。

这些工具支持在 Avro 二进制格式与人类可读的 JSON 之间转换、schema 提取与校验、文件操作以及代码生成。Avro 文件是自描述的，数据旁边就带有自己的 schema，avro-tools 可以提取并显示它。

常见工作流包括：检查数据管道产出的 Avro 文件、为调试在格式之间转换数据、生成测试数据，以及将 schema 编译为特定语言的类以供应用开发使用。

# CAVEATS

JSON 转 Avro 需要 schema 文件；JSON 结构必须与 schema 匹配。大文件可能需要增大 JVM 堆空间（**-Xmx** 选项）。拼接文件时会强制检查 schema 兼容性。该工具以 Java JAR 文件形式分发，需要 JRE。

# HISTORY

Apache Avro 由 **Doug Cutting**（也是 Hadoop 和 Lucene 的创造者）创建，于 **2009** 年首次发布。它的开发是为了解决现有序列化框架在配合 Hadoop 等大数据系统工作时的局限性。Avro 于 **2010** 年成为 Apache 顶级项目，广泛应用于数据工程领域，尤其是 Kafka、Spark 和 Hadoop 生态。

# INSTALL

```aur: yay -S avro-tools```

```brew: brew install avro-tools```

```nix: nix profile install nixpkgs#avro-tools```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[parquet-tools](/man/parquet-tools)(1)
