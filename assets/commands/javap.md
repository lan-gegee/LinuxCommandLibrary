# TAGLINE

反汇编 Java class 文件

# TLDR

**显示类的公共方法签名**

```javap [ClassName]```

**反汇编字节码指令**

```javap -c [ClassName]```

**显示所有成员（包括私有）**

```javap -p [ClassName]```

**输出栈大小、局部变量和常量池等详细信息**

```javap -v [ClassName]```

**反编译 JAR 文件中的类**

```javap -cp [lib.jar] [com.example.ClassName]```

**显示行号表和局部变量表**

```javap -l [ClassName]```

**显示内部类型签名**

```javap -s [ClassName]```

# SYNOPSIS

**javap** [_options_] _class_...

# PARAMETERS

_CLASS_
> 要反汇编的一个或多个类名或 .class 文件路径。

**-c**
> 反汇编每个方法的字节码指令。

**-p**, **-private**
> 显示所有类和成员，包括私有的。

**-protected**
> 仅显示 protected 和 public 的类和成员。

**-public**
> 仅显示 public 的类和成员。

**-package**
> 显示 package、protected 和 public 的类和成员（默认）。

**-v**, **-verbose**
> 打印栈大小、局部变量数量、方法参数和常量池。

**-l**
> 打印行号表和局部变量表。

**-s**
> 打印内部类型签名。

**-sysinfo**
> 显示类的系统信息（路径、大小、日期、MD5 哈希）。

**-cp** _PATH_, **-classpath** _PATH_
> 用于定位类的类路径。覆盖 CLASSPATH 环境变量。

**-bootclasspath** _PATH_
> 加载启动类（bootstrap classes）的路径。

**-J** _FLAG_
> 将标志直接传给 Java 运行时系统。

**--help**
> 显示帮助信息。

# DESCRIPTION

**javap** 是 JDK 自带的 Java class 文件反汇编器。它检查编译后的 .class 文件并显示其字段、方法的信息，还可以选择显示组成每个方法的字节码指令。

该工具适用于理解编译后的 Java 代码、调试编译问题、验证方法签名，以及在缺少原始源代码的情况下检查字节码。

# CAVEATS

显示的是编译后的字节码，而不是原始源代码。理解 JVM 字节码指令有助于解读 **-c** 输出。类名应使用点号表示法（com.example.MyClass），而不是文件路径。是 JDK 的一部分；需要安装 Java。

# HISTORY

**javap** 自 **Java 1.0** 起就是 **JDK** 的一部分，用于深入了解编译后的 Java 字节码。它在 **Java 7** 中得到大幅更新，改进了输出格式并增加了选项。

# SEE ALSO

[java](/man/java)(1), [javac](/man/javac)(1), [jar](/man/jar)(1)
