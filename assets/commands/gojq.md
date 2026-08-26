# TAGLINE

jq JSON 处理器的纯 Go 实现

# TLDR

**美化打印 JSON**

```cat [file.json] | gojq .```

**提取一个字段**

```cat [file.json] | gojq '.[field]'```

**过滤数组元素**

```cat [file.json] | gojq '.[] | select(.active == true)'```

**映射与变换**

```cat [file.json] | gojq '[.[] | {name: .title, id: .uuid}]'```

**直接从文件读取**

```gojq '.users[]' [file.json]```

**处理 YAML 输入**

```gojq --yaml-input '.spec.containers[]' [deployment.yaml]```

**以 YAML 格式输出**

```gojq --yaml-output '.data' [file.json]```

**使用变量**

```gojq --arg name "[value]" '.items[] | select(.name == $name)' [file.json]```

# SYNOPSIS

**gojq** [_options_] _filter_ [_file_...]

# PARAMETERS

**-r**, **--raw-output**
> 输出字符串时不带 JSON 引号。

**-c**, **--compact-output**
> 紧凑输出而不是美化打印。

**-n**, **--null-input**
> 不读取输入；配合 --argjson 使用很有用。

**-e**, **--exit-status**
> 根据输出内容设置退出码。

**-s**, **--slurp**
> 把所有输入读入一个数组。

**-S**, **--sort-keys**
> 对输出中的对象键进行排序。

**-C**, **--color-output**
> 强制彩色输出。

**-M**, **--monochrome-output**
> 禁用彩色输出。

**--tab**
> 使用制表符缩进。

**--indent** _n_
> 设置缩进级别。

**--yaml-input**
> 将输入解析为 YAML。

**--yaml-output**
> 以 YAML 而非 JSON 输出。

**--arg** _name_ _value_
> 将变量设置为字符串值。

**--argjson** _name_ _json_
> 将变量设置为 JSON 值。

**--slurpfile** _name_ _file_
> 将变量设置为以数组形式表示的文件内容。

**--rawfile** _name_ _file_
> 将变量设置为文件的原始内容。

**-f**, **--from-file** _file_
> 从文件读取过滤器。

**-L** _path_
> 将目录加入模块搜索路径。

# DESCRIPTION

**gojq** 是 JSON 处理器 jq 的纯 Go 实现。它提供同样的查询语言来过滤、变换和提取 JSON 数据，并额外原生支持 YAML。

过滤器语言用 **|** 表示管道、**.** 表示字段访问、**[]** 表示迭代、**select()** 表示过滤。复杂的变换可以将它们与对象构造、数组切片及内置函数组合使用。

得益于 YAML 输入/输出，gojq 在 Kubernetes 以及其他大量使用 YAML 的工作流中格外有用。借助 **--arg** 设置变量可以构造参数化查询，便于脚本化使用。

# CAVEATS

部分高级 jq 特性存在细微的行为差异。处理超大文件时的性能可能与 C 语言版 jq 有所不同。模块路径的搜索方式与 jq 不同。SQL 风格的运算符尚未实现。

# HISTORY

gojq 由 **itchyny** 创建，大约于 **2019 年**首次发布。其开发目标是提供一个无 C 依赖、单二进制的 jq 替代品。YAML 支持是后来加入的特色功能。该项目与 jq 保持高度兼容，同时也可作为库，供需要 JSON 变换能力的 Go 应用使用。

# INSTALL

```apt: sudo apt install gojq```

```dnf: sudo dnf install gojq```

```apk: sudo apk add gojq```

```zypper: sudo zypper install gojq```

```brew: brew install gojq```

```nix: nix profile install nixpkgs#gojq```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [yq](/man/yq)(1), [jless](/man/jless)(1), [fx](/man/fx)(1)

# RESOURCES

```[Source code](https://github.com/itchyny/gojq)```

<!-- verified: 2026-07-17 -->
