# TAGLINE

管理 Apache HTTP Server 基本认证的用户认证文件

# TLDR

**创建新的密码文件**并添加用户

```htpasswd -c [path/to/.htpasswd] [username]```

**在已有文件中添加或更新用户**

```htpasswd [path/to/.htpasswd] [username]```

**在命令行上指定密码添加用户**（不安全）

```htpasswd -b [path/to/.htpasswd] [username] [password]```

**从文件中删除用户**

```htpasswd -D [path/to/.htpasswd] [username]```

**验证用户的密码**

```htpasswd -v [path/to/.htpasswd] [username]```

**使用 bcrypt 加密**（更安全）

```htpasswd -B [path/to/.htpasswd] [username]```

**只显示密码哈希**而不更新文件

```htpasswd -n [username]```

**使用 SHA 加密创建文件**

```htpasswd -c -s [path/to/.htpasswd] [username]```

# SYNOPSIS

**htpasswd** [_-cimBdpsDv_] [_-C cost_] _passwordfile_ _username_ [_password_]

# PARAMETERS

**-c**
> 创建新文件（覆盖已有文件）。

**-n**
> 将结果显示到标准输出，不更新文件。

**-b**
> 使用命令行中给出的密码（批处理模式，不安全）。

**-i**
> 从标准输入读取密码，不进行确认。

**-m**
> 使用 MD5 加密（大多数系统的默认值）。

**-B**
> 使用 bcrypt 加密（最安全）。

**-C** _cost_
> 设置 bcrypt cost（4-17，默认 5，越高越慢）。

**-d**
> 使用 crypt() 加密（不安全，密码最多 8 个字符）。

**-s**
> 使用 SHA 加密（不安全）。

**-p**
> 使用明文（不安全，仅用于测试）。

**-D**
> 删除指定用户。

**-v**
> 验证用户密码。

# DESCRIPTION

**htpasswd** 管理 Apache HTTP Server 基本认证所需的用户认证文件。它创建并更新包含用户名和加密密码的平面文件数据库，供 **.htaccess** 或 Apache 配置指令使用。

密码文件的格式很简单：每个用户一行，形如 **username:encrypted_password**。Apache 的 mod_auth_basic 读取该文件来认证请求。此文件应存放在 web 根目录之外，并设置严格的访问权限。

密码加密默认采用基于 MD5 的算法（以 $apr1$ 为前缀）。**-B** 选项启用 bcrypt，它能更好地抵抗暴力破解攻击，推荐用于新部署。cost 因子（-C）控制 bcrypt 的计算强度。

若要在脚本中进行非交互式操作，**-b** 允许直接在命令行上给出密码，但这会把密码暴露在进程列表中。**-i** 选项改为从标准输入读取，对脚本而言更安全。

该工具也常与 Nginx 搭配使用，因为 Nginx 可以读取 Apache 格式的密码文件来实现基本认证。

# CAVEATS

-b 选项会将密码暴露在进程列表中。基本认证以 base64 发送凭据（并未加密）——务必配合 HTTPS 使用。旧算法（crypt、SHA、明文）都不安全。文件权限必须严格限制。不适合高安全性场景。

# HISTORY

**htpasswd** 自上世纪 90 年代中期以来一直是 Apache HTTP Server 项目的一部分。它源自 NCSA HTTPd 的密码管理工具。随着密码安全要求的提高，后来加入了 bcrypt 选项。尽管如今有更复杂的认证方法可用，该工具仍是管理 Apache 基本认证的标准工具。

# INSTALL

```apt: sudo apt install apache2-utils```

```apk: sudo apk add apache2-utils```

```zypper: sudo zypper install apache2-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apache2](/man/apache2)(8), [nginx](/man/nginx)(8), [openssl](/man/openssl)(1)
