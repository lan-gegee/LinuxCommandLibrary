# TAGLINE

从 XML 文档生成 Go 结构体

# TLDR

**从 XML 文件生成 Go 结构体**

```zek [file.xml]```

**从标准输入的 XML 生成结构体**

```cat [file.xml] | zek```

**用自定义结构体名称生成**

```zek -n [StructName] [file.xml]```

**使用紧凑输出格式**

```zek -c [file.xml]```

**从 URL 读取**

```zek [https://example.com/feed.xml]```

# SYNOPSIS

**zek** [_options_] [_file_|_url_]

# PARAMETERS

**-c**
> 紧凑输出（最小化 struct 标签）

**-e**
> 为结构体添加 XMLName 字段

**-n** _name_
> 使用指定的结构体名称（默认：从根元素派生）

**-p**
> 添加 xml.Name XMLName 字段以便精确序列化

**-t**
> 在输出中包含类型注释

**-x**
> 只输出结构体本身，不含包声明

**-max-examples** _n_
> 注释中最多显示的示例数量

**-version**
> 输出版本并退出

# DESCRIPTION

**zek** 从 XML 文档生成 Go 结构体定义。它分析 XML 结构并生成可对该 XML 格式进行反序列化（及序列化）的类型安全的 Go 代码。

给定一个 XML 文件，zek 会推断其结构，并生成带有恰当 xml struct 标签的合适 Go 类型。它能处理嵌套元素、属性、重复元素（切片）和混合内容。

这对于快速创建用于消费 XML API、解析 XML 数据文件或处理 RSS、Atom、SOAP 等基于 XML 的格式的 Go 类型非常有用。

zek 通过采样来推断类型，因此提供涵盖所有可能字段的代表性 XML 会得到最佳结果。

# CAVEATS

类型推断是启发式的。样本 XML 中未出现的很少使用的可选字段可能会被遗漏。

带有多态元素或命名空间的复杂 XML schema 可能需要手动调整生成的结构体。

对于非常大的 XML 文件，zek 会将整个文档读入内存进行分析。

生成的代码在生产使用前应经过审查和调整，尤其是空值处理和校验方面。

# SEE ALSO

[xmllint](/man/xmllint)(1), [xq](/man/xq)(1), [xmlstarlet](/man/xmlstarlet)(1)
