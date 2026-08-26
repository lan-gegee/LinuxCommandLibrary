# TAGLINE

有主见的 Scala 代码格式化工具

# TLDR

**格式化文件**

```scalafmt [file.scala]```

**原地格式化**

```scalafmt -i [file.scala]```

**检查格式**

```scalafmt --check [file.scala]```

**格式化目录**

```scalafmt [src/]```

**使用配置文件**

```scalafmt -c [.scalafmt.conf] [file.scala]```

**显示差异**

```scalafmt --diff [file.scala]```

**格式化标准输入**

```cat [file.scala] | scalafmt --stdin```

# SYNOPSIS

**scalafmt** [_-i_] [_--check_] [_-c config_] [_options_] [_files_]

# PARAMETERS

**-i**, **--inplace**
> 原地修改文件。

**--check**
> 仅检查，不做更改。

**-c**, **--config** _FILE_
> 配置文件。

**--diff**
> 显示变更。

**--stdin**
> 从标准输入读取。

**--stdout**
> 写到标准输出。

**--exclude** _PATTERN_
> 排除文件。

**--help**
> 显示帮助。

# DESCRIPTION

**scalafmt** 是一款有主见的 Scala 代码格式化工具，用于在项目间强制统一的代码风格。它依据可配置的规则重新排版源代码，涵盖行长、缩进、对齐和 import 排序，并通过 dialect 配置同时支持 Scala 2 和 Scala 3 语法。

**--check** 模式在不修改文件的情况下验证格式，如果需要做出更改则返回非零退出码，非常适合在 CI 流水线中强制执行。**-i**（in-place）模式在开发过程中直接修改文件。配置通过项目根目录下采用 HOCON 格式的 **.scalafmt.conf** 文件定义。

# CONFIGURATION

**.scalafmt.conf**
> 采用 HOCON 格式的项目级配置文件，定义 maxColumn、dialect、align 设置以及重写规则等格式化规则。

# CAVEATS

可能细微地改变代码结构。配置选项繁多。建议配合编辑器集成使用。

# HISTORY

**scalafmt** 由 **Olafur Pall Geirsson** 为 Scala 格式化而创建。它在 Scala 生态中被广泛用于代码风格强制。

# INSTALL

```nix: nix profile install nixpkgs#scalafmt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scala](/man/scala)(1), [sbt](/man/sbt)(1), [metals](/man/metals)(1)
