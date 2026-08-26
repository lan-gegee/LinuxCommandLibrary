# TAGLINE

生成 BEAM 字节码的 Erlang 编译器

# TLDR

**编译 Erlang 模块**

```erlc [module.erl]```

**编译到指定目录**

```erlc -o [ebin] [module.erl]```

**附带调试信息编译**

```erlc +debug_info [module.erl]```

**指定头文件目录**

```erlc -I [include] [module.erl]```

**编译多个文件**

```erlc [*.erl]```

**将警告视为错误**

```erlc -Werror [module.erl]```

# SYNOPSIS

**erlc** [_options_] _files_...

# DESCRIPTION

**erlc** 是 Erlang 编译器，把 Erlang 源文件（.erl）转换为 BEAM 字节码（.beam）。它是编译 Erlang 模块的标准方式。

该编译器支持优化、调试和头文件路径等多种选项。它通常经由 rebar3 等构建工具调用，但也可以直接使用。

# PARAMETERS

**-o** _directory_
> 编译产物的输出目录。

**-I** _directory_
> 添加头文件目录。

**-D** _name[=value]_
> 定义宏。

**-W** _level_
> 警告级别。

**-Werror**
> 将警告视为错误。

**+debug_info**
> 包含调试信息。

**+native**
> 本地代码编译（HiPE）。

**-b** _type_
> 输出类型（beam、asm 等）。

**-v**
> 详细输出。

**-pa** _path_
> 添加代码路径。

# CAVEATS

需要安装 Erlang/OTP。OTP 24 及以上版本已弃用本地编译。头文件路径必须显式指定。模块名必须与文件名一致。

# HISTORY

**erlc** 自 **Erlang/OTP** 早期发布起便是其中一员。Erlang 由 **Joe Armstrong** 等人自 **1986 年**起在 **Ericsson** 开发，**1998 年**开源发布。该编译器为 Erlang 虚拟机生成 BEAM 字节码。

# INSTALL

```apt: sudo apt install erlang-base```

```apk: sudo apk add erlang27```

```zypper: sudo zypper install erlang27```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[erl](/man/erl)(1)
