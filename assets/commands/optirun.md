# TAGLINE

Bumblebee 项目用于在 NVIDIA Optimus 笔记本上运行应用程序的工具

# TLDR

**使用 NVIDIA GPU 运行应用**

```optirun [application]```

**以指定选项运行**

```optirun -b [primus] [application]```

**检查 GPU 状态**

```optirun --status```

**以详细模式运行**

```optirun -vvv [application]```

**强制开启 GPU 电源**

```optirun --no-xorg [glxinfo]```

# SYNOPSIS

**optirun** [_options_] _command_ [_args_...]

# PARAMETERS

**-b**, **--bridge** _method_
> 渲染桥（virtualgl、primus）。

**-c** _file_
> 配置文件。

**--no-xorg**
> 不启动辅助 X 服务器。

**--status**
> 检查 Bumblebee 状态。

**-v**
> 详细输出。

**-q**
> 静默模式。

# DESCRIPTION

**optirun** 是 Bumblebee 项目用于在 NVIDIA Optimus 笔记本上运行应用程序的工具。它允许选择性地使用独立 NVIDIA GPU，同时由集成 GPU 负责显示输出。

Bumblebee 会管理 GPU 电源，在不需要独立 GPU 时节省电池电量。

# BRIDGES

```
virtualgl - VirtualGL bridge
primus    - Faster, lower latency
```

# CAVEATS

需要 Bumblebee 守护进程。替代方案：NVIDIA PRIME。可能存在兼容性问题。正在被原生 PRIME 取代。

# HISTORY

Bumblebee 是为 NVIDIA Optimus 笔记本而生的 Linux 解决方案——该硬件在 **2011 年**推出时缺乏官方 Linux 支持。

# INSTALL

```apt: sudo apt install bumblebee```

```pacman: sudo pacman -S bumblebee```

```zypper: sudo zypper install bumblebee```

```brew: brew install bumblebee```

```nix: nix profile install nixpkgs#bumblebee```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nvidia-settings](/man/nvidia-settings)(1)
