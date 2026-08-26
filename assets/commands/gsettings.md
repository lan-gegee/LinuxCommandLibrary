# TAGLINE

GNOME 桌面配置命令行界面

# TLDR

**设置**键的值

```gsettings set [org.example.schema] [example-key] [value]```

**获取**键的值

```gsettings get [org.example.schema] [example-key]```

将键**重置**为其架构默认值

```gsettings reset [org.example.schema] [example-key]```

递归显示所有架构、键和**值**

```gsettings list-recursively```

显示**单个架构**中的键和值

```gsettings list-recursively [org.example.schema]```

显示键的**允许取值范围**

```gsettings range [org.example.schema] [example-key]```

显示键的**描述**

```gsettings describe [org.example.schema] [example-key]```

# SYNOPSIS

**gsettings** _command_ [_arguments_]

# PARAMETERS

**get** _SCHEMA_ _KEY_
> 获取键的值

**set** _SCHEMA_ _KEY_ _VALUE_
> 设置键的值（必须符合架构类型）

**reset** _SCHEMA_ _KEY_
> 将键重置为架构默认值

**list-schemas**
> 列出已安装的架构

**list-keys** _SCHEMA_
> 列出架构中的键

**list-recursively** [_SCHEMA_]
> 列出所有设置（可选按架构过滤）

**range** _SCHEMA_ _KEY_
> 显示键的有效取值

**describe** _SCHEMA_ _KEY_
> 显示人类可读的描述

**monitor** _SCHEMA_ [_KEY_]
> 监视更改

# DESCRIPTION

**gsettings** 是 GSettings（GNOME 的配置系统）的命令行界面。它提供经架构校验的 dconf 设置访问方式，确保类型安全和取值有效。

设置按架构组织（如 org.gnome.desktop.interface），其中包含带类型的键。与直接访问 dconf 不同，gsettings 会在应用值之前根据架构进行校验。

# COMMON SCHEMAS

**org.gnome.desktop.interface** - 桌面外观设置
**org.gnome.desktop.wm.preferences** - 窗口管理器偏好
**org.gnome.shell** - GNOME Shell 设置

# CAVEATS

仅适用于使用 GSettings 的应用（主要是 GNOME）。某些设置需要注销或重启才能生效。必须安装相应架构，设置才能工作。

# HISTORY

GSettings 于 GLib 2.26（**2010 年**）中引入，用以取代 GConf。它以 dconf 作为后端，同时提供架构校验，使配置更健壮且可自省。

# INSTALL

```apt: sudo apt install libglib2.0-bin```

```dnf: sudo dnf install glib```

```apk: sudo apk add glib```

```brew: brew install glib```

```nix: nix profile install nixpkgs#glib```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dconf](/man/dconf)(1)
