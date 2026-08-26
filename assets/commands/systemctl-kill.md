# TAGLINE

向单元的进程发送信号

# TLDR

向单元发送 **SIGTERM**

```systemctl kill [unit]```

发送**指定信号**

```systemctl kill -s [SIGNAL] [unit]```

只向**主进程**发送信号

```systemctl kill --kill-whom=main -s SIGHUP [unit]```

终止某个**用户**服务的进程

```systemctl --user kill [unit]```

# SYNOPSIS

**systemctl kill** [_OPTIONS_] _PATTERN_...

# PARAMETERS

**-s, --signal=** _SIGNAL_
> 要发送的信号（名称或编号，默认：SIGTERM）

**--kill-whom=** _WHO_
> 要杀掉哪些进程：main、control 或 all（默认：all）。较旧的 systemd 版本使用 `--kill-who`。

**--user**
> 终止用户服务的进程

# DESCRIPTION

**systemctl kill** 向一个单元的一个或多个进程发送信号。默认情况下，它会向该单元 cgroup 中的所有进程发送 SIGTERM。这比 `systemctl stop` 提供更精细的控制，后者会遵循单元配置的停止行为。

`--kill-whom` 选项控制哪些进程接收信号：main（主进程）、control（控制进程）或 all（cgroup 中的每个进程）。

# CAVEATS

会绕过单元配置的 ExecStop 命令。终止主进程后，子进程是否变成孤儿取决于单元的配置。SIGKILL 无法被进程捕获或忽略。

# HISTORY

**kill** 子命令提供向单元进程直接发送信号的能力，适用于正常停止流程不够用或需要特定信号的场景（例如用 SIGHUP 重新加载配置）。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-stop](/man/systemctl-stop)(1), [systemctl-restart](/man/systemctl-restart)(1), [kill](/man/kill)(1)
