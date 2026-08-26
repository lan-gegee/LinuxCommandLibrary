# TAGLINE

从源码生成 PHP API 文档

# TLDR

**使用默认配置生成文档**

```phpdox```

**使用指定的配置文件**

```phpdox -f [phpdox.xml]```

**只运行收集器阶段**（解析源码）

```phpdox -c```

**只运行生成器阶段**（产出文档）

```phpdox -g```

**生成骨架配置文件**

```phpdox --skel > [phpdox.xml]```

**生成不带注释的骨架配置**

```phpdox --skel --strip > [phpdox.xml]```

**列出可用的输出引擎**

```phpdox --engines```

# SYNOPSIS

**phpdox** [_options_]

# PARAMETERS

**-f**, **--file** _FILE_
> 使用指定的 XML 配置文件（默认为 ./phpdox.xml 或 ./phpdox.xml.dist）。

**-c**, **--collector**
> 只运行收集器过程（源码解析）。

**-g**, **--generator**
> 只运行生成器过程（文档输出）。

**--backends**
> 显示可用后端列表并退出。

**--engines**
> 显示可用输出引擎列表并退出。

**--enrichers**
> 显示可用输出增强器列表并退出。

**--skel**
> 显示带注释的骨架配置 XML 文件并退出。

**--strip**
> 使用 **--skel** 时去除骨架配置 XML 中的注释。

**-v**, **--version**
> 显示应用版本。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**phpDox** 基于标准技术（SRC、DOCBLOCK、XML 和 XSLT）从源码生成 PHP API 文档。它解析 PHP 源文件，提取 PHPDoc 注释块，并产出 HTML 文档。配置在 XML 文件中定义（通常是 **phpdox.xml**）。

文档生成过程分为两个阶段：**收集器**将源码解析为 XML 表示形式，**生成器**则使用可配置的引擎和增强器将其转换为输出。

# CONFIGURATION

**phpdox.xml**
> XML 配置文件，指定源码目录、输出路径、模板设置和构建目标。运行必需。可用 **--skel** 生成模板。

# CAVEATS

需要 XML 配置文件。建议在源代码中编写 PHPDoc 注释块，才能得到有用的输出。该项目已不再积极维护。

# INSTALL

```aur: yay -S phpdox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[phpdoc](/man/phpdoc)(1), [doxygen](/man/doxygen)(1), [php](/man/php)(1)
