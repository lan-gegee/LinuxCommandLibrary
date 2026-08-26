# TAGLINE

列出 libvirt 虚拟机

# TLDR

**列出运行中的域**

```virsh list```

**列出所有域**（包括非活动域）

```virsh list --all```

**列出所有域并带标题列**

```virsh list --all --title```

**仅列出已关闭的域**

```virsh list --state-shutoff```

**列出域并带自启动信息**

```virsh list --all --autostart```

**仅列出域名称**（每行一个）

```virsh list --all --name```

**仅列出非活动域**

```virsh list --inactive```

# SYNOPSIS

**virsh** **list** [_options_]

# PARAMETERS

**--all**
> 包含非活动域。

**--inactive**
> 仅列出非活动（已关闭）的域。

**--state-running**
> 仅列出运行中的域。

**--state-paused**
> 仅列出已暂停的域。

**--state-shutoff**
> 仅列出已关闭的域。

**--state-other**
> 仅列出处于其他状态的域（崩溃、垂死、pmsuspended）。

**--transient**
> 仅列出瞬态域（未持久化定义的域）。

**--title**
> 显示域标题列。

**--autostart**
> 显示自启动状态列。

**--no-autostart**
> 仅列出未配置自启动的域。

**--name**
> 仅显示域名称（每行一个）。

**--uuid**
> 仅显示域 UUID。

**--id**
> 仅显示域 ID。

**--managed-save**
> 显示托管保存状态。

**--with-managed-save**
> 仅列出具托管保存状态的域。

**--without-managed-save**
> 仅列出无托管保存状态的域。

# DESCRIPTION

**virsh list** 显示由 libvirt 管理的虚拟机，包括域 ID、名称和状态。默认只显示运行中的虚拟机；使用 `--all` 可获得包含非活动域在内的完整列表。域 ID 只会分配给运行中的域。

# CAVEATS

域 ID 是动态分配的，每次启动域都会变化。在脚本中请使用域名或 UUID 作为稳定引用。

# INSTALL

```apt: sudo apt install libvirt-clients```

```dnf: sudo dnf install libvirt-client```

```apk: sudo apk add libvirt-client```

```zypper: sudo zypper install libvirt-client```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[virsh](/man/virsh)(1), [virsh-help](/man/virsh-help)(1), [virt-manager](/man/virt-manager)(1)

