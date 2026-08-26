# TAGLINE

计算 Java 序列化版本 UID

# TLDR

**获取 serial version UID**

```serialver [ClassName]```

**指定类路径**

```serialver -classpath [path] [ClassName]```

**显示 JAR 中类的 UID**

```serialver -classpath [app.jar] [com.example.MyClass]```

# SYNOPSIS

**serialver** [_-classpath path_] [_options_] _classname_

# PARAMETERS

**-classpath** _PATH_
> 类搜索路径。

**-J** _FLAG_
> 将选项传给 Java 运行时（例如 -J-Xms48m）。

**-show**
> 显示 GUI 检查器（现代 JDK 版本已移除）。

# DESCRIPTION

**serialver** 计算并显示实现了 Serializable 接口的 Java 类的 serialVersionUID。该 UID 是由类结构（字段、方法、接口）派生的哈希值，Java 的序列化机制用它来验证序列化对象的发送方和接收方是否具有兼容的类定义。

当类未显式声明 serialVersionUID 时，JVM 会在运行时自动计算一个。使用 serialver 获取该值并将其硬编码到类源码中，可以防止在类结构发生仍与旧有序列化形式兼容的变化时出现不兼容的类版本错误。

# CAVEATS

类必须实现 Serializable。需要 JDK。**-show** GUI 模式在近期的 JDK 版本中已被移除。

# HISTORY

**serialver** 是 **Java Development Kit** 的一部分，为 Serializable 类提供 serial version UID 计算。

# SEE ALSO

[java](/man/java)(1), [javac](/man/javac)(1), [jar](/man/jar)(1)
