# TAGLINE

实时观察 Java 方法的参数、返回值和异常。

# TLDR

**观察**方法返回值

```watch [com.example.MyClass] [myMethod] returnObj```

观察**参数与返回值**

```watch [com.example.MyClass] [myMethod] '{params, returnObj}'```

带**条件**观察

```watch [com.example.MyClass] [myMethod] returnObj 'returnObj != null'```

观察**异常**

```watch [com.example.MyClass] [myMethod] '{params, throwExp}' -e```

以**更大的对象展开深度**观察

```watch [com.example.MyClass] [myMethod] '{params, returnObj}' -x 3```

# SYNOPSIS

**watch** [_-n count_] [_-x depth_] [_-b_|_-e_|_-s_|_-f_] _class-pattern_ _method-pattern_ _express_ [_condition-express_]

# DESCRIPTION

**watch** 是一个 Arthas 命令，用于实时观察方法的参数、返回值和异常。它使用 OGNL 表达式从方法调用中提取并显示特定的数据。

无需停止应用或添加日志代码，即可排查生产环境的问题。

# PARAMETERS

**class-pattern**
> 类名（支持通配符）

**method-pattern**
> 方法名（支持通配符）

**express**
> 指定观察内容的 OGNL 表达式

**-b**
> 在方法执行前观察

**-e**
> 在抛出异常时观察

**-s**
> 在成功返回时观察

**-f**
> 在方法结束时观察（包括成功返回和抛出异常）

**-n** _count_
> 执行 count 次调用后停止

**-x** _depth_
> 对象展开深度（默认：1，最大：4）

**-M** _size_
> 输出的大小上限

**condition-express**
> 过滤条件（OGNL）

# VARIABLES

- **params**：方法参数数组
- **returnObj**：返回值
- **throwExp**：抛出的异常
- **target**：对象实例

# CAVEATS

OGNL 表达式可能很复杂，请仔细测试。观察热点方法可能影响性能。

# INSTALL

```aur: yay -S arthas```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[arthas](/man/arthas)(1), [arthas-trace](/man/arthas-trace)(1)
