# TAGLINE

Windows DLL 导入库创建工具

# TLDR

**从 def 文件创建导入库**

```dlltool -d [library.def] -l [library.a]```

**从 DLL 创建 def 文件**

```dlltool -z [output.def] [library.dll]```

**从 def 文件和目标文件创建**导出文件

```dlltool -d [library.def] -e [exports.o] [objects.o]```

**指定机器类型**

```dlltool -m [i386] -d [library.def] -l [library.a]```

**同时创建导入库和**导出文件

```dlltool -d [library.def] -l [library.a] -e [exports.o]```

# SYNOPSIS

**dlltool** [_options_] [_file_...]

# PARAMETERS

**-d**, **--input-def** _FILE_
> 读取指定的 .def 文件。

**-l**, **--output-lib** _FILE_
> 生成导入库。

**-e**, **--output-exp** _FILE_
> 生成导出文件。

**-z**, **--output-def** _FILE_
> 生成 .def 文件（来自 DLL 或目标文件）。

**-y**, **--output-delaylib** _FILE_
> 创建延迟导入库。

**-m**, **--machine** _MACHINE_
> 目标机器类型（如 i386、x86_64、arm）。

**-D**, **--dllname** _NAME_
> 记录在库中的输入 DLL 名称。

**-U**, **--add-underscore**
> 为所有导出符号添加下划线前缀。

**-k**, **--kill-at**
> 去掉 stdcall 导出名中的 @n 后缀。

**-A**, **--add-stdcall-alias**
> 为不带 @n 的 stdcall 符号添加别名。

**--export-all-symbols**
> 导出所有全局符号和弱符号。

**-I**, **--identify** _FILE_
> 报告导入库关联的 DLL 名称。

**-v**, **--verbose**
> 显示正在执行的操作。

**--help**
> 显示帮助信息。

# DESCRIPTION

**dlltool** 是一款 GNU binutils 工具，用于创建在 Windows 上构建和使用动态链接库（DLL）所需的各类文件。它处理模块定义（.def）文件，并生成导入库和导出文件。

导入库允许在编译时链接 DLL。该工具会生成运行时解析所需的桩代码。导出文件则定义了 DLL 提供给其他程序使用的符号。

dlltool 是在 Unix 系统上交叉编译 Windows 软件的必备工具，也用于配合 MinGW 等工具链创建 DLL。

# CAVEATS

仅限 Windows 相关用途。def 文件语法必须正确。机器类型必须与目标架构匹配。导入库格式可能因工具链而异。

# HISTORY

dlltool 是 **GNU binutils** 的组成部分，为交叉编译环境中 Windows DLL 的创建提供支持。它使 MinGW 等 GNU 工具链能够构建 Windows 软件。

# SEE ALSO

[ld](/man/ld)(1), [nm](/man/nm)(1), [objdump](/man/objdump)(1), [windres](/man/windres)(1)
