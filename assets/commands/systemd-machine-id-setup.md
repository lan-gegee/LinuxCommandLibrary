# TAGLINE

初始化机器 ID

# TLDR

**初始化** /etc/machine-id 中的机器 ID

```sudo systemd-machine-id-setup```

**打印**设置完成后生成或提交的机器 ID

```sudo systemd-machine-id-setup --print```

**将**瞬态机器 ID **提交**到磁盘上的持久存储

```sudo systemd-machine-id-setup --commit```

**操作**指定的根目录

```sudo systemd-machine-id-setup --root /[path/to/root]```

**操作**磁盘镜像

```sudo systemd-machine-id-setup --image /[path/to/image]```

# SYNOPSIS

**systemd-machine-id-setup** [_options_]

# PARAMETERS

**--print**
> 在设置操作完成后打印机器 ID

**--commit**
> 将瞬态机器 ID 提交到磁盘持久存储。若 /etc/machine-id 并非从内存挂载，或 /etc/ 为只读，则此选项无效。主要由 systemd-machine-id-commit.service 使用

**--root _path_**
> 操作指定的根目录而非真实根目录。包括 /etc/machine-id 在内的所有路径都会加上给定路径前缀

**--image _path_**
> 操作指定的磁盘镜像（设备节点或普通文件）而非目录树

**--image-policy _policy_**
> 使用 --image 时指定镜像挂载策略字符串。默认为 "*" 策略（使用所有可识别的文件系统）

**-h**, **--help**
> 显示简短帮助并退出

**--version**
> 显示版本信息并退出

# DESCRIPTION

**systemd-machine-id-setup** 初始化存储在 **/etc/machine-id** 中的机器 ID。它面向系统安装工具在安装阶段使用，或在 /etc/machine-id 为空或缺失时使用。

在不带 **--commit** 调用时，该工具按以下顺序使用第一个可用的来源来初始化机器 ID：

1. 来自 /run/machine-id 的有效 ID
2. 已存在的 D-Bus 机器 ID
3. 来自 system.machine_id 凭据的机器 ID
4. 来自 KVM 虚拟机配置的 UUID
5. 来自容器环境配置的 UUID
6. 兜底方案：新生成的随机 ID

**--commit** 选项用于把瞬态机器 ID（早期启动时挂载到内存中）转换为写入磁盘的持久机器 ID。

# CAVEATS

需要 root 权限。只应在系统安装期间或 **/etc/machine-id** 缺失或为空时运行一次。更改机器 ID 可能破坏依赖它进行稳定标识的服务。本命令是 systemd 套件的一部分。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-id128](/man/systemd-id128)(1), [machine-id](/man/machine-id)(5), [systemd-firstboot](/man/systemd-firstboot)(1)
