# TAGLINE

使用字符串替换重命名文件

# TLDR

使用**简单替换**重命名文件

```rename [foo] [bar] *```

**试运行**——显示将发生哪些重命名而不实际执行

```rename -v -n [foo] [bar] *```

**不覆盖**已存在的文件

```rename -o [foo] [bar] *```

修改**文件扩展名**

```rename .ext .bak *.ext```

为所有文件名**添加前缀**

```rename '' '[prefix]' *```

为带编号的文件**补零**

```rename foo foo00 foo? && rename foo foo0 foo??```

# SYNOPSIS

**rename** [_options_] _expression_ _replacement_ _file_...

# PARAMETERS

**-v**, **--verbose**
> 显示哪些文件正在被重命名

**-n**, **--no-act**
> 试运行；显示将要进行的重命名但不执行

**-o**, **--no-overwrite**
> 不覆盖已存在的文件

**-a**, **--all**
> 替换所有出现，而非仅第一次

**-l**, **--last**
> 替换最后一次出现而非第一次

**-s**, **--symlink**
> 重命名符号链接的目标而不是链接本身

**-i**, **--interactive**
> 覆盖前进行提示

**-V**, **--version**
> 显示版本信息

**-h**, **--help**
> 显示帮助信息

# DESCRIPTION

util-linux 的 **rename** 通过简单的字符串替换执行批量文件重命名。它将每个文件名中第一次出现的 _expression_ 替换为 _replacement_。与 Perl 版 rename 命令不同，它不使用正则表达式。

该命令处理所有匹配的文件，非常适合更改扩展名或添加前缀等批量操作。可以串联多个 rename 操作以实现更复杂的变换。

# CAVEATS

默认**不提示直接覆盖文件**；使用 **-n** 进行试运行，使用 **-o** 防止覆盖。除非指定 **-a**，否则只替换第一次出现。不支持正则表达式；复杂模式请使用 Perl 版 rename。

# HISTORY

属于 **util-linux**（标准 Linux 工具集）的一部分。提供基于简单字符串的重命名，与 Debian 系统上更强大（但更复杂）的 Perl 版 rename 相对。两者因同名而经常被混淆。

# SEE ALSO

[mv](/man/mv)(1), [rename](/man/rename)(1), [mmv](/man/mmv)(1)
