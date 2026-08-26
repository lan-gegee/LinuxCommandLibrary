# TAGLINE

反汇编 .NET 程序集

# TLDR

**反汇编 .NET 程序集**

```monodis [assembly.dll]```

**显示程序集元数据**

```monodis --assembly [assembly.dll]```

**显示类型定义**

```monodis --typedef [assembly.dll]```

**输出到文件**

```monodis [assembly.dll] > [output.il]```

# SYNOPSIS

**monodis** [_options_] _assembly_

# PARAMETERS

**--assembly**
> 显示程序集表。

**--typedef**
> 显示类型定义。

**--typeref**
> 显示类型引用。

**--methoddef**
> 显示方法定义。

**--method** _name_
> 反汇编特定方法。

**--output** _file_
> 输出到文件。

**--mscorlib**
> 反汇编时引用 mscorlib。

# DESCRIPTION

**monodis** 将 .NET 程序集（DLL/EXE）反汇编为 CIL（Common Intermediate Language，公共中间语言）文本。它是 Mono 框架的一部分，可用于调试、逆向工程和理解 .NET 字节码。

# INSTALL

```apt: sudo apt install mono-utils```

```pacman: sudo pacman -S mono```

```apk: sudo apk add mono```

```brew: brew install mono```

```nix: nix profile install nixpkgs#mono```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[monop](/man/monop)(1)
