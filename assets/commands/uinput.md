# TAGLINE

虚拟输入设备事件写入器

# TLDR

**预览**设备描述（dry-run）

```uinput -p```

合并 **YAML** 设备描述

```sudo uinput -c [path/to/device1.yaml] [path/to/device2.yaml]```

从 **device** 节点合并

```sudo uinput -d [/dev/input/eventX] [/dev/input/eventY]```

# SYNOPSIS

**uinput** [_OPTIONS_]

# PARAMETERS

**-p**
> 输出合并后的 YAML 设备描述并退出（dry-run 预览）。

**-c** _FILE..._
> 将一个或多个 YAML 设备描述文件合并到虚拟设备中。

**-d** _DEVICE..._
> 合并从现有 `/dev/input/event*` 设备节点克隆的能力。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**uinput** 是 Interception Tools 管道的写入端：它从 stdin 读取 `input_event` 记录，并通过一个基于内核 `/dev/uinput` 接口新建的虚拟输入设备分发这些记录。虚拟设备的能力（按键、轴、LED 等）派生自通过 `-c` 传入的 YAML 描述文件，也可以选择通过 `-d` 与从现有设备克隆的能力合并。

典型用法是将它串联在 **udevmon** 和各设备的转换工具（如 **caps2esc**）之后，使重映射后的事件重新注入输入栈，就像它们来自一个普通设备一样。

# CAVEATS

需要 CAP_MKNOD 权限和对 **/dev/uinput** 的写访问权限——通常以 root 运行，或通过授予执行用户访问权限的 udev 规则运行。必须加载 `uinput` 内核模块（`modprobe uinput`）。配置不当的管道可能让系统失去键盘输入；请准备好备用会话。

# INSTALL

```apt: sudo apt install interception-tools```

```pacman: sudo pacman -S interception-tools```

```nix: nix profile install nixpkgs#interception-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[udevmon](/man/udevmon)(1)
