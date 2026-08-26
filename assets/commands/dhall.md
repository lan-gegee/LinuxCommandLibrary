# TAGLINE

保证终止的可编程配置语言

# TLDR

**求值一个 Dhall 表达式**

```dhall <<< "[expression]"```

**求值一个 Dhall 文件**

```dhall < [config.dhall]```

**将 Dhall 转换为 JSON**

```dhall-to-json <<< "[expression]"```

**将 Dhall 转换为 YAML**

```dhall-to-yaml < [config.dhall]```

**对一个 Dhall 文件做类型检查**

```dhall type < [config.dhall]```

**格式化一个 Dhall 文件**

```dhall format < [config.dhall]```

**将 JSON 转换为 Dhall**

```json-to-dhall '[Type]' < [data.json]```

# SYNOPSIS

**dhall** [_command_] [_options_]

# PARAMETERS

**type**
> 推断并显示表达式的类型。

**normalize**
> 规范化一个表达式。

**format**
> 格式化 Dhall 源码。

**lint**
> 改进 Dhall 表达式。

**diff**
> 显示两个表达式之间的差异。

**hash**
> 计算表达式的语义哈希。

**freeze**
> 为导入添加完整性校验。

**encode** / **decode**
> 二进制编码/解码。

**--explain**
> 提供详细的错误解释。

**--ascii**
> 使用 ASCII 输出而不是 Unicode。

# DESCRIPTION

**Dhall** 是一种保证终止的可编程配置语言。它提供编程语言的表达力（函数、类型、导入），同时确保配置总能产出结果，不会陷入无限循环。

Dhall 表达式可以转换为 JSON、YAML 或其他格式，供应用程序使用。该语言具有强大的类型系统，能在求值阶段捕获配置错误。

关键特性包括：带完整性校验的远程导入（内容寻址的依赖）、全量类型系统（没有运行时错误），以及用于常见转换的内置函数。

# EXAMPLE

```dhall
-- config.dhall
let Config = { name : Text, port : Natural }

let defaults = { name = "myapp", port = 8080 }

in  defaults // { port = 9000 }
```

# CAVEATS

对不熟悉带类型函数式编程的人有一定学习曲线。大型配置求值可能较慢。并非所有工具都原生支持 Dhall；转换成 JSON/YAML 会增加一个构建步骤。导入缓存的行为可能让用户感到意外。

# HISTORY

Dhall 由 **Gabriella Gonzalez** 创建，首次发布于 **2016 年**。名字来源于一种印度谷物。它的设计目的是解决 YAML 和 JSON 在复杂配置上的局限，同时避免图灵完备带来的不可预测性——那正是其他模板语言的问题所在。该语言已在 Kubernetes 配置和基础设施即代码领域获得采用。

# INSTALL

```apt: sudo apt install dhall```

```dnf: sudo dnf install dhall```

```pacman: sudo pacman -S dhall```

```brew: brew install dhall```

```nix: nix profile install nixpkgs#dhall```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [yq](/man/yq)(1), [jsonnet](/man/jsonnet)(1)

# RESOURCES

```[Source code](https://github.com/dhall-lang/dhall-lang)```

```[Homepage](https://dhall-lang.org)```

```[Documentation](https://docs.dhall-lang.org)```

<!-- verified: 2026-07-11 -->
