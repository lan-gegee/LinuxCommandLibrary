# TAGLINE

配置 SteamOS 链式加载器与内核启动调试

# TLDR

**显示**当前的链式加载器/内核调试状态

```sudo steamos-bootdebug status```

**在启动时启用 GRUB 链式加载器菜单**（可选择 A/B 槽位或编辑内核参数）

```sudo steamos-bootdebug menu```

**启用详细**的链式加载器日志输出到控制台

```sudo steamos-bootdebug verbose```

**禁用**菜单与详细输出（静默启动）

```sudo steamos-bootdebug quiet```

**启用内核调试**输出到控制台（大量内核消息）

```sudo steamos-bootdebug kernel-debug```

**仅为下一次启动启用内核调试**，之后自动还原

```sudo steamos-bootdebug kernel-debug-once```

**恢复**正常的静默内核启动

```sudo steamos-bootdebug kernel-quiet```

**将**链式加载器日志**写入** **EFI** 分区

```sudo steamos-bootdebug log enable```

**显示**磁盘上链式加载器日志的内容

```sudo steamos-bootdebug log show```

# SYNOPSIS

**steamos-bootdebug** _command_ [_image_]

# PARAMETERS

**menu**
> 启用链式加载器启动菜单，允许在启动时编辑 GRUB 和选择 A/B 槽位。

**verbose**
> 将链式加载器日志输出发送到系统控制台。

**quiet**
> 同时禁用菜单和详细控制台输出。

**log enable**
> 将链式加载器日志持久保存到 EFI 系统分区（**/esp**）上的文件。

**log disable**
> 停止将链式加载器日志持久保存到文件系统。

**log show**
> 打印链式加载器日志文件的内容。

**kernel-debug** [_image_]
> 为指定槽位的 _image_（省略时为两者）启用内核调试输出（移除 **quiet** 参数，调试消息显示在控制台上）。

**kernel-debug-once** [_image_]
> **仅在下次启动时**启用内核调试，然后自动还原。

**kernel-quiet** [_image_]
> 恢复标准的静默内核启动。

**status**
> 打印两个槽位当前的调试配置。

# DESCRIPTION

**steamos-bootdebug** 是随 SteamOS 3+ 附带于 **Steam Deck** 的一个小型管理脚本。它提供对 SteamOS **链式加载器**（决定加载两个 A/B 系统映像中哪一个的小型引导加载程序桩）以及写入每个映像的内核命令行的控制。

链式加载器先于 GRUB 运行，通常静默启动活动槽位。**steamos-bootdebug menu** 会将其切换到交互模式，让用户可以编辑 GRUB 条目（用于添加 **systemd.unit=rescue.target**、替代的 **root=** 参数等）。**verbose** 与 **quiet** 切换链式加载器日志是输出到控制台还是被抑制；**log enable**/**disable**/**show** 则将这些日志捕获到 EFI 系统分区中的文件里，便于事后检查。

**kernel-debug**/**kernel-quiet** 系列命令编辑一个或两个 A/B 映像的内核命令行：启用内核调试会移除 **quiet** 参数并开启详细的 printk 输出，对诊断显示、GPU 或存储初始化问题极有价值。**kernel-debug-once** 是最安全的选择——它会在一次启动后自动还原，因此不会意外让系统停留在嘈杂状态。

# CAVEATS

**只读根文件系统**：SteamOS 使用不可变根，因此 **steamos-bootdebug** 写入的是 EFI 系统分区而非 **/etc**。启动菜单会显示在固件选择的显示器上；如果你在连接扩展坞时启动 Steam Deck 又在菜单出现期间断开，菜单可能会在内置屏幕上丢失，此时只能盲操作或重启。可选的 _image_ 参数选择 **A** 或 **B** 槽位——省略时两个槽位都会被修改。

# HISTORY

**steamos-bootdebug** 由 Valve 随 **SteamOS 3** 发布（这是自 **2022 年 2 月**起运行于 Steam Deck 的基于 Arch 的 Linux 发行版）。它是 **steamos-customizations** 脚本家族的一员，这些脚本将标准 Arch 安装适配为 Deck 上使用的只读 A/B 映像模型。

# SEE ALSO

[grub](/man/grub)(8), [steamos-readonly](/man/steamos-readonly)(1), [bootctl](/man/bootctl)(1), [efibootmgr](/man/efibootmgr)(8)
