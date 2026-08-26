# TAGLINE

面向 Python 打包的 debhelper 扩展

# TLDR

**用 debhelper 构建 Python 3 软件包**

```dh_python3```

**指定支持的 Python 版本**

```dh_python3 --shebang=/usr/bin/python3```

**使用指定的 Python 包目录构建**

```dh_python3 -p [package-name]```

**从 requires.txt 生成依赖关系**

```dh_python3 --depends```

# SYNOPSIS

**dh_python3** [_options_]

**dh_python2** [_options_] (deprecated)

# PARAMETERS

**-p**, **--package** _package_
> 只作用于指定软件包。

**-n**, **--no-package** _package_
> 排除指定软件包。

**--shebang** _path_
> 在 shebang 中使用指定的 Python 解释器。

**--depends** _section_
> 从指定部分生成依赖关系。

**--recommends** _section_
> 从指定部分生成推荐依赖。

**--suggests** _section_
> 从指定部分生成建议依赖。

**-v**, **--verbose**
> 详细输出。

**-O**_opt_
> 向 debhelper 传递选项。

# DESCRIPTION

**dh-python** 为 Debian 中的 Python 模块和应用打包提供 debhelper 扩展。主要命令是处理 Python 3 软件包的 **dh_python3** 和已弃用的 Python 2 工具 **dh_python2**。

这些工具负责 Python 特有的打包任务：对模块进行字节码编译、根据 Python 元数据生成依赖关系、修正 shebang 以使用系统 Python，以及创建正确的包关系。

在 debian/rules 中，dh_python3 通常通过 dh 序列执行器加 **--with python3** 自动调用。它从 debian/control 和 Python 元数据文件读取配置。

# CAVEATS

Python 2 支持（dh_python2）已被弃用并从现代 Debian 中移除。多 Python 版本需要谨慎处理。不直接支持虚拟环境；软件包安装到系统目录。字节码编译错误可能意味着存在语法问题。

# HISTORY

dh-python 为 Debian 而开发，用以替代更早的 python-support 和 python-central 系统。它由 **Piotr Ożarowski** 在 **2012 年**前后创建，在 Python 3 成为标准之际提供了更简洁的打包方案。该工具成为 Debian Python 软件包的标准方法，Ubuntu 及其衍生版也在使用。

# INSTALL

```aur: yay -S dh-python```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pybuild](/man/pybuild)(1), [dh](/man/dh)(1), [debhelper](/man/debhelper)(7)
