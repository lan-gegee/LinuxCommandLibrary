# TAGLINE

基于 Java 的构建自动化工具

# TLDR

**运行**默认目标

```ant```

运行**指定目标**

```ant [build]```

使用**构建文件**运行

```ant -f [build.xml] [target]```

携带**属性**运行

```ant -Dproperty=[value] [target]```

**列出**可用目标

```ant -p```

**安静**运行

```ant -q [target]```

# SYNOPSIS

**ant** [_-f buildfile_] [_-D property=value_] [_options_] [_target_]

# DESCRIPTION

**ant**（Another Neat Tool）是一款基于 Java、使用 XML 配置文件的构建工具。它自动化软件构建流程，包括编译、测试、打包和部署 Java 应用。

构建文件（通常是 build.xml）定义包含任务的 target。Ant 按依赖顺序执行任务，类似 make，但采用 XML 语法并可跨平台运行。

# PARAMETERS

**-f** _file_, **-buildfile** _file_
> 构建文件（默认：build.xml）

**-D** _prop=val_
> 设置属性值

**-p**, **-projecthelp**
> 列出可用目标

**-q**, **-quiet**
> 最少输出

**-v**, **-verbose**
> 详细输出

**-d**, **-debug**
> 调试输出

**-e**, **-emacs**
> 无装饰的输出

**-S**, **-silent**
> 只打印任务输出和构建失败信息

**-k**, **-keep-going**
> 继续执行所有不依赖失败目标的目标

**-lib** _path_
> 指定搜索 jar 包和类的路径

**-l** _file_, **-logfile** _file_
> 将日志输出写入给定文件

**-logger** _classname_
> 执行日志记录的类

**-propertyfile** _name_
> 从文件加载所有属性（-D 属性优先级更高）

**-noinput**
> 不允许交互式输入

**-s** _file_, **-find** _file_
> 向文件系统根目录方向搜索构建文件并使用它

**-nice** _number_
> 主线程的 nice 值：1（最低）到 10（最高），默认 5

**-diagnostics**
> 打印有助于诊断问题的信息后退出

**-version**
> 显示版本

# CAVEATS

需要 Java 运行环境。对于复杂项目，XML 构建文件可能变得冗长。在现代 Java 项目中已基本被 Maven 和 Gradle 取代。

# HISTORY

**Apache Ant** 由 James Duncan Davidson 作为 Tomcat 项目的一部分创建，首个独立版本于 **2000 年**发布。在 Maven 于 2000 年代中期流行起来之前，它一直是主流的 Java 构建工具。

# INSTALL

```dnf: sudo dnf install ant```

```pacman: sudo pacman -S ant```

```apk: sudo apk add apache-ant```

```zypper: sudo zypper install ant```

```brew: brew install ant```

```nix: nix profile install nixpkgs#ant```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[mvn](/man/mvn)(1), [gradle](/man/gradle)(1), [make](/man/make)(1)

# RESOURCES

```[Source code](https://github.com/apache/ant)```

```[Homepage](https://ant.apache.org/)```

```[Documentation](https://ant.apache.org/manual/)```

<!-- verified: 2026-06-11 -->
