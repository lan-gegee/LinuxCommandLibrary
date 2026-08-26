# TAGLINE

OpenWrt 统一配置接口

# TLDR

**获取**一个值

```uci get [network.lan.ipaddr]```

**显示**所有选项

```uci show [network]```

**设置**一个值

```uci set [config].[section].[option]=[value]```

**添加**新节

```uci add [config] [section]```

**删除**节或选项

```uci delete [config].[section].[option]```

**提交**更改

```uci commit [config]```

**撤销**未提交的更改

```uci revert [config]```

**向列表型选项添加值**

```uci add_list [network.lan.dns]=[8.8.8.8]```

**显示待生效的更改**

```uci changes```

# SYNOPSIS

**uci** _COMMAND_ [_ARGUMENTS_...]

# COMMANDS

**get** _CONFIG.SECTION.OPTION_
> 获取一个值

**show** [_CONFIG_]
> 列出所有选项和值

**set** _CONFIG.SECTION.OPTION=VALUE_
> 设置配置值

**add** _CONFIG_ _SECTION_
> 添加新的匿名节

**delete** _CONFIG.SECTION[.OPTION]_
> 删除节或选项

**rename** _CONFIG.SECTION[.OPTION]=NAME_
> 重命名节或选项

**add_list** _CONFIG.SECTION.OPTION=VALUE_
> 向列表型选项添加一个值

**del_list** _CONFIG.SECTION.OPTION=VALUE_
> 从列表型选项中移除一个值

**commit** [_CONFIG_]
> 将更改写入配置文件

**revert** _CONFIG_
> 丢弃未提交的更改

**changes** [_CONFIG_]
> 显示尚未提交的待生效更改

**export** [_CONFIG_]
> 以机器可读格式导出配置

# DESCRIPTION

**uci**（Unified Configuration Interface，统一配置接口）管理 OpenWrt 的配置文件。它提供标准化的方式来读写 OpenWrt 中普遍使用的 UCI 配置格式。

配置文件存储在 **/etc/config/** 中，按文件、节、选项三个层级组织。更改会先暂存在临时位置，必须提交后才能生效。revert 命令可丢弃未提交的更改。

# CAVEATS

OpenWrt 专用。更改需要 commit 才会生效。部分服务在配置更改后需要重启。无效的配置可能导致网络无法访问。

# HISTORY

**UCI** 为 **OpenWrt** 开发，旨在为所有系统服务提供一致的配置界面，简化嵌入式路由器和设备的管理。

# INSTALL

```nix: nix profile install nixpkgs#uci```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ubus](/man/ubus)(1), [opkg](/man/opkg)(1)
