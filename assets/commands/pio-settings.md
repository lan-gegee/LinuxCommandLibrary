# TAGLINE

管理 PlatformIO 配置设置

# TLDR

**显示所有设置**

```pio settings get```

**获取特定设置**

```pio settings get [projects_dir]```

**设置选项值**

```pio settings set [projects_dir] [~/pio-projects]```

**恢复默认设置**

```pio settings reset```

# SYNOPSIS

**pio settings** _command_ [_options_]

# PARAMETERS

**get** [_name_]
> 获取设置值。

**set** _name_ _value_
> 设置设置项的值。

**reset**
> 恢复默认设置。

# DESCRIPTION

**pio settings** 用于管理 PlatformIO 配置设置，控制默认目录、自动更新、遥测以及其他全局偏好。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio-system](/man/pio-system)(1), [pio-account](/man/pio-account)(1)
