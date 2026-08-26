# TAGLINE

音频与数字信号处理语言编译器

# TLDR

**编译** ADscript 文件

```adscript [script.ad]```

编译并指定**输出文件**

```adscript [script.ad] -o [output]```

**直接运行** ADscript 文件

```adscript -r [script.ad]```

# SYNOPSIS

**adscript** [_options_] _file_

# DESCRIPTION

**adscript** 是 ADscript 编程语言的编译器。ADscript 是一门为音频和数字信号处理应用设计的领域专用语言。它为音频处理任务生成优化代码。

ADscript 将函数式编程概念与音频专用原语相结合，适合开发音频插件、合成引擎和信号处理算法。

# PARAMETERS

**-o** _file_
> 指定输出文件名

**-r**
> 直接运行脚本而不是编译

**-O** _level_
> 优化级别（0-3）

**-v**, **--verbose**
> 启用详细输出

**--help**
> 显示帮助信息

# CAVEATS

ADscript 是一门专门化语言；通用编程可能更适合选用其他语言。性能取决于目标平台和优化设置。

# HISTORY

ADscript 为音频编程应用而开发，在低层音频处理操作之上提供高层的抽象，同时保有实时音频所需的性能特征。

# SEE ALSO

[csound](/man/csound)(1)
