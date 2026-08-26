# TAGLINE

面向多语言的模式驱动代码生成器

# TLDR

**从规范生成代码**

```dcg [specification.dcg] -o [output_dir]```

**以指定目标语言生成**

```dcg [specification.dcg] --lang [go]```

**使用自定义模板生成**

```dcg [specification.dcg] --template [template_dir]```

**仅校验规范**而不生成代码

```dcg [specification.dcg] --validate```

**列出可用的生成器**

```dcg --list-generators```

# SYNOPSIS

**dcg** [_options_] _specification_

# PARAMETERS

_SPECIFICATION_
> 要处理的输入规范文件。

**-o**, **--output** _DIR_
> 生成代码的输出目录。

**--lang** _LANGUAGE_
> 目标编程语言。

**--template** _DIR_
> 存放自定义模板的目录。

**--validate**
> 仅校验规范。

**--list-generators**
> 显示可用的代码生成器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dcg**（Data Code Generator）是一个代码生成工具，它将数据规范或模式转换为多种编程语言的代码。它可以自动创建数据结构、序列化代码及相关样板代码。

该工具读取描述数据类型及其关系的规范文件，然后应用特定语言的模板生成对应的源代码。这种方式确保了文档与实现之间的一致性。

对于数据模型复杂、需要多种语言实现，或要求在系统边界之间严格遵循模式的项目而言，像 dcg 这样的代码生成器非常有价值。

# CAVEATS

生成的代码在处理边界情况时可能需要手动调整。使用自定义模板需要了解模板引擎。规范中的破坏性变更可能要求重新生成所有依赖代码。

# HISTORY

dcg 代表了一类代码生成工具，它们的出现是为了解决在多语言和多平台之间维护一致数据表示的难题。存在多种采用不同规范格式和目标语言的实现。

# SEE ALSO

[protoc](/man/protoc)(1), [thrift](/man/thrift)(1)
