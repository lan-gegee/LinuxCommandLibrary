# TAGLINE

分析 Java 类的依赖关系

# TLDR

**分析类依赖**

```jdeps [class.jar]```

**显示包级别的依赖**

```jdeps -s [class.jar]```

**检查 JDK 内部 API 的使用情况**

```jdeps --jdk-internals [class.jar]```

**生成 module-info**

```jdeps --generate-module-info [dir] [class.jar]```

**分析指定的包**

```jdeps -p [com.example] [class.jar]```

**multi-release JAR 分析**

```jdeps --multi-release [17] [class.jar]```

# SYNOPSIS

**jdeps** [_options_] _path_...

# PARAMETERS

_PATH_
> JAR 文件或类目录。

**-s**, **--summary**
> 摘要级别的输出。

**--jdk-internals**
> 检查内部 API 的使用情况。

**--generate-module-info** _DIR_
> 生成 module-info.java。

**-p** _PACKAGE_
> 分析指定的包。

**--multi-release** _VERSION_
> 分析 multi-release JAR。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jdeps** 用于分析 Java 类的依赖关系。它显示一个 JAR 依赖哪些包和模块。

该工具有助于 Java 模块化迁移。它能识别出未来版本中可能失效的 JDK 内部 API 的使用。

# CAVEATS

是 JDK 的一部分。需要 class 文件而非源文件。输出格式可能有所不同。

# HISTORY

jdeps 在 **JDK 8** 中加入，用于帮助开发者理解依赖关系，并为 JDK 9 的 Java 模块系统做准备。

# SEE ALSO

[javap](/man/javap)(1), [java](/man/java)(1), [jar](/man/jar)(1)
