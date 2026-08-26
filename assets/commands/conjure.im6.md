# TAGLINE

ImageMagick MSL 脚本解释器

# TLDR

**执行 Magick Scripting Language**（MSL）脚本

```conjure.im6 [script.msl]```

**以详细输出执行**

```conjure.im6 -verbose [script.msl]```

**使用自定义 define 执行脚本**

```conjure.im6 -define [key]=[value] [script.msl]```

**以调试模式运行**

```conjure.im6 -debug all [script.msl]```

**以特定资源限制执行**

```conjure.im6 -limit memory [256MB] [script.msl]```

# SYNOPSIS

**conjure.im6** [_options_] _script.msl_

# PARAMETERS

**-debug** _EVENTS_
> 为指定的事件类型启用调试输出。

**-define** _KEY=VALUE_
> 设置可在脚本内访问的配置值。

**-limit** _TYPE VALUE_
> 设置资源限制（memory、map、disk、file、thread、time）。

**-log** _FORMAT_
> 日志输出格式规格。

**-monitor**
> 监视图像处理操作的进度。

**-quiet**
> 屏蔽所有警告消息。

**-regard-warnings**
> 将警告视为错误。

**-seed** _VALUE_
> 为伪随机数生成器设置种子。

**-verbose**
> 执行期间启用详细输出。

**-version**
> 显示版本信息。

# DESCRIPTION

**conjure.im6** 是 ImageMagick 第 6 版的 Magick Scripting Language（MSL）解释器。MSL 是一种基于 XML 的脚本语言，用于以编程方式执行复杂的图像处理操作。

MSL 脚本使用与 ImageMagick 操作相对应的 XML 标签来定义图像处理工作流。这样无需编写 shell 脚本或使用编程语言绑定，就能创建可复用、可参数化的图像处理流水线。

MSL 对批量处理特别有用，也适合创建可一致应用于大量图像的复杂图像处理模板。它主要面向希望进行自定义图像处理、但又不想借助编程语言或编译器的用户。

# CAVEATS

与通过 shell 脚本或编程语言使用 ImageMagick 相比，MSL 是一种采用率较低的专业语言。ImageMagick 6 已进入维护模式；ImageMagick 7 采用不同的脚本方案。**.im6** 后缀确保在同时安装了两个版本的系统上使用第 6 版。

# HISTORY

conjure 是 ImageMagick 脚本能力的一部分，支持基于 XML 的批量图像处理。ImageMagick 由 John Cristy 创建于 **1990** 年。带版本后缀的 **conjure.im6** 命令于 **2016** 年随 ImageMagick 7 的破坏性变更一同引入，使两个版本得以共存。

# SEE ALSO

[composite.im6](/man/composite.im6)(1), [display.im6](/man/display.im6)(1), [mogrify.im6](/man/mogrify.im6)(1), [magick](/man/magick)(1), [convert](/man/convert)(1)
