# TAGLINE

根据 `/etc/locale 编译本地化（locale）定义

# TLDR

从 /etc/locale.gen **生成** locale

```sudo locale-gen```

生成时**保留已有** locale

```sudo locale-gen --keep-existing```

# SYNOPSIS

**locale-gen** [_options_]

# DESCRIPTION

**locale-gen** 将 `/etc/locale.gen` 中的 locale 定义编译为二进制 locale 数据。运行该命令前，需要先在该文件中取消注释所需的 locale。

# PARAMETERS

**--keep-existing**
> 不删除已有的 locale 数据

**--purge**
> 生成前移除已有的 locale

# CAVEATS

需要 root 权限。生成前先编辑 `/etc/locale.gen` 以启用所需 locale。基于 Debian 的系统可使用 `dpkg-reconfigure locales` 进行交互式配置。

# SEE ALSO

[locale](/man/locale)(1), [localedef](/man/localedef)(1), [localectl](/man/localectl)(1)
