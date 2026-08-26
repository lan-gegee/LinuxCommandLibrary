# TAGLINE

Ada 源文件预处理器

# TLDR

**预处理 Ada 源文件**

```gnatprep [input.adb] [output.adb]```

**使用符号定义文件预处理**

```gnatprep [input.adb] [output.adb] [defs.txt]```

**在命令行定义符号**

```gnatprep -DDEBUG=True [input.adb] [output.adb]```

**用空行替换预处理器行**

```gnatprep -b [input.adb] [output.adb]```

**将预处理器行保留为注释**

```gnatprep -c [input.adb] [output.adb]```

**列出已定义的符号**

```gnatprep -s [input.adb] [output.adb] [defs.txt]```

# SYNOPSIS

**gnatprep** _inputfile_ _outputfile_ [_definitions_file_] [_switches_]

# PARAMETERS

**-b**
> 用空行替换预处理器行和被删除的行。

**-c**
> 将预处理器行和被删除的行保留为注释。

**-D**_symbol_=_value_
> 在命令行上定义符号。

**-s**
> 将符号名和值列出到 stdout。

**-T**
> 只使用命令行或定义文件中定义的符号（不使用环境变量）。

**-u**
> 将未定义的符号视为 FALSE。

**-r**
> 生成源引用 pragma。

**-v**
> 详细模式，处理时显示文件名。

# DESCRIPTION

**gnatprep** 是 Ada 程序的预处理器。它处理 Ada 源文件中的条件编译指令（#if、#elsif、#else、#end if）和符号替换（$symbol）。虽然它是为 GNAT 设计的，但并不依赖 GNAT 特有的功能，可以独立使用。

# CAVEATS

-b 和 -c 都无法保留原始行号。若两者均未指定，除非给出 -r，否则预处理器行和被删除的行将被完全移除。

# INSTALL

```apt: sudo apt install gnat-12```

```dnf: sudo dnf install gcc-gnat```

```apk: sudo apk add gcc-gnat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnatmake](/man/gnatmake)(1), [gcc](/man/gcc)(1), [gprbuild](/man/gprbuild)(1), [m4](/man/m4)(1)
