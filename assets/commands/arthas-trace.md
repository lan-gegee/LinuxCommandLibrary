# TAGLINE

追踪 Java 方法的执行路径和耗时。

# TLDR

**追踪**方法执行

```trace [com.example.MyClass] [myMethod]```

带**条件**追踪

```trace [com.example.MyClass] [myMethod] '#cost > 100'```

追踪类中的**所有方法**

```trace [com.example.MyClass] *```

带**调用次数限制**的追踪

```trace -n [5] [com.example.MyClass] [myMethod]```

使用**正则表达式**匹配类/方法进行追踪

```trace -E [com\.example\.(Foo|Bar)] [myMethod]```

# SYNOPSIS

**trace** [_-n count_] [_-E_] [_--skipJDKMethod value_] _class-pattern_ _method-pattern_ [_condition-express_]

# DESCRIPTION

**trace** 是一个 Arthas 命令，用于追踪方法的执行路径和耗时。它展示一次方法调用内部的调用层级，并突出显示哪些子方法耗时最多。

无需添加日志或性能剖析插桩，就能定位性能瓶颈，这一点极为有用。

# PARAMETERS

**class-pattern**
> 类名（支持通配符）

**method-pattern**
> 方法名（支持通配符）

**-n** _count_
> 执行 count 次调用后停止（默认：100）

**-E**
> 对类名和方法名模式启用正则表达式匹配（默认为通配符匹配）

**--skipJDKMethod** _value_
> 跳过对 JDK 方法的追踪（默认：true）

**--exclude-class-pattern** _pattern_
> 将匹配该模式的类排除在追踪之外

**-m** _count_, **--maxMatch** _count_
> 可被插桩的匹配类的最大数量（默认：50）

**-v**
> 打印条件表达式求值的详细信息

**condition-express**
> OGNL 条件表达式（例如 '#cost > 100' 表示只追踪耗时超过 100ms 的调用）

# OUTPUT

展示调用树，包括：
- 方法名
- 执行时间
- 嵌套调用结构

# CAVEATS

深层追踪可能产生大量输出。性能开销随追踪深度增加。请使用条件表达式来限制输出。

# HISTORY

**trace** 是 Arthas 中的核心诊断命令，是生产环境 Java 应用性能排查的必备工具。

# INSTALL

```aur: yay -S arthas```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[arthas](/man/arthas)(1), [arthas-watch](/man/arthas-watch)(1)

# RESOURCES

```[Source code](https://github.com/alibaba/arthas)```

```[Homepage](https://arthas.aliyun.com)```

```[Documentation](https://arthas.aliyun.com/en/doc/trace.html)```

<!-- verified: 2026-06-16 -->
