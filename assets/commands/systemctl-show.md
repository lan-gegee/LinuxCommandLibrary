# TAGLINE

以机器可读格式显示单元属性

# TLDR

显示**管理器**属性

```systemctl show```

显示**用户**管理器属性

```systemctl show --user```

显示**单元**属性

```systemctl show [unit]```

显示**特定**属性

```systemctl show [unit] -p [MainPID,ActiveState]```

只显示特定属性的**值**

```systemctl show [unit] -p [MainPID] --value```

包括**空的**属性

```systemctl show -a [unit]```

# SYNOPSIS

**systemctl show** [_OPTIONS_] [_PATTERN_...|_JOB_...]

# PARAMETERS

**--user**
> 显示用户服务管理器的属性

**-a, --all**
> 包括空属性

**-p, --property=** _NAME_
> 只显示指定的属性

**--value**
> 只打印值，跳过属性名和 "="（配合 -p 使用）

**--no-pager**
> 禁用分页器

# DESCRIPTION

**systemctl show** 以机器可读的格式显示单元、任务或服务管理器自身的属性。不带参数时，显示服务管理器的属性。

输出适合脚本解析。需要人类可读的输出请使用 `systemctl status`。

# COMMON PROPERTIES

**ActiveState** - 当前状态（active、inactive、failed、activating、deactivating）

**LoadState** - 加载状态（loaded、not-found、error、masked）

**SubState** - 更细粒度的状态（running、dead、exited 等）

**MainPID** - 主进程 ID

**ExecMainStartTimestamp** - 启动时间

**Wants、Requires、Conflicts** - 单元依赖属性

**FragmentPath** - 单元文件路径

# CAVEATS

输出格式为 key=value 键值对。某些属性可能为空。需要人类可读的格式请改用 `systemctl status`。

# HISTORY

**show** 子命令提供机器可解析的属性访问方式，支持脚本化查询和监控集成。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl-status](/man/systemctl-status)(1), [systemctl-set-property](/man/systemctl-set-property)(1), [systemctl](/man/systemctl)(1)
