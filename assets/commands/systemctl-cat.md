# TAGLINE

显示 systemd unit 文件内容

# TLDR

显示 **unit 文件**内容

```systemctl cat [unit]```

显示**多个** unit 文件

```systemctl cat [unit1 unit2 ...]```

显示**模板** unit 文件

```systemctl cat [template@]```

显示**用户级** unit 文件

```systemctl cat [unit] --user```

# SYNOPSIS

**systemctl cat** _PATTERN_...

# PARAMETERS

**--user**
> 查询调用用户的 **systemd --user** 管理器，而非系统管理器。

**--system**
> 查询系统管理器（默认）。

**--no-pager**
> 不将输出通过管道传给分页器。

**--root=**_PATH_
> 从另一个文件系统根读取 unit 文件（用于检查 chroot 或已挂载的镜像）。

**--image=**_PATH_
> 从 _PATH_ 处的磁盘镜像文件读取 unit 文件。

**-M**, **--machine=**_NAME_
> 在指定名称的容器或虚拟机内对 systemd 管理器执行操作。

**-l**, **--full**
> 不省略显示的路径。

# DESCRIPTION

**systemctl cat** 按 systemd 所见的完整内容显示 unit 文件，包括主 unit 文件和所有 drop-in 覆盖文件。它会在每个文件的内容之前显示其绝对路径。

这对调试 unit 配置很有用，尤其是当 `.d/` 目录中的 drop-in 文件修改了基础 unit 时。

# CAVEATS

显示的是原始文件内容，而非解析后的有效配置。要查看实际的运行时值，请使用 `systemctl show`。模板 unit 应带尾部 @ 符号指定。

# HISTORY

**cat** 子命令是 **systemd** 项目中 **systemctl** 的一部分。它提供了一种便捷方式来检查 unit 配置，无需在多个目录中手动定位文件。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-edit](/man/systemctl-edit)(1), [systemctl-show](/man/systemctl-show)(1)
