# TAGLINE

管理 Cinnamon 桌面的小程序、桌件和扩展

# TLDR

**列出所有已安装的扩展**

```cinnamon-extension-tool --list --extension```

**列出所有已安装的小程序**

```cinnamon-extension-tool --list --applet```

**列出所有已安装的桌件**

```cinnamon-extension-tool --list --desklet```

**按 UUID 启用扩展**

```cinnamon-extension-tool --enable [extension-uuid]```

**按 UUID 禁用扩展**

```cinnamon-extension-tool --disable [extension-uuid]```

**重新加载 Cinnamon Shell**

```cinnamon-extension-tool --reload```

# SYNOPSIS

**cinnamon-extension-tool** [**--list**] [**--enable** _UUID_] [**--disable** _UUID_] [**--reload**] [**--applet**|**--desklet**|**--extension**|**--lnf**]

# DESCRIPTION

**cinnamon-extension-tool** 从命令行管理 Cinnamon "spices"（小程序、桌件、扩展和主题）。它提供列出、启用、禁用和重新加载桌面组件的功能，无需使用图形设置界面。

每个 spice 都由一个唯一的 UUID 标识，可从 **--list** 输出中获取。已启用的项目会标记星号（*）。

# PARAMETERS

**--list**
> 列出指定类型的已安装 spices

**--enable** _UUID_
> 启用具有指定 UUID 的 spice

**--disable** _UUID_
> 禁用具有指定 UUID 的 spice

**--reload**
> 重新加载 Cinnamon Shell

**Spice type selectors:**

**--applet**
> 针对面板小程序

**--desklet**
> 针对桌面小部件（桌件）

**--extension**
> 针对 Shell 扩展

**--lnf**
> 针对观感（look & feel）主题

# CAVEATS

需要正在运行的 Cinnamon 桌面会话才能与之通信。UUID 区分大小写。更改通常立即生效，但某些更改可能需要重新加载 Shell 或注销后生效。

# HISTORY

**cinnamon-extension-tool** 由 Linux Mint 团队于 **Cinnamon 2.4**（2014 年）中引入，用于通过命令行管理 Cinnamon spices，类似于 GNOME 的扩展 CLI 工具。

# SEE ALSO

[cinnamon](/man/cinnamon)(1), [cinnamon-launcher](/man/cinnamon-launcher)(1)
