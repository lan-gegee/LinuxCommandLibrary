# TAGLINE

Hyprland（动态平铺 Wayland 合成器）的插件管理器

# TLDR

从 Git 仓库**添加**插件

```hyprpm add [git_url]```

**移除**插件

```hyprpm remove [plugin_name]```

**启用**插件

```hyprpm enable [plugin_name]```

**禁用**插件

```hyprpm disable [plugin_name]```

**更新**所有插件

```hyprpm update```

**列出**所有已安装的插件

```hyprpm list```

**强制**执行操作

```hyprpm -f [operation]```

# SYNOPSIS

**hyprpm** [_options_] _command_ [_arguments_]

# PARAMETERS

**add** _URL_
> 从 Git 仓库 URL 添加插件

**remove** _NAME_
> 移除已安装的插件

**enable** _NAME_
> 启用已禁用的插件

**disable** _NAME_
> 禁用已启用的插件

**update**
> 更新并重新构建所有插件

**list**
> 列出所有已安装的插件

**-f**, **--force**
> 强制执行操作，即使正常情况下会失败

# DESCRIPTION

**hyprpm** 是 Hyprland（一款动态平铺 Wayland 合成器）的插件管理器。它负责从 Git 仓库下载、构建、启用和更新 Hyprland 插件。

插件通过边框、动画、工作区修改等合成器增强功能来扩展 Hyprland 的能力。插件针对当前 Hyprland 版本编译，在 Hyprland 更新后可能需要重新构建。

# CAVEATS

插件必须与当前 Hyprland 版本兼容。Hyprland 更新之后，可能需要通过 hyprpm update 重新构建插件。编译插件需要构建工具。

# HISTORY

hyprpm 作为 Hyprland 生态的一部分推出，为合成器插件的管理提供标准化方式。Hyprland 自 **2022 年**起凭借丰富的自定义选项而广受欢迎。

# SEE ALSO

[hyprctl](/man/hyprctl)(1), [hyprpaper](/man/hyprpaper)(1), [hyprland](/man/hyprland)(1)
