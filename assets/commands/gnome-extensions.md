# TAGLINE

GNOME Shell 扩展管理器

# TLDR

**列出**所有已安装的扩展

```gnome-extensions list```

显示特定扩展的**信息**

```gnome-extensions info "[extension_id]"```

**启用**特定扩展

```gnome-extensions enable "[extension_id]"```

**禁用**特定扩展

```gnome-extensions disable "[extension_id]"```

**卸载**特定扩展

```gnome-extensions uninstall "[extension_id]"```

显示特定子命令的**帮助**

```gnome-extensions help [subcommand]```

显示**版本**

```gnome-extensions version```

# SYNOPSIS

**gnome-extensions** _command_ [_options_]

# PARAMETERS

**list**
> 列出已安装的扩展（--user 仅限用户级，--enabled 仅限已启用）

**info** _UUID_
> 显示某个扩展的信息

**enable** _UUID_
> 启用某个扩展

**disable** _UUID_
> 禁用某个扩展

**uninstall** _UUID_
> 移除某个扩展

**create**
> 从模板创建新扩展

**pack**
> 打包扩展以便分发

**install** _BUNDLE_
> 从 bundle 文件安装扩展

**prefs** _UUID_
> 打开扩展的偏好设置窗口

# DESCRIPTION

**gnome-extensions** 是用于管理 GNOME Shell 扩展的命令行工具。扩展可以修改 GNOME Shell 的行为和外观，添加诸如系统监视器、窗口平铺或自定义主题等功能。

扩展由 UUID 标识，例如 **dash-to-dock@micxgx.gmail.com**。它们安装在 **~/.local/share/gnome-shell/extensions/**（用户级）或 **/usr/share/gnome-shell/extensions/**（系统级）中。

# CAVEATS

扩展可能导致 GNOME Shell 不稳定或崩溃。每个新的 GNOME Shell 版本都要求扩展相应更新。禁用有问题的扩展可能需要注销或使用 TTY。

# HISTORY

gnome-extensions 于 GNOME 3.34（**2019** 年）推出，作为旧工具 gnome-shell-extension-tool 的现代化替代。GNOME Shell 扩展本身自 **2011** 年的 GNOME 3.0 起就已可用。

# INSTALL

```apt: sudo apt install gnome-shell```

```dnf: sudo dnf install gnome-shell```

```pacman: sudo pacman -S gnome-shell```

```apk: sudo apk add gnome-shell```

```zypper: sudo zypper install gnome-shell```

```nix: nix profile install nixpkgs#gnome-shell```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dconf](/man/dconf)(1)
