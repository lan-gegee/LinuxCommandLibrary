# TAGLINE

管理系统扩展镜像

# TLDR

**显示当前合并状态**

```systemd-sysext status```

**列出**已安装的扩展镜像

```systemd-sysext list```

将扩展**合并**到 /usr 和 /opt

```systemd-sysext merge```

**取消合并**所有扩展

```systemd-sysext unmerge```

**刷新**（先取消合并再合并）

```systemd-sysext refresh```

合并时忽略版本兼容性检查

```systemd-sysext merge --force```

# SYNOPSIS

**systemd-sysext** [_OPTIONS_] _COMMAND_

# COMMANDS

**status**
> 显示当前合并状态。不带命令调用时的默认行为。

**list**
> 列出已安装的扩展镜像。

**merge**
> 使用 overlayfs 将扩展镜像叠加到 /usr 和 /opt 上。

**unmerge**
> 移除扩展叠加层。

**refresh**
> 先取消合并再合并（在安装或删除镜像后重新加载扩展）。

# PARAMETERS

**--root=** _PATH_
> 相对于指定的根目录进行操作。

**--force**
> 合并时忽略版本不兼容问题。

**--mutable=** _MODE_
> 设置可变性模式（disabled、auto、yes、import、ephemeral、ephemeral-import）。

**--no-reload**
> 合并、取消合并或刷新后不重载守护进程。

**--no-pager**
> 不将输出通过分页器显示。

**--no-legend**
> 不打印列标题和页脚提示。

**--json=** _MODE_
> 以 JSON 格式输出（short、pretty 或 off）。

# DESCRIPTION

**systemd-sysext** 管理系统扩展镜像，这些镜像会将文件叠加到 `/usr/` 和 `/opt/` 上。扩展是只读镜像（DDI 格式），可以在不修改根文件系统的情况下向基础系统添加软件。

扩展存储在 `/var/lib/extensions/` 或 `/run/extensions/` 中，并通过 overlayfs 合并。

# CAVEATS

扩展必须与宿主操作系统版本匹配。基础 /usr 必须是不可变的或只读的，叠加才能生效。更改需要执行 refresh 才会生效。

# HISTORY

**systemd-sysext** 支持模块化的系统组装，以不可变的基础镜像配合分层扩展来添加额外软件。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-confext](/man/systemd-confext)(8), [systemctl](/man/systemctl)(1), [portablectl](/man/portablectl)(1), [machinectl](/man/machinectl)(1)
