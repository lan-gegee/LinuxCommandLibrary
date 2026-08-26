# TAGLINE

Raku 编程语言解释器

# TLDR

**启动交互式 REPL** 会话

```raku```

**执行 Raku 脚本**

```raku [path/to/script.raku]```

**运行单行程序**

```raku -e 'say "Hello, World!"'```

**只检查脚本语法而不执行**

```raku -c [path/to/script.raku]```

**对输入的每一行运行程序**（类似 awk/sed）

```cat [path/to/file] | raku -ne 'say .uc'```

**运行处理完每行后还打印该行的单行程序**

```cat [path/to/file] | raku -pe '.=uc'```

**添加模块搜索路径**并在执行前加载模块

```raku -I [lib] -M [MyModule] [path/to/script.raku]```

**提取并显示内嵌 Pod 文档**

```raku --doc [path/to/script.raku]```

# SYNOPSIS

**raku** [_switches_] [**--**] [_programfile_] [_arguments_]

# PARAMETERS

**-c**
> 仅检查语法（会运行 BEGIN 和 CHECK 块，但不执行程序）。

**-e** _program_
> 执行一行程序。默认启用严格模式。

**-n**
> 对输入的每一行运行一次程序。

**-p**
> 与 **-n** 相同，但还会在每行结束时打印 **$_**。

**-I** _path_
> 将 _path_ 添加到模块搜索路径。

**-M** _module_
> 在运行程序前加载 _module_。

**-o**, **--output** _name_
> 指定编译输出文件的名称。

**-h**, **--help**
> 显示帮助文本。

**-v**, **--version**
> 显示版本信息。

**-V**
> 打印配置摘要。

**--doc**[=_module_]
> 提取内嵌 Pod 文档并以文本打印。可选用 **Pod::To::**_module_ 进行渲染（例如 **--doc=HTML**）。

**--target** _stage_
> 指定要输出的编译阶段（parse、ast、mast、mbc）。

**--optimize** _level_
> 设置优化级别（0 到 3）。

**--rakudo-home** _path_
> 覆盖 Rakudo 运行时文件的路径。

**--stagestats**
> 显示每个编译阶段所花的时间。

**--ll-exception**
> 出错时显示底层回溯信息。

**--profile**[=_name_]
> 将性能剖析信息写入文件。格式由扩展名决定（.json、.sql 或 .html）。

**--profile-compile**[=_name_]
> 将编译期性能剖析信息写入文件。

**--full-cleanup**
> 尝试释放所有内存并干净退出。

**--debug-port** _port_
> 在 _port_ 上监听调试器连接。

**--debug-suspend**
> 在入口点暂停执行。

# DESCRIPTION

**raku** 是 **Raku** 编程语言（原名 Perl 6）的解释器。Raku 是一门多范式语言，支持过程式、面向对象、函数式和并发编程。它具有渐进类型系统、基于文法的强大模式匹配、内置并发原语，以及全面贯穿的 Unicode 支持。

不带参数调用时，raku 会启动交互式 REPL（读取-求值-打印循环）。给定程序文件或使用 **-e** 选项时，它会编译并执行相应代码。**-n** 和 **-p** 标志提供类 awk/sed 的单行程序能力，可逐行处理输入。

该解释器由 **Rakudo** 实现——这是主要的 Raku 编译器，以 MoarVM 虚拟机为目标（也可选用 JVM）。Raku 脚本按惯例使用 **.raku** 文件扩展名（此前为 **.p6** 或 **.pl6**）。

# CAVEATS

由于编译开销，启动时间可能明显慢于 Perl 5 或 Python。**-c** 标志会运行 BEGIN 和 CHECK 块，因此语法检查并非完全没有副作用。模块生态比 Perl 5 的 CPAN 小。对于长时间运行的程序，**--profile** 选项可能生成非常大的输出文件。

# HISTORY

Raku 始于 **Perl 6**，由 **Larry Wall** 于 **2000 年**宣布，是对 Perl 语言的彻底重新设计。经过近二十年的开发，首个稳定版本（**Rakudo Star 2015.12**）于 **2015 年 12 月**发布。**2019 年 10 月**，该语言正式从 Perl 6 更名为 **Raku**，以建立独立于 Perl 5 的身份。主要实现是运行在 **MoarVM** 虚拟机上的 **Rakudo**。

# INSTALL

```apt: sudo apt install rakudo```

```dnf: sudo dnf install rakudo```

```apk: sudo apk add rakudo```

```zypper: sudo zypper install rakudo```

```brew: brew install rakudo```

```nix: nix profile install nixpkgs#rakudo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[perl](/man/perl)(1), [python](/man/python)(1), [ruby](/man/ruby)(1)
