# TAGLINE

Mono 类结构查看器

# TLDR

**显示某个类型的结构**

```monop [System.String]```

**显示特定程序集中的类型**

```monop -r:[path/to/assembly.dll] [TypeName]```

**列出程序集中的所有类型**

```monop -r:[path/to/assembly.dll] --list```

**只显示该类型自身声明的成员**（排除继承的成员）

```monop --only-declared [System.Console]```

**按部分名称搜索类型**

```monop -s [PartialName]```

**显示私有成员**

```monop -a [System.String]```

# SYNOPSIS

**monop** [_options_] _typename_

# PARAMETERS

**-r:**_assembly_
> 引用特定的程序集文件。

**--only-declared**
> 只显示在指定类型中声明的成员（排除继承成员）。

**--filter-obsolete**
> 不显示已过时的类型和成员。

**--refs**
> 打印给定程序集引用的程序集列表。

**--list**
> 列出程序集中的所有类型。

**-a**
> 显示私有成员。

**-s**
> 在所有已知程序集中按部分名称搜索类型。

# DESCRIPTION

**monop** 是 Mono 框架的命令行类结构查看器。它显示 .NET 类型的结构，包括类签名、方法、属性、字段、事件和构造函数。它可以检查来自标准库或特定程序集的类型，无需反编译器或 IDE 即可快速查阅 API，非常实用。

# INSTALL

```pacman: sudo pacman -S mono```

```apk: sudo apk add mono```

```brew: brew install mono```

```nix: nix profile install nixpkgs#mono```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[monodis](/man/monodis)(1), [mono](/man/mono)(1), [dotnet](/man/dotnet)(1)
