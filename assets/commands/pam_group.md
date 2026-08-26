# TAGLINE

基于登录上下文授予组访问权限的 PAM 模块

# TLDR

**在 PAM 配置中启用组分配**

```auth required pam_group.so```

**在所有时间向所有用户授予 audio 组**

```echo "* ; * ; * ; Al0000-2400 ; audio" >> /etc/security/group.conf```

**向 tty 设备上的用户授予 video 组**

```echo "* ; tty* ; * ; Al0000-2400 ; video" >> /etc/security/group.conf```

# SYNOPSIS

**pam_group.so**

# PARAMETERS

配置位于 /etc/security/group.conf：

格式：_services_ ; _ttys_ ; _users_ ; _times_ ; _groups_

该模块不接受任何选项。

# DESCRIPTION

**pam_group** 是一个 PAM 模块，在认证的凭据设置阶段授予补充组成员身份。它不对用户进行认证。成员身份根据所访问的服务、终端、用户和登录时间授予，配置位于 /etc/security/group.conf。这些组是在 /etc/group 中已有组之外额外添加的。

# CAVEATS

仅提供 **auth** 模块类型。需要配置 /etc/security/group.conf。一旦获得组成员身份，用户就可能尝试创建 setgid 二进制文件；可使用 **nosuid** 选项挂载文件系统来缓解此风险。

# SEE ALSO

[group.conf](/man/group.conf)(5), [pam](/man/pam)(8), [pam.d](/man/pam.d)(5), [pam_time](/man/pam_time)(8), [pam_unix](/man/pam_unix)(8)
