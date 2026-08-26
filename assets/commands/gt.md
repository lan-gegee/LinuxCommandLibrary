# TAGLINE

基于 configfs 的 USB gadget 管理工具

# TLDR

**列出可用的 USB 设备控制器（UDC）**

```gt udc```

**列出现有的 gadget**

```gt gadget```

**创建新的 gadget**

```gt create [gadget-name]```

**设置 gadget 属性**（厂商/产品 ID）

```gt set [gadget-name] idVendor=[0x1d6b] idProduct=[0x0104]```

**创建 USB 功能**（如以太网）

```gt func create [gadget-name] [ecm] [usb0]```

**创建配置并将功能绑定到其中**

```gt config create [gadget-name] [c] [1]```

```gt config add [gadget-name] [c] [1] [ecm] [usb0]```

**在第一个可用的 UDC 上启用 gadget**

```gt enable [gadget-name]```

**将当前 gadget 设置保存为可复用的模板**

```gt save [gadget-name] [template-name]```

**移除 gadget 及其所有配置/功能**

```gt rm -rf [gadget-name]```

# SYNOPSIS

**gt** _command_ [_options_...]

**gadgetctl** _command_ [_options_...]

# PARAMETERS

_COMMAND_
> 要执行的子命令（见下文）。

**udc**
> 显示可用的 USB 设备控制器列表。

**create** _gadget_ [_attr=val_...]
> 创建具有给定名称的 gadget，可选设置其属性。`-f`/`--force` 会覆盖同名 gadget。

**rm** _gadget_
> 移除 gadget。`-f`/`--force` 会先禁用处于启用状态的 gadget；`-r`/`--recursive` 还会移除其配置和功能。

**get** _gadget_ [_attr_]
> 打印给定的属性；未指定时打印所有属性。

**set** _gadget_ _attr=val_...
> 将一个或多个 gadget 属性设置为新值。

**enable** [_gadget_]
> 在 UDC 上启用 gadget。若只存在一个 gadget/UDC 则自动选择。

**disable** [_gadget_]
> 禁用 gadget。`-u`/`--udc` _udc_ 可禁用在给定 UDC 上活动的任意 gadget。

**gadget** [_name_]
> 列出所有 gadget 或显示某个 gadget 的详情。`-v`/`--verbose` 同时打印属性；`-r`/`--recursive` 还显示功能/配置详情。

**func create/rm/show** _gadget_ _type_ _instance_
> 创建、移除或显示绑定到 gadget 的 USB 功能（如 **ecm**、**acm**、**mass_storage**）。

**func list-types**
> 打印当前内核支持的功能类型列表。

**config create/rm/show** _gadget_ _label_ _id_
> 创建、移除或显示 gadget 配置。

**config add/del** _gadget_ _label_ _id_ _func-type_ _func-instance_
> 将功能绑定到配置或解除绑定。

**save** _gadget_ [_name_]
> 将 gadget 当前的设置保存为系统模板。`--file`、`--stdout` 和 `--path` 可以改变保存位置。

**load** _name_ [_gadget_]
> 从保存的模板创建并启用 gadget。`-o`/`--off` 跳过启用步骤。

**template** [_name_]
> 列出模板，或显示某个模板的配置和功能。

**settings set/get/append/detach** _variable_ [_value_]
> 管理 gt 自身的配置变量（其中一些变量持有列表值）。

# DESCRIPTION

**gt**（gadget-tool）通过内核的 **configfs** 接口配置 Linux USB gadget，用一小组子命令取代对 configfs 树的手工 `mkdir`/`echo` 操作。它由**功能**（function，如以太网、大容量存储、串口、HID）组成 gadget，这些功能被归入一个或多个**配置**（configuration），随后在 USB 设备控制器（UDC）上启用。

**gt** 直接操作 configfs，因此需要 root 权限。配套的二进制程序 **gadgetctl** 使用相同的命令语法与 **gadgetd** 守护进程通信，但 gadgetd 已被视为过时。

# CAVEATS

需要 root 权限以及启用了 USB gadget/configfs 支持的内核（`CONFIGFS_FS`、`USB_CONFIGFS` 以及相关的功能驱动）；可用的功能类型取决于当前运行的内核。主要用于嵌入式开发板和带 USB 设备模式控制器的设备，而非典型的桌面硬件。

# INSTALL

```apt: sudo apt install genometools```

```dnf: sudo dnf install gt```

```apk: sudo apk add gadget-tool```

```brew: brew install genometools```

```nix: nix profile install nixpkgs#gt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(8), [lsusb](/man/lsusb)(8), [modprobe](/man/modprobe)(8)

# RESOURCES

```[Source code](https://github.com/linux-usb-gadgets/gt)```

<!-- verified: 2026-07-17 -->
