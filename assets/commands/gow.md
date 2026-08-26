# TAGLINE

Go 命令的文件监听工具

# TLDR

**自动重载地运行**

```gow run [.]```

**运行特定文件**

```gow run [main.go]```

**带监听地运行测试**

```gow test [./...]```

**每次重启时清空终端**

```gow -c run [.]```

**除 .go 外再监听其他文件扩展名**

```gow -e=go,mod,html run [.]```

# SYNOPSIS

**gow** [_flags_] _command_ [_args_]

# PARAMETERS

_COMMAND_
> 要包装并重新运行的任意 go 子命令（run、test、build、vet 等）。

**-c**
> 每次重启前清空终端。

**-e** _ext,ext,..._
> 要监听的文件扩展名。默认：go。

**-v**
> 详细输出，打印每次重启的触发原因。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gow**（"go watch"）的调用方式与 **go** 完全相同，但会额外监听 Go 源码树，并在任何被监听的文件发生变化时重新运行给定命令。它透明地包装 go run、go test、go build 等子命令，默认忽略非 Go 文件。

它使用递归的、事件驱动的监听器（不轮询），因此重启几乎是即时的；它会在两次运行之间清除残留输出，还支持诸如 **ctrl+r** 强制重启之类的快捷键。

# CAVEATS

仅限开发用途；不适合用于生产环境的进程守护。默认从当前目录开始递归监听。

# HISTORY

gow 由 **Nelo Mitranim** 创建，作为其早期 **gorun** 工具的轻量替代品，为 Go 开发工作流添加了更好的文件监听器和快捷键支持。

# INSTALL

```nix: nix profile install nixpkgs#gow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1), [air](/man/air)(1), [goreload](/man/goreload)(1)

# RESOURCES

```[Source code](https://github.com/mitranim/gow)```

<!-- verified: 2026-07-17 -->
