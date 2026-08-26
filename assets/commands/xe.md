# TAGLINE

简单的 xargs 和 apply 替代品

# TLDR

**为 stdin 的每一行运行命令**

```cat [list.txt] | xe [command]```

**使用 {} 作为参数占位符**

```cat [list.txt] | xe [command] {}```

**以 N 个作业并行执行**

```cat [urls.txt] | xe -j [4] curl {}```

**在 -- 之后直接传递参数**

```xe -a -- mv {} {}.bak -- [file1] [file2]```

**以 null 分隔的输入**（用于带空格的文件名）

```find . -print0 | xe -0 echo {}```

**每条命令最多传 N 个参数**

```xe -N [10] rm -- [*.txt]```

**Dry-run：只打印命令而不执行**

```cat list.txt | xe -n [command] {}```

# SYNOPSIS

**xe** [_-0FLnqvR_] [_-I replace-arg_] [_-N maxargs_] [_-j maxjobs_] [_-f argfile_] [_-s shellscript_] [_-a_] [_command_ [_args...]]

# DESCRIPTION

**xe** 是一款从文件列表或参数构建命令行的工具，结合了 **xargs**(1) 和 **apply**(1) 的最佳特性。默认情况下它对每个输入行运行一次给定命令，并将 **{}** 替换为该参数，使常见用法比 **xargs** 更简单。

与 xargs 不同，xe 的默认行为很合理：等价于 `xargs -d'\n' -I{} -n1 -r`。参数可以从 stdin（默认）、通过 **-f** 从文件、或通过 **-a** 直接从命令行读取。

**xe** 支持通过 **-j** 并行执行、通过 **-p** 进行 make 风格的百分号规则匹配，并可通过 **-s** 对每个参数调用一个 shell 脚本。

# PARAMETERS

**-0**
> 输入参数以 NUL 字节而不是换行符分隔。配合 `find -print0` 很有用。

**-a**
> 从命令行获取参数（位于命令之后，以 **--** 分隔），而不是从 stdin 获取。

**-A** _argsep_
> 使用自定义参数分隔符代替 **--**（隐含 **-a**）。

**-f** _argfile_
> 从 _argfile_ 读取参数而不是 stdin。

**-F**
> Fatal：命令执行失败时停止并退出。

**-I** _replace-arg_
> 设置替换字符串（默认：**{}**）。

**-j** _maxjobs_
> 最多并发运行 _maxjobs_ 个进程。

**-L**
> 按行缓冲输出，使并发作业的输出行不会交错。

**-N** _maxargs_
> 每次命令调用最多传入 _maxargs_ 个参数（默认：**1**）。

**-n**
> Dry-run：打印将要执行的命令而不实际运行。

**-p**
> 用于按模式分发命令的 make 风格百分号规则匹配。

**-q**
> 安静模式：将命令的 stdout/stderr 重定向到 /dev/null。

**-R**
> 未提供任何参数时返回退出状态 122（而不是 0）。

**-s** _shellscript_
> 通过 shell 执行 _shellscript_；参数可通过 $1、$2 等访问。

**-v**
> 详细模式：运行前将命令打印到 stderr。

# CAVEATS

虽然目标相似，**xe** 与 XenServer 的 **xe** CLI 以及 xargs 都不相同。如果需要 xargs 兼容性，标志和行为可能有差异（例如 xe 默认使用 **{}** 作为占位符，并且在未指定 **-N** 时总是每个参数运行一次命令）。

# HISTORY

**xe** 由 **Leah Neukirchen** 编写，作为 **xargs**(1) 和 **apply**(1) 的现代化替代品，拥有更合理的默认值和更简洁的接口。它是一个小巧、可移植的 C 程序。

# INSTALL

```apt: sudo apt install xe```

```brew: brew install xe```

```nix: nix profile install nixpkgs#xe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xargs](/man/xargs)(1), [parallel](/man/parallel)(1), [find](/man/find)(1)
