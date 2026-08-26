# TAGLINE

显示每日消息（message of the day）

# TLDR

**显示每日消息**

```session optional pam_motd.so```

**自定义 motd 位置**

```session optional pam_motd.so motd=/etc/custom_motd```

**多个 motd 文件**

```session optional pam_motd.so motd_dir=/etc/motd.d```

**对非登录 shell 禁用**

```session optional pam_motd.so noupdate```

# SYNOPSIS

**pam_motd.so** [_options_]

# PARAMETERS

**motd=**_FILE_
> MOTD 文件路径。

**motd_dir=**_DIR_
> 包含 MOTD 文件的目录。

**noupdate**
> 不运行 motd 脚本。

# DESCRIPTION

**pam_motd** 是一个 PAM 模块，在用户登录时显示"每日消息"。默认显示 **/etc/motd** 的内容。它还可以运行 motd 目录（例如 **/etc/update-motd.d/**）中的可执行脚本来生成动态消息，展示系统信息、安全更新或自定义公告。

该模块作为 **session** 模块配置在 PAM 服务文件（通常是 **/etc/pam.d/login** 或 **/etc/pam.d/sshd**）中。它总是标记为 **optional**，这样即使 MOTD 无法显示，登录也能成功。

# CAVEATS

**motd_dir** 中的脚本以 root 身份在登录期间运行，因此必须经过仔细审计。长时间运行的脚本会拖慢登录过程。**noupdate** 选项会阻止脚本执行，但仍会显示静态 MOTD 文件。

# SEE ALSO

[pam](/man/pam)(8), [motd](/man/motd)(5)
