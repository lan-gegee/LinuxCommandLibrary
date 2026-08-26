# TAGLINE

显示 unit 的手册页

# TLDR

显示某个 unit 的**手册**

```systemctl help [unit]```

显示**多个** unit 的手册

```systemctl help [unit1 unit2 ...]```

显示**用户级** unit 的手册

```systemctl help [unit] --user```

不使用**分页器**显示

```systemctl help [unit] --no-pager```

显示某个 **PID** 所属 unit 的手册

```systemctl help [pid]```

# SYNOPSIS

**systemctl help** _PATTERN_...|_PID_...

# PARAMETERS

**--user**
> 显示用户级 unit 的帮助

**--no-pager**
> 一次性显示所有输出，不分页

# DESCRIPTION

**systemctl help** 显示一个或多个 unit 的手册页。如果提供的是数字 PID 而非 unit 名称，则显示该进程所属 unit 的手册。

手册页由 unit 文件中的 `Documentation=` 指令决定。

# CAVEATS

并非所有 unit 都有相关文档。必须在 unit 文件中设置 Documentation= 指令才能生效。如果不存在特定手册，会回退到通用的 systemd 文档。

# HISTORY

**help** 子命令将文档访问直接集成到 unit 管理界面中，把 unit 与其相关手册页关联起来。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-cat](/man/systemctl-cat)(1), [man](/man/man)(1)
