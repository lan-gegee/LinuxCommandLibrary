# TAGLINE

编辑 systemd unit 覆盖文件

# TLDR

以**非破坏性方式**叠加修改 unit 文件

```sudo systemctl edit [unit]```

**编辑**完整 unit 文件

```sudo systemctl edit [unit] --full```

**创建**新 unit 文件

```sudo systemctl edit [unit] --full --force```

编辑**用户级** unit 文件

```systemctl edit [unit] --user```

# SYNOPSIS

**systemctl edit** [_OPTIONS_] _UNIT_...

# PARAMETERS

**-l, --full**
> 编辑主 unit 文件，而非创建 drop-in 覆盖文件

**--force**
> 如果 unit 文件不存在则创建新文件（与 --full 配合）

**--user**
> 编辑用户级 unit 文件

**--system**
> 编辑系统级 unit 文件（默认）

**--runtime**
> 使更改临时生效（重启后清除）

# DESCRIPTION

**systemctl edit** 打开文本编辑器来修改 systemd unit 文件。默认情况下，它会在 `/etc/systemd/system/<unit>.d/override.conf` 创建一个 drop-in 覆盖文件，在不直接修改原 unit 的情况下对其进行扩展。

使用 `--full` 时，会打开整个 unit 文件进行编辑。配合 `--full --force` 可以创建新的 unit 文件。编辑后 systemd 会自动重载配置。所用的编辑器由 `SYSTEMD_EDITOR`、`EDITOR` 或 `VISUAL` 环境变量决定。

# CAVEATS

Drop-in 文件只能添加或覆盖特定设置，无法移除现有配置。编辑后守护进程会自动重载，但运行中的 unit 可能需要手动重启。unit 文件的语法错误可能导致服务无法启动。

# HISTORY

**edit** 子命令加入 **systemctl** 是为了简化 unit 的自定义。Systemd 由 **Lennart Poettering** 和 **Kay Sievers** 在 Red Hat 创建，自 **2015 年**起成为多数主流 Linux 发行版的默认 init 系统。drop-in 覆盖模式允许在软件包更新后依然保留的安全自定义。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-revert](/man/systemctl-revert)(1)
