# TAGLINE

并行运行任务，充分利用多个 CPU 核心

# TLDR

**对多个输入运行命令**

```parallel [gzip] ::: [*.txt]```

**将输入通过管道传给并行任务**

```cat [urls.txt] | parallel [curl -O]```

**以指定任务数运行**

```parallel -j [4] [command] ::: [args]```

**将输入用作参数占位符**

```parallel [wget {}] ::: [url1] [url2]```

**多个输入来源**

```parallel [convert {1} {2}] ::: [*.jpg] ::: [--resize 50%]```

**在远程主机上运行**

```parallel -S [host1,host2] [command] ::: [args]```

**显示进度条**

```parallel --bar [command] ::: [args]```

**试运行**（只显示命令而不执行）

```parallel --dry-run [command] ::: [args]```

# SYNOPSIS

**parallel** [_-j jobs_] [_-S hosts_] [_--bar_] [_options_] _command_ **:::** _arguments_

# PARAMETERS

**-j**, **--jobs** _N_
> 并行任务数（N、N%、+N、-N）。

**-S**, **--sshlogin** _HOSTS_
> 用于分布式执行的远程主机。

**-a**, **--arg-file** _FILE_
> 从文件读取参数。

**:::**, **:::::**
> 参数分隔符（内联输入或来自文件）。

**{}**
> 参数替换字符串。

**{#}**
> 任务编号。

**{%}**
> 任务槽编号。

**{.}**
> 去掉扩展名的参数。

**{/}**
> 参数的基本名（basename）。

**{//}**
> 参数所在的目录。

**--bar**
> 显示进度条。

**--eta**
> 显示预计完成时间。

**--dry-run**
> 只显示命令而不执行。

**--keep-order**, **-k**
> 保持输出顺序。

**--halt** _MODE_
> 何时中止：never、soon、now。

**--results** _DIR_
> 将输出保存到目录中的文件。

**--delay** _TIME_
> 任务启动之间的延迟。

**--retries** _N_
> 重试失败的任务。

**--timeout** _TIME_
> 每个任务的最长运行时间。

# DESCRIPTION

**GNU Parallel** 并行运行任务，充分利用多个 CPU 核心。它是 xargs -P 的更强替代品，专为命令行任务的并行处理而设计。

参数可以来自命令行（:::）、文件（::::）或标准输入。占位符 {} 会被替换为每个参数。{.}（无扩展名）、{/}（基本名）和 {//}（目录部分）等变体支持灵活的文件名操作。

任务控制包括限制并行度（-j）、分发到 SSH 主机（-S）以及失败处理（--halt）。输出可以保持顺序（--keep-order），也可以保存到单独的文件（--results）。

在分布式计算场景中，parallel 会把必要的文件复制到远程主机、运行任务并取回输出。这让你无需复杂的作业调度器就能搭建集群。

借助 --bar 或 --eta 进行进度跟踪，有助于监控长时间运行的批处理任务。日志选项会记录哪些任务运行过、哪些失败了，便于事后分析。

# CAVEATS

复杂命令的 Shell 引号转义可能比较棘手。它与 moreutils 的 parallel（一个更简单的工具）不同。进度条需要终端环境。分布式模式需要先配置好 SSH 密钥。内存占用随任务数增长。不加 -k 时各任务的输出会交错在一起。

# HISTORY

**GNU Parallel** 由 **Ole Tange** 从 **2007 年**前后开始编写。它被设计成一个通用的并行化工具，比 xargs 更灵活。该工具后来加入了分布式计算功能和精细的任务控制。它以 GPL 许可发布，并请求在学术作品中引用它。

# INSTALL

```apt: sudo apt install moreutils```

```dnf: sudo dnf install moreutils```

```pacman: sudo pacman -S moreutils```

```apk: sudo apk add parallel```

```zypper: sudo zypper install moreutils```

```brew: brew install moreutils```

```nix: nix profile install nixpkgs#moreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xargs](/man/xargs)(1), [make](/man/make)(1), [sem](/man/sem)(1), [nohup](/man/nohup)(1)
