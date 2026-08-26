# TAGLINE

将 Java 源文件编译为可在 Java 虚拟机上运行的字节码 class 文件

# TLDR

**编译 Java 文件**

```javac [File.java]```

**编译多个文件**

```javac [File1.java] [File2.java]```

**编译当前目录下所有 Java 文件**

```javac *.java```

**使用 classpath 编译**

```javac -cp [lib/*:classes] [File.java]```

**为 class 文件指定输出目录**

```javac -d [out] [File.java]```

**按指定的 Java 版本兼容性编译**

```javac --release [11] [File.java]```

**启用所有警告**

```javac -Xlint:all [File.java]```

**以详细输出编译**

```javac -verbose [File.java]```

# SYNOPSIS

**javac** [_OPTIONS_] _SOURCE-FILES_

**javac** [_OPTIONS_] **@**_ARGFILE_

# PARAMETERS

**-d** _DIR_
> 编译后 class 文件的输出目录。

**-cp**, **-classpath** _PATH_
> 用于查找用户类文件和库的类路径。

**--module-path** _PATH_
> 用于查找应用模块的模块路径。

**-sourcepath** _PATH_
> 查找源文件的路径。

**--release** _VERSION_
> 针对特定的 Java SE 版本编译。

**-source** _VERSION_
> 源代码兼容版本。

**-target** _VERSION_
> 为特定 VM 版本生成 class 文件。

**-Xlint**[**:**_WARNINGS_]
> 启用警告（all、deprecation、unchecked 等）。

**-g**
> 包含调试信息。

**-verbose**
> 输出编译器正在执行的操作的相关消息。

**-deprecation**
> 显示使用了已废弃 API 的说明。

**-encoding** _ENCODING_
> 源文件的字符编码。

**-h** _DIR_
> 为 JNI 生成本机头文件。

**@**_FILE_
> 从文件读取选项和文件名。

# DESCRIPTION

**javac** 将 Java 源文件（.java）编译为可在 Java 虚拟机上运行的字节码 class 文件（.class）。它会进行语法和类型检查、优化代码，并生成平台无关的字节码。

编译器使用类路径定位被引用的类和库。对于模块化项目（Java 9+），模块路径指定模块的位置。**--release** 标志确保与特定 Java 版本在编译层面和可用 API 层面都保持兼容。

编译大量文件时，可使用 @argfile 避免命令行长度限制。argfile 中每行可以包含一个源文件或选项。

# CAVEATS

源文件和类文件必须按照目录路径匹配 Java 包结构。源文件之间存在循环依赖时，必须将这些文件一起编译。类路径分隔符在 Unix 上是 :，在 Windows 上是 ;。

# HISTORY

javac 自 **1996 年**的 Java 1.0 起就是 Java 开发工具包的一部分。编译器经历了显著演进，加入了泛型（Java 5）、模块（Java 9）以及众多语言特性。现代版本支持增量编译和注解处理。

# SEE ALSO

[java](/man/java)(1), [jar](/man/jar)(1), [javadoc](/man/javadoc)(1)
