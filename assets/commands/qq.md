# TAGLINE

由 jq 语法驱动的多格式转换和查询工具

# TLDR

**将 YAML 转换为 JSON**

```qq '.' [config.yaml] -o json```

**查询 TOML 文件**

```qq '.database.host' [config.toml]```

**将 CSV 转换为 Parquet**

```qq '.' [data.csv] -o parquet```

**交互式查询模式**

```qq . [file.json] --interactive```

# SYNOPSIS

**qq** [_filter_] [_file_] [_options_]

# PARAMETERS

**-i**, **--input** _FORMAT_
> 显式指定输入格式（如 json、yaml、toml、csv、xml）。

**-o**, **--output** _FORMAT_
> 指定输出格式。

**--interactive**
> 带自动补全和实时预览的交互式查询构建器。

**--stream**
> 流式模式，可高效处理大文件且节省内存（与 jq 相同）。

**-s**, **--slurp**
> slurp 模式：将多个输入读入一个数组。

**-e**
> 退出状态模式：以最后一个值作为退出码。

**--monochrome-output**
> 禁用彩色输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**qq** 是一款由 jq 语法驱动、基于 gojq 引擎的多格式转换和查询工具。它支持读写 JSON、YAML、TOML、XML、HCL/Terraform、CSV、TSV、INI、Parquet、MessagePack、CBOR、Avro 等多种格式。格式会根据文件扩展名自动检测。

# HISTORY

**qq** 由 **JFryy** 创建，使用 **Go** 编写。

# INSTALL

```nix: nix profile install nixpkgs#qq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [yq](/man/yq)(1), [oq](/man/oq)(1), [gron](/man/gron)(1)
