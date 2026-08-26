# TAGLINE

面向开发的测试数据生成器

# TLDR

**列出可用的生成器**

```fakedata --generators```

生成假姓名

```fakedata name```

组合多个生成器（各占一列）

```fakedata name email```

**生成指定数量的行**

```fakedata -l [10] name email```

以 CSV 格式输出

```fakedata -f csv name email```

以 SQL INSERT 语句输出

```fakedata -f sql name email```

从自定义模板生成（生成器名首字母大写）

```echo "{{Name}},{{Email}}" | fakedata```

# SYNOPSIS

**fakedata** [_options_] _generator_...

# PARAMETERS

**-l**, **--limit** _count_
> 要生成的行数（默认 10）。

**-f**, **--format** _format_
> 输出格式：csv、tab 或 sql。

**--generators**
> 列出所有可用的生成器后退出。

# DESCRIPTION

**fakedata** 为测试和开发生成假数据。它提供大量数据生成器，可创建逼真但合成的信息，包括姓名、邮箱、地址、电话号码、日期、数字和自定义格式字符串。

该工具专为填充测试数据库、创建样例数据集而设计，适用于需要真实感数据但不希望使用真实用户信息的开发场景。它支持多种输出格式，包括 CSV、JSON 和制表符分隔值。

一次调用可以组合多个生成器；seed 选项支持可复现的数据生成，便于保持测试场景一致。

# SEE ALSO

[faker](/man/faker)(1)

# RESOURCES

```[Source code](https://github.com/lucapette/fakedata)```

<!-- verified: 2026-07-15 -->
