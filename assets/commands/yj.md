# TAGLINE

在 YAML、JSON、TOML 和 HCL 之间转换

# TLDR

将 **YAML 文件转换为 JSON**

```cat [file.yaml] | yj```

将 **YAML 文件转换为 TOML**

```cat [file.yaml] | yj -yt```

将 **JSON 文件转换为 YAML**

```cat [file.json] | yj -jy```

将 **TOML 文件转换为 JSON** 并带**缩进输出**

```cat [file.toml] | yj -ti```

将 **HCL 文件转换为 JSON**

```cat [file.hcl] | yj -c```

将 **JSON 文件转换为 TOML** 并带**缩进输出**

```cat [file.json] | yj -jti```

# SYNOPSIS

**yj** [**-**][_ytjcrneikhv_]

# PARAMETERS

**-yj**, **-y**
> 将 YAML 转换为 JSON（默认）

**-yy**
> 将 YAML 转换为 YAML

**-yt**
> 将 YAML 转换为 TOML

**-yc**
> 将 YAML 转换为 HCL

**-jy**, **-r**
> 将 JSON 转换为 YAML

**-jj**
> 将 JSON 转换为 JSON

**-jt**
> 将 JSON 转换为 TOML

**-jc**
> 将 JSON 转换为 HCL

**-tj**, **-t**
> 将 TOML 转换为 JSON

**-ty**
> 将 TOML 转换为 YAML

**-tt**
> 将 TOML 转换为 TOML

**-tc**
> 将 TOML 转换为 HCL

**-cj**, **-c**
> 将 HCL 转换为 JSON

**-cy**
> 将 HCL 转换为 YAML

**-ct**
> 将 HCL 转换为 TOML

**-cc**
> 将 HCL 转换为 HCL

**-n**
> 不在字符串与 inf、-inf 和 NaN 之间转换（仅限 YAML 或 TOML）

**-e**
> 对输出中的 HTML 字符进行转义（仅限 JSON）

**-i**
> 缩进输出（仅限 JSON 或 TOML）

**-k**
> 尝试将键解析为对象或数值类型（仅限 YAML 输出）

**-h**
> 显示帮助

**-v**
> 显示版本

# DESCRIPTION

**yj** 是一款轻量级命令行工具，用于在 **YAML**、**JSON**、**TOML** 和 **HCL** 序列化格式之间转换。它从 **stdin** 读取并向 **stdout** 写入，因此很容易通过管道与其他 Unix 工具组合。

yj 的一个关键特性是转换过程中能**保留映射键的顺序**，这是许多类似工具做不到的。默认行为是将 YAML 转换为 JSON。转换方向由格式字母的组合指定：第一个字母是输入格式，第二个是输出格式（例如 **-yt** 表示从 YAML 到 TOML）。

支持的格式版本包括 YAML v1.2、TOML v1.0.0、JSON RFC 7159 和 HCL v1。

# CAVEATS

仅支持 **HCL v1**。使用 HCL2 语法的现代 Terraform 文件可能无法正确解析。该工具只能从 stdin 读取、向 stdout 写入；没有直接指定输入或输出文件的选项。JSON 和 TOML 输出默认是紧凑格式，需要 **-i** 才能得到便于阅读的缩进输出。

# HISTORY

**yj** 由 **Stephen Levine** 创建，首次发布于 **2017 年 3 月**。它用 **Go** 编写，GitHub 地址为 sclevine/yj。可以通过 Homebrew 安装，也有适用于 Linux、macOS 和 Windows 的预构建二进制文件。采用 Apache License 2.0 许可证。

# INSTALL

```apk: sudo apk add yj```

```brew: brew install yj```

```nix: nix profile install nixpkgs#yj```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [yq](/man/yq)(1), [python](/man/python)(1)
