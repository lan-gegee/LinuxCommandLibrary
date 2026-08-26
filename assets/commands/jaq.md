# TAGLINE

专注于正确性和速度的快速 jq 克隆

# TLDR

从 stdin **过滤 JSON**

```echo '{"name": "world"}' | jaq '.name'```

**处理 JSON 文件**

```jaq '.[0]' [path/to/file.json]```

**过滤并格式化输出**

```jaq -r '.[] | .name' [path/to/file.json]```

**读取 YAML 输入**

```jaq --from yaml '.' [path/to/file.yaml]```

**将 JSON 转换为 YAML**

```jaq --to yaml '.' [path/to/file.json]```

# SYNOPSIS

**jaq** [**-r**] [**--from** _format_] [**--to** _format_] _filter_ [_file_...]

# PARAMETERS

**-r**, **--raw-output**
> 打印字符串时不加 JSON 引号。

**-R**, **--raw-input**
> 将输入按原始字符串读取，每行一个。

**-s**, **--slurp**
> 将所有输入值收集到单个数组中。

**-c**, **--compact-output**
> 以单行形式输出 JSON。

**-S**, **--sort-keys**
> 对输出中的对象键排序。

**--indent** _N_
> 每级缩进使用 _N_ 个空格（默认 **2**）。

**--tab**
> 每级缩进使用一个制表符。

**-C**, **--color-output**
> 即使 stdout 不是 TTY 也强制使用彩色输出。

**-M**, **--monochrome-output**
> 禁用彩色输出。

**-i**, **--in-place**
> 用过滤器的结果重写每个输入文件。

**--from** _FORMAT_
> 输入格式：**json**、**yaml**、**cbor**、**toml**、**xml**、**csv**、**tsv**、**raw**、**raw0**、**xjon**。

**--to** _FORMAT_
> 输出格式（与 **--from** 相同的一组）。

**-n**, **--null-input**
> 使用 **null** 作为输入值。

# DESCRIPTION

**jaq** 是 JSON 处理工具 **jq** 的克隆，专注于正确性、速度和简洁性。它既可以作为命令行程序使用（几乎可以直接替换 jq），也可以作为 Rust 库使用。除了标准 JSON 之外，jaq 还支持 **YAML**、**CBOR**、**TOML** 和 **XML** 格式。

jaq 的目标是在边缘情况下提供比 jq 更正确、更可预期的行为，同时对常见用法保持兼容。其核心已由 **Radically Open Security** 完成安全审计。

# CAVEATS

虽然与 jq 高度兼容，但部分边缘行为为了正确性而有意不同。并非所有 jq 内置函数都已实现。不支持自定义 jq 模块。

# HISTORY

**jaq** 由 **Michael Färber**（01mf02）创建，采用 **Rust** 编写。其开发动机是对 jq 启动时间和边缘情况正确性的担忧；基准测试显示它在大多数操作上比 jq 更快。

# INSTALL

```pacman: sudo pacman -S jaq```

```zypper: sudo zypper install jaq```

```brew: brew install jaq```

```nix: nix profile install nixpkgs#jaq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [yq](/man/yq)(1)
