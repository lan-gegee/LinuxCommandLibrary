# TAGLINE

管理 Wake-on-LAN 设备的 TUI 工具

# TLDR

**启动 Wake-on-LAN TUI**

```wakey```

# SYNOPSIS

**wakey**

# DESCRIPTION

**wakey** 是一个用于管理和唤醒设备的终端用户界面，基于 Wake-on-LAN。它让你将设备组织为分组、发送魔术包唤醒机器，并 ping 设备以检查其在线/离线状态。

按键绑定：**Tab** 在设备视图和分组视图之间切换，**n** 新增设备或分组，**e** 编辑，**d** 删除，**Enter** 唤醒设备或分组，**r** 刷新状态，方向键或 vim 移动键导航，**Ctrl+H** 显示全部按键绑定。

配置存储在 **~/.wakey_config.json** 中，包含设备条目（名称、MAC 地址、IP 地址）和分组。

# CAVEATS

目标设备必须启用 Wake-on-LAN。需要网络访问权限才能发送魔术包。

# HISTORY

**wakey** 由 **Jonathan Ruiz**（jonathanruiz）创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S wakey```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wakeonlan](/man/wakeonlan)(1), [etherwake](/man/etherwake)(1), [wol](/man/wol)(1)
