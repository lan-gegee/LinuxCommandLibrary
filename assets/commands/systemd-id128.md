# TAGLINE

生成并打印 128 位标识符

# TLDR

**生成**新的随机标识符

```systemd-id128 new```

**打印**当前机器的标识符

```systemd-id128 machine-id```

**打印**当前启动的标识符

```systemd-id128 boot-id```

**打印**当前服务调用的标识符

```systemd-id128 invocation-id```

**生成**新标识符并以 UUID 格式打印

```systemd-id128 new --uuid```

**生成**由机器 ID 派生的应用专属 ID

```systemd-id128 machine-id --app-specific [app-id]```

**显示**众所周知的标识符

```systemd-id128 show```

# SYNOPSIS

**systemd-id128** [_options_] _command_

# PARAMETERS

**new**
> 生成新的随机标识符。

**machine-id**
> 打印来自 /etc/machine-id 的机器 ID。

**boot-id**
> 打印当前启动 ID。

**invocation-id**
> 打印服务调用 ID（仅限 systemd 服务）。

**show** [_NAME_|_UUID_...]
> 显示 systemd 的众所周知标识符。

**-u, --uuid**
> 以 UUID 格式（连字符分隔的分组）打印。

**-p, --pretty**
> 生成编程语言代码片段形式的输出。

**-P, --value**
> 只打印标识符的值。

**-a, --app-specific** _APP-ID_
> 通过对机器 ID 或启动 ID 与给定的应用 ID 进行哈希运算，生成应用专属 ID。

**--json=**_MODE_
> 以 JSON 格式输出。MODE 可为 short、pretty 或 off。

**--no-pager**
> 禁用分页器输出。

**--no-legend**
> 配合 show 命令使用时省略列标题和页脚。

# DESCRIPTION

**systemd-id128** 生成并打印 systemd 所使用的 sd-id128 标识符。这些 128 位标识符唯一地标识机器、启动和服务调用。

机器 ID 跨重启保持不变，存储在 **/etc/machine-id** 中。启动 ID 每次启动都会变化，用于标识当前的系统会话。调用 ID 则在每次服务启动时都是唯一的。

# CAVEATS

invocation-id 子命令仅在 systemd 服务上下文中有效。机器 ID 在初始设置后不应再更改。UUID 与 RFC 4122 兼容。本命令是 systemd 套件的一部分。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-machine-id-setup](/man/systemd-machine-id-setup)(1), [machine-id](/man/machine-id)(5), [systemctl](/man/systemctl)(1), [uuidgen](/man/uuidgen)(1)
