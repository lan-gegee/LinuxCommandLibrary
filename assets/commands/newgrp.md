# TAGLINE

将当前实际组 ID 更改为指定的组

# TLDR

**切换**到另一个主组

```newgrp [group_name]```

**切换**组并以登录 shell 的方式重新初始化环境

```newgrp - [group_name]```

**重置**为默认主组

```newgrp```

权限被拒后**用 sudo 重跑上一条命令**（常见模式）

```sudo newgrp [group_name]```

# SYNOPSIS

**newgrp** [**-**] [_group_]

# PARAMETERS

**-**
> 像用户重新登录一样重新初始化环境

**group**
> 要切换到的组名；必须是该组成员或知道组密码

# DESCRIPTION

**newgrp** 将当前实际组 ID 更改为指定的组，并尝试将该组加入用户的组集合。如果提供了连字符，环境会像登录 shell 一样被重新初始化。运行 newgrp 之后创建的文件将以新组作为属主组。

如果不是 root，当用户没有密码而组有密码，或用户未列为组成员且该组设有密码时，系统会提示输入密码。若组密码为空且用户不在成员列表中，访问将被拒绝。如果未指定组，则切换为 /etc/passwd 中列出的默认组。

# CAVEATS

该命令会启动一个已更改组的新 shell，原 shell 的组保持不变。组密码很少使用且被认为不安全。此更改仅影响新 shell 及其子进程。

# HISTORY

**newgrp** 是标准 POSIX 命令，自早期 Unix 版本起就已存在。它提供了一种无需注销再登录即可临时切换组上下文的方式。

# INSTALL

```apt: sudo apt install login```

```apk: sudo apk add util-linux-login```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[groups](/man/groups)(1), [id](/man/id)(1), [sg](/man/sg)(1), [gpasswd](/man/gpasswd)(1), [chgrp](/man/chgrp)(1)
