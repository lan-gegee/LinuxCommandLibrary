# TAGLINE

编译时区数据文件

# TLDR

**编译时区数据**到默认目录

```zic [path/to/tzdata_file]```

**编译到指定**输出目录

```zic -d [path/to/output_directory] [path/to/tzdata_file]```

**编译时包含闰秒**信息

```zic -L [path/to/leapseconds] [path/to/tzdata_file]```

**设置本地时区**链接

```sudo zic -l [America/New_York]```

**编译时输出详细**警告

```zic -v [path/to/tzdata_file]```

**从标准输入读取时区数据**

```zic -d [path/to/output_directory] -```

# SYNOPSIS

**zic** [_OPTIONS_] [_FILE..._]

# PARAMETERS

**-d** _DIRECTORY_
> 编译后的 TZif 文件的输出目录（默认：系统时区目录）。

**-l** _timezone_
> 使用给定时区作为本地时间，并创建 localtime 链接。

**-p** _timezone_
> 对缺少转换规则的 POSIX 风格 TZ 字符串使用该时区的规则。

**-L** _leapsecondfile_
> 从指定文件读取闰秒信息。

**-v**
> 报告关于输入数据的警告，包括超出可表示范围的年份。

**-b** _(slim|fat)_
> 输出向后兼容数据。"fat" 为旧软件生成额外条目。"slim" 保持文件精简（默认）。

**-r** _@lo/@hi_
> 将输出限制在给定范围内的时间戳。

**-D**
> 不创建输出文件的各级父目录。

**-m** _mode_
> 设置创建的 TZif 文件的文件权限。

**--version**
> 输出版本信息并退出。

# DESCRIPTION

**zic** 是时区编译器。它读取描述时区规则（时区名称、UTC 偏移量、夏令时转换）的文本文件，生成 C 库的 localtime() 及相关函数所使用的二进制 TZif（Time Zone Information Format）文件。

输入文件采用特定格式，通过 Rule、Zone 和 Link 行定义时区转换。编译出的二进制文件通常安装在 /usr/share/zoneinfo/ 中。zic 编译器通常作为 tzdata 软件包安装的一部分运行。

# CAVEATS

需要格式正确的时区源文件。写入系统目录时通常需要 root 权限。错误的数据可能破坏整个系统的时间处理。用于 year 类型命令的 **-y** 选项已过时，现代版本不再支持。

# INSTALL

```apt: sudo apt install libc-bin```

```apk: sudo apk add tzdata-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zdump](/man/zdump)(8), [tzselect](/man/tzselect)(8)
