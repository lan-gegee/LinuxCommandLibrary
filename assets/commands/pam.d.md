# TAGLINE

按服务划分的 PAM 配置目录

# TLDR

**查看 login 的 PAM 配置**

```cat /etc/pam.d/login```

**查看 SSH 的 PAM 配置**

```cat /etc/pam.d/sshd```

**查看 sudo 的 PAM 配置**

```cat /etc/pam.d/sudo```

**查看通用认证配置**

```cat /etc/pam.d/common-auth```

# SYNOPSIS

**/etc/pam.d/** - PAM 配置目录

# DESCRIPTION

**/etc/pam.d/** 包含按服务划分的 PAM 配置文件。每个文件为特定服务（login、sshd、sudo 等）定义认证规则。

这种基于目录的配置方式在现代系统中取代了单一文件的 /etc/pam.conf。

# FILE FORMAT

```
# /etc/pam.d/login
type  control  module  [arguments]

auth      required   pam_securetty.so
auth      required   pam_unix.so
account   required   pam_unix.so
session   required   pam_limits.so
```

# COMMON FILES

```
common-auth     - Shared auth rules
common-account  - Shared account rules
common-password - Password rules
common-session  - Session rules
login           - Console login
sshd            - SSH daemon
sudo            - Sudo command
```

# TYPES

```
auth     - Authentication
account  - Account management
password - Password updates
session  - Session setup/teardown
```

# CAVEATS

配置错误可能把用户锁在系统外。请保留一个备用 root 会话进行测试。通用配置请使用 @include。

# SEE ALSO

[pam](/man/pam)(8), [pam.conf](/man/pam.conf)(5), [pam_unix](/man/pam_unix)(8)
