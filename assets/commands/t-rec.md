# TAGLINE

速度极快的终端录制器，可生成动画 GIF

# TLDR

**录制当前终端会话**

```t-rec```

**同时生成 GIF 和 MP4 输出**

```t-rec --video```

使用特定 shell 录制并添加投影效果

```t-rec -d shadow /bin/sh```

# SYNOPSIS

**t-rec** [_options_] [_shell_]

# PARAMETERS

**--video**
> 同时生成 GIF 和 MP4 输出。

**-d** _DECOR_
> 应用装饰效果（如阴影）。

# DESCRIPTION

**t-rec** 捕获终端会话并将其转换为动画 GIF 图像或 MP4 视频。它具备智能空闲帧检测以优化文件体积、可配置的帧率、可选的投影等装饰效果，并且可以录制任意窗口。完全离线运行，支持 macOS、Linux 和 NetBSD。

# HISTORY

**t-rec** 由 **Sven Assmann**（sassman）创建，采用 **Rust** 编写。

# INSTALL

```brew: brew install t-rec```

```nix: nix profile install nixpkgs#t-rec```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[asciinema](/man/asciinema)(1), [vhs](/man/vhs)(1), [terminalizer](/man/terminalizer)(1)
