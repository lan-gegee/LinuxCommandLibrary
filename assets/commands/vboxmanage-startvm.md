# TAGLINE

启动 VirtualBox 虚拟机

# TLDR

**以 GUI 启动虚拟机**（默认）

```vboxmanage startvm [vmname]```

**无界面启动**（不显示窗口，用于远程显示）

```vboxmanage startvm [vmname] --type headless```

**以可分离的独立前端启动**

```vboxmanage startvm [vmname] --type separate```

**通过 UUID 启动虚拟机**

```vboxmanage startvm [670e746d-abea-4ba6-ad02-2a3b043810a5]```

**启动时设置环境变量**

```vboxmanage startvm [vmname] --putenv "[DISPLAY=:0.0]"```

# SYNOPSIS

**vboxmanage** **startvm** _vmname|uuid_ [**--type** _type_] [**--putenv** _name_=_value_]

# PARAMETERS

**--type** _type_
> 前端类型：gui（默认，显示窗口）、headless（无窗口，仅远程显示）、separate（可分离的 UI）。

**--putenv** _name_=_value_
> 为虚拟机进程设置环境变量。

# DESCRIPTION

**vboxmanage startvm** 启动当前处于关闭（Powered Off）或已保存（Saved）状态的虚拟机。可以通过名称或 UUID 指定虚拟机。支持 GUI 模式（默认）、headless（无窗口）和 separate（可分离 GUI）。服务器型虚拟机建议使用 headless。

# SEE ALSO

[vboxmanage](/man/vboxmanage)(1), [vboxmanage-controlvm](/man/vboxmanage-controlvm)(1), [vboxmanage-list](/man/vboxmanage-list)(1), [vboxmanage-showvminfo](/man/vboxmanage-showvminfo)(1)
