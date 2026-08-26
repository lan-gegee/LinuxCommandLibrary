# TAGLINE

以 GameMode 优化运行程序，提升游戏性能

# TLDR

在启用 GameMode CPU 与系统优化的情况下**运行程序**

```gamemoderun ./mygame```

通过设置启动选项**从 Steam 运行游戏**

```gamemoderun %command%```

**配合自定义包装器运行**，包装器接收原始命令

```GAMEMODERUNEXEC="env __GL_SYNC_TO_VBLANK=1" gamemoderun ./game```

通过同一个变量**使用混合 GPU 启动器**

```GAMEMODERUNEXEC=optirun gamemoderun ./game```

# SYNOPSIS

**gamemoderun** _program_ [_args_...]

# DESCRIPTION

**gamemoderun** 是一个辅助工具，它在 GameMode 下启动给定的程序。GameMode 是 Linux 上守护进程与库的组合，当游戏或其他性能敏感的应用运行时，它会请求临时性的系统优化（如 CPU governor 调整、I/O 优先级、进程 nice 值、抑制屏保、GPU 性能模式以及可选的自定义脚本）。

其原理是预加载 `libgamemodeauto.so.0`，由它与 `gamemoded` 守护进程通信。这种设计将客户端与守护进程清晰解耦，使游戏可以安全地请求模式而无需硬依赖。

对于未直接集成 GameMode 客户端库的游戏，gamemoderun 是推荐的启动方式。它常用于 Steam 启动选项和桌面启动器中。

# PARAMETERS

gamemoderun 本身不接受任何标志；它通过 `LD_PRELOAD` 在 GameMode 下执行其参数。

**GAMEMODERUNEXEC**
> 环境变量。若设置，gamemoderun 会先运行此命令（或命令前缀），并把原始程序及参数交给它。适用于混合 GPU 包装器（`optirun`、`env DRI_PRIME=1`、NVIDIA prime offload 环境变量）或其他启动辅助工具。GameMode 会注入最终的游戏进程，而不是注入包装器本身。可以全局设置（例如在 `/etc/environment` 中）。

# CAVEATS

GameMode 的优化属于尽力而为，取决于主机配置和权限。在某些系统上，CPU governor 更改可能受限。必须安装并运行守护进程（或可通过用户服务激活），优化才会生效；缺少守护进程时游戏仍能正常启动。

# INSTALL

```dnf: sudo dnf install gamemode```

```pacman: sudo pacman -S gamemode```

```apk: sudo apk add gamemode```

```zypper: sudo zypper install gamemode```

```nix: nix profile install nixpkgs#gamemode```

<!-- packages: 2026-07-22 -->

# RESOURCES

```[Source code](https://github.com/FeralInteractive/gamemode)```

```[Documentation](https://github.com/FeralInteractive/gamemode#requesting-gamemode)```

<!-- verified: 2026-07-11 -->
