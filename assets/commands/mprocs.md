# TAGLINE

并行运行多条命令并分别显示各自的输出

# TLDR

**运行 mprocs.yaml 中定义的命令**

```mprocs```

**运行指定的命令**

```mprocs "[command1]" "[command2]"```

**使用指定的配置文件**

```mprocs --config [path/to/config.yaml]```

# SYNOPSIS

**mprocs** [_options_] [_commands_...]

# DESCRIPTION

**mprocs** 并行运行多条命令，并在 TUI 中分别显示每条命令的输出。它专为开发过程中反复运行的命令而设计，例如编译器、测试运行器和开发服务器。

每个进程都在自己的窗口中运行，你可以直接与进程交互（包括在 mprocs 内使用 vim 等编辑器）。与 tmux 不同，当 mprocs 结束时，它管理的所有进程也会随之结束。

# CONFIGURATION

**~/.config/mprocs/mprocs.yaml**
> 全局配置，用于按键绑定和默认值。

**mprocs.yaml**
> 本地项目配置，定义要运行的进程。

# CAVEATS

mprocs 退出时进程会被终止。它并不打算替代 tmux 或 screen 来维持长时间会话。

# HISTORY

**mprocs** 由 **pvolok** 创建，使用 **Rust** 编写。

# INSTALL

```apk: sudo apk add mprocs```

```brew: brew install mprocs```

```nix: nix profile install nixpkgs#mprocs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [screen](/man/screen)(1), [foreman](/man/foreman)(1)
