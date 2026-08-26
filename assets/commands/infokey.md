# TAGLINE

为 GNU Info 阅读器编译自定义键绑定

# TLDR

**编译默认键绑定文件**

```infokey```

**编译指定的输入文件**

```infokey [path/to/file]```

**编译并输出到指定文件**

```infokey -o [path/to/output] [path/to/input]```

# SYNOPSIS

**infokey** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入文件（默认为 $HOME/.infokey）。

**-o** _FILE_
> 输出编译后的键文件（默认为 $HOME/.info）。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**infokey** 把包含 GNU Info 阅读器自定义键绑定和变量设置的源文件编译成二进制格式。它默认读取 $HOME/.infokey，并将编译结果写入 $HOME/.info。

输入文件包含若干区段，用于定义按键序列及其关联的动作。**#info** 区段定义 Info 窗口的键绑定，**#echo-area** 区段定义回显区的绑定，**#var** 区段设置 Info 变量。自定义绑定会覆盖 Info 默认的导航键。

# CAVEATS

输入文件格式为 Info 专用，使用自定义语法。二进制输出不可读。需要配合 GNU Info 阅读器才能使用编译后的绑定。在较新版本的 Texinfo（6.0+）中，infokey 命令已被弃用，Info 阅读器可以直接读取 .infokey 文本文件而无需编译。

# HISTORY

infokey 是 **GNU Texinfo** 软件包的一部分，用于自定义 Info 阅读器的键绑定。在 **Texinfo 6.0**（2015 年）中，独立的 infokey 命令被弃用，因为 Info 阅读器已能直接读取 .infokey 源文件。

# SEE ALSO

[info](/man/info)(1)
