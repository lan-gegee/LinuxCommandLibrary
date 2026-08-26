# TAGLINE

Debian 软件包变更日志编辑器

# TLDR

**添加新的变更日志条目**

```dch "[changelog message]"```

**为新版本递增版本号**

```dch -i```

**以指定版本创建新的变更日志**条目

```dch -v [1.0.0-1]```

**在编辑器中编辑**变更日志

```dch -e```

**追加到当前**条目

```dch -a "[additional message]"```

**为特定发行版创建**条目

```dch -D [unstable] "[message]"```

**设置紧急程度**

```dch -u [high] "[message]"```

# SYNOPSIS

**dch** [_options_] [_message_]

# PARAMETERS

_MESSAGE_
> 要添加的变更日志条目文本。

**-i**, **--increment**
> 为新上游版本递增版本号。

**-v** _VERSION_
> 以指定版本创建条目。

**-a**, **--append**
> 追加到当前变更日志条目。

**-e**, **--edit**
> 在编辑器中打开变更日志。

**-D** _DIST_
> 设置目标发行版。

**-u** _URGENCY_
> 设置紧急程度：low、medium、high、emergency、critical。

**-n**, **--nmu**
> 非维护者上传（NMU）版本递增。

**-b**, **--force-bad-version**
> 允许使用低于当前版本的版本号。

**-p**, **--preserve**
> 保留目录名作为软件包名。

**-r**, **--release**
> 完成发布条目（设置发行版和时间戳）。

**--create**
> 创建新的变更日志文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dch**（Debian changelog）是用于编辑 Debian 软件包变更日志文件（debian/changelog）的工具。它可以自动完成版本号递增和条目格式化，并维持 Debian 打包所要求的严格变更日志格式。

该工具处理 Debian 变更日志繁琐的格式要求，包括正确的日期格式、来自 DEBEMAIL/DEBFULLNAME 环境变量的维护者信息，以及版本字符串的处理。

dch 对 Debian 软件包维护者至关重要，可在软件包更新、安全修复和新上游版本发布期间自动化变更日志工作流。

# CAVEATS

需要正确配置 DEBEMAIL 和 DEBFULLNAME 环境变量。必须在包含 debian/changelog 的目录中运行。版本字符串格式必须遵循 Debian 规范。

# HISTORY

dch 是 **devscripts** 的一部分，这是一套面向 Debian 软件包维护者的工具集。自 1990 年代中期以来，它一直是 Debian 的核心开发工具，并随 Debian 打包标准一同演进。

# SEE ALSO

[debchange](/man/debchange)(1), [dpkg-buildpackage](/man/dpkg-buildpackage)(1), [dpkg](/man/dpkg)(1)
