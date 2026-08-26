# TAGLINE

从 Java 源代码生成 API 文档

# TLDR

**生成文档**

```javadoc [*.java]```

**输出到目录**

```javadoc -d [docs/] [*.java]```

**包含私有成员**

```javadoc -private [*.java]```

**使用 classpath 生成**

```javadoc -cp [lib/*] [src/*.java]```

**为包生成文档**

```javadoc -d [docs/] -sourcepath [src/] [com.example]```

**链接到外部文档**

```javadoc -link [https://docs.oracle.com/javase/17/docs/api/] [*.java]```

# SYNOPSIS

**javadoc** [_options_] _sources_...

# PARAMETERS

**-d** _DIR_
> 输出目录。

**-sourcepath** _PATH_
> 源文件路径。

**-cp** _PATH_
> 依赖项的类路径。

**-private**
> 包含所有成员。

**-public**
> 仅包含 public 成员。

**-link** _URL_
> 链接到外部文档。

**-author**
> 包含 @author 标签。

**-version**
> 包含 @version 标签。

**-subpackages** _PKGS_
> 递归处理子包（冒号分隔）。

**-encoding** _NAME_
> 源文件编码。

**-windowtitle** _TITLE_
> 浏览器窗口标题。

**-doctitle** _TITLE_
> 概览页上的标题。

**--help**
> 显示帮助信息。

# DESCRIPTION

**javadoc** 从 Java 源代码生成 API 文档。它解析 Javadoc 注释并生成 HTML 页面。

该工具会生成可导航的文档，包括类层次结构、方法详情和交叉引用。它是标准的 Java 文档生成器。

# CAVEATS

需要源代码。注释格式很重要。大型项目可能较慢。

# HISTORY

javadoc 自 Java 1.0 起就是 **JDK** 的一部分，由 **Sun Microsystems** 创建，用于生成 API 文档。

# SEE ALSO

[javac](/man/javac)(1), [java](/man/java)(1), [doxygen](/man/doxygen)(1)
