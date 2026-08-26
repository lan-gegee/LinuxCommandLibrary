# TAGLINE

以树形递归显示控制组内容

# TLDR

**显示整个控制组层级**

```systemd-cgls```

**显示特定控制器的 cgroup 树**

```systemd-cgls [cpu|memory|io]```

**显示特定单元的控制组层级**

```systemd-cgls -u [unit1] [unit2]```

**显示包括空组在内的所有控制组**

```systemd-cgls --all```

**显示时不截断进程名称**

```systemd-cgls -l```

# SYNOPSIS

**systemd-cgls** [_options_] [_cgroup_...]

# PARAMETERS

**-u**, **--unit** _UNIT_
> 显示指定 systemd 单元的 cgroup 子树。

**-a**, **--all**
> 显示所有控制组，包括不包含任何进程的空组。

**-l**, **--full**
> 不省略（截断）进程树条目。

**-k**
> 在输出中包括内核线程。

**--no-pager**
> 不将输出送入分页器。

**-M**, **--machine** _CONTAINER_
> 显示指定容器中的控制组内容。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**systemd-cgls** 以树形格式递归显示 Linux 控制组（cgroup）层级的内容。它展示哪些进程属于哪些控制组，并按 systemd 的 slice、scope 和 service 组织。

如果指定了参数，则显示指定控制组的所有成员进程及其子组。如果不带参数且当前工作目录位于 **/sys/fs/cgroup/** 之下，则显示该 cgroup 的内容。否则会显示完整的 systemd 控制组层级。

该工具以清晰的视觉方式呈现 cgroup 嵌套结构和进程，有助于理解 systemd 如何组织进程以及调试资源管理问题。

# CAVEATS

需要挂载 cgroups（v1 或 v2）。默认隐藏空的控制组，除非使用 **--all**。树形结构反映的是 systemd 单元层级。属于 systemd 工具套件的一部分。

# HISTORY

systemd-cgls 作为 Lennart Poettering 主导的 **systemd** 项目的一部分推出，为 systemd 管理的 cgroup 层级提供了直观的视图。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-cgtop](/man/systemd-cgtop)(1), [systemctl](/man/systemctl)(1), [ps](/man/ps)(1), [cgroups](/man/cgroups)(7)
