# TAGLINE

为 C/C++ 代码生成语言绑定

# TLDR

**生成 Python 封装**

```swig -python [interface.i]```

**针对 C++ 生成**

```swig -c++ -python [interface.i]```

**指定输出文件**

```swig -python -o [wrap.c] [interface.i]```

**包含目录**

```swig -I[/usr/include] -python [interface.i]```

**生成 Java 封装**

```swig -java [interface.i]```

# SYNOPSIS

**swig** [_-python|-java|-ruby_] [_-c++_] [_-o file_] [_options_] _interface.i_

# PARAMETERS

**-python**
> 目标为 Python。

**-java**
> 目标为 Java。

**-ruby**
> 目标为 Ruby。

**-c++**
> C++ 模式。

**-o** _FILE_
> 输出文件。

**-I** _DIR_
> 包含路径。

**-module** _NAME_
> 模块名。

# DESCRIPTION

**swig**（Simplified Wrapper and Interface Generator）生成封装代码，使 C 和 C++ 库能够被其他编程语言调用。它读取接口定义文件（.i），其中描述了要暴露哪些函数、类和类型，并产出目标语言所需的胶水代码。

支持的目标语言包括 Python、Java、Ruby、Perl、PHP、Lua、Go、JavaScript、C# 等众多语言。SWIG 负责 C/C++ 与目标语言之间的自动类型转换和数据编组，包括复杂类型、指针、数组以及继承和模板等面向对象结构。

接口文件使用类似 C/C++ 头文件的语法，外加用于控制封装过程的 SWIG 指令。对较简单的场景，SWIG 还可以直接解析实际的 C/C++ 头文件。

# CAVEATS

接口文件有学习曲线。需要 C/C++ 知识。需与构建系统集成。

# HISTORY

**SWIG**（Simplified Wrapper and Interface Generator）由 **David Beazley** 创建，用于将 C/C++ 与脚本语言连接起来。

# INSTALL

```apt: sudo apt install swig```

```dnf: sudo dnf install swig```

```pacman: sudo pacman -S swig```

```apk: sudo apk add swig```

```zypper: sudo zypper install swig```

```brew: brew install swig```

```nix: nix profile install nixpkgs#swig```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cython](/man/cython)(1), [pybind11](/man/pybind11)(1), [ctypes](/man/ctypes)(1)
