# TAGLINE

支持 50 多种字符串变换的跨平台 CLI

# TLDR

**生成字符串的 MD5 哈希**

```sttr md5 "[Hello World]"```

**对管道输入进行 Base64 编码**

```echo "Hello" | sttr base64-encode```

**将 YAML 文件转换为 JSON**

```sttr yaml-json [file.yaml]```

# SYNOPSIS

**sttr** _operation_ [_input_]

# DESCRIPTION

**sttr** 是一个跨平台命令行应用，用于对字符串执行各种变换操作。它支持编码/解码（base64、URL）、哈希（MD5、SHA）、大小写转换、JSON/YAML 转换等多种功能。它同时提供交互式 TUI 模式和可脚本化的 CLI 接口。

# HISTORY

**sttr** 由 **abhimanyu003** 创建，使用 **Go** 编写。

# INSTALL

```brew: brew install sttr```

```nix: nix profile install nixpkgs#sttr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [base64](/man/base64)(1), [openssl](/man/openssl)(1)
