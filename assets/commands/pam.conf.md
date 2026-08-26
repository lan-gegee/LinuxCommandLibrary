# TAGLINE

旧式 PAM 配置文件格式，所有服务都配置在单个文件中

# TLDR

**基本认证条目**

```login auth required pam_unix.so```

**账户管理条目**

```login account required pam_unix.so```

**会话条目**

```login session required pam_limits.so```

**密码条目**

```login password required pam_unix.so```

# SYNOPSIS

**/etc/pam.conf**

# PARAMETERS

**service**
> 应用程序名称。

**type**
> auth、account、password、session。

**control**
> required、requisite、sufficient、optional。

**module**
> PAM 模块路径。

**arguments**
> 模块参数。

# DESCRIPTION

**pam.conf** 是旧式的 PAM 配置文件格式，所有服务都配置在单个文件中。现代系统通常改用 /etc/pam.d/ 目录，为每个服务单独提供配置文件。

每行定义一条规则，格式为：service type control module-path [arguments]。

# EXAMPLE

```
# /etc/pam.conf
login   auth       required   pam_securetty.so
login   auth       required   pam_unix.so
login   account    required   pam_unix.so
login   session    required   pam_limits.so
login   password   required   pam_unix.so

other   auth       required   pam_deny.so
other   account    required   pam_deny.so
```

# CONTROL FLAGS

```
required   - Must succeed, continue checking
requisite  - Must succeed, fail immediately if not
sufficient - Success ends checking, failure continues
optional   - Result ignored unless only module
```

# CAVEATS

现代系统更推荐使用 /etc/pam.d/。语法错误可能把你锁在系统外。请用另一个 root 会话进行测试。

# SEE ALSO

[pam.d](/man/pam.d)(5), [pam](/man/pam)(8), [pam_unix](/man/pam_unix)(8), [passwd](/man/passwd)(1), [sudo](/man/sudo)(8)
