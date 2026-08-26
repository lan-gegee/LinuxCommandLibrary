# TAGLINE

基于 Apache Ant 的 PHP 构建工具

# TLDR

**运行默认目标**

```phing```

**运行特定目标**

```phing [target]```

**使用自定义构建文件**

```phing -f [build.xml] [target]```

**列出可用目标**

```phing -l```

**设置属性值**

```phing -D[name]=[value] [target]```

**以详细输出运行**

```phing -verbose [target]```

**以调试模式运行**

```phing -debug [target]```

**指定日志记录器**

```phing -logger phing.listener.DefaultLogger [target]```

# SYNOPSIS

**phing** [_options_] [_target_...]

# PARAMETERS

_TARGET_
> 要执行的构建目标。省略时运行默认目标。

**-f** _FILE_
> 使用指定的构建文件代替默认的 build.xml。

**-l**
> 列出构建文件中的可用目标。

**-D**_PROP_**=**_VALUE_
> 将构建属性设置为给定值，覆盖构建文件中的定义。

**-verbose**
> 输出详细信息以便调试。

**-debug**
> 输出调试级别信息。

**-q**, **-quiet**
> 抑制大部分输出，只显示错误。

**-logger** _CLASS_
> 指定自定义日志记录器类。

**-logfile** _FILE_
> 将输出写入日志文件。

**-find** _FILE_
> 向上级目录搜索构建文件。

# DESCRIPTION

**phing**（PHing Is Not GNU make）是一款基于 Apache Ant 的 PHP 项目构建工具。它使用 XML 构建文件来定义目标和任务，从而自动化 PHP 项目的工作流程，例如编译、测试、打包和部署。

Phing 提供丰富的内置任务，涵盖文件操作、PHP 专属任务（PHPUnit、PHP_CodeSniffer、phpDocumentor）、版本控制集成和归档创建。自定义任务可用 PHP 编写。

# CAVEATS

需要 PHP CLI。构建文件使用类 Ant 语法的 XML 格式。任务名和属性区分大小写。默认构建文件是当前目录下的 build.xml。

# HISTORY

Phing 最初由 **Andreas Aderhold** 于 2002 年创建，是 Apache Ant 的 PHP 移植版。其名称是一个递归缩写：PHing Is Not GNU make。

# INSTALL

```aur: yay -S phing```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ant](/man/ant)(1), [make](/man/make)(1), [composer](/man/composer)(1), [php](/man/php)(1)
