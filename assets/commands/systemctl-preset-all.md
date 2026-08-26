# TAGLINE

将所有单元重置为预设默认值

# TLDR

将**所有**单元重置为预设默认值

```sudo systemctl preset-all```

仅**启用**模式

```sudo systemctl preset-all --preset-mode enable-only```

仅**禁用**模式

```sudo systemctl preset-all --preset-mode disable-only```

**安静**模式

```sudo systemctl preset-all -q```

# SYNOPSIS

**systemctl preset-all** [_OPTIONS_]

# PARAMETERS

**--preset-mode=** _MODE_
> full（默认）、enable-only 或 disable-only

**-q, --quiet**
> 不输出内容，仅返回退出码

**--user**
> 操作用户单元

# DESCRIPTION

**systemctl preset-all** 将所有已安装单元文件的启用状态重置为预设策略文件中定义的默认值。这会将发行版的默认设置应用到系统上的每一个单元。

通常在系统初次安装后运行一次，或在需要恢复到发行版默认设置时运行。

# CAVEATS

这是一种影响整个系统的操作，可能改变许多服务的启用状态。可使用 `--preset-mode` 将范围限制为只启用或只禁用。运行前请备份当前配置。

# HISTORY

**preset-all** 子命令提供了一种将整个系统重置为发行版默认服务配置的方式，适用于恢复或标准化场景。

# SEE ALSO

[systemctl-preset](/man/systemctl-preset)(1), [systemctl-enable](/man/systemctl-enable)(1)
