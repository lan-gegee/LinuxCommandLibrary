# TAGLINE

生成适合用户账户使用的随机密码

# TLDR

**生成随机密码**

```makepasswd```

**生成多个密码**

```makepasswd --count [5]```

**生成指定长度的密码**

```makepasswd --chars [16]```

**使用指定字符集生成**

```makepasswd --string '[A-Za-z0-9!@#]'```

**Generate a crypted password**（用于 /etc/shadow，MD5 方案）

```makepasswd --crypt-md5```

**使用固定随机种子**以获得可复现的输出

```makepasswd --randomseed [42] --count [3]```

**指定最小和最大长度**

```makepasswd --minchars [8] --maxchars [12]```

# SYNOPSIS

**makepasswd** [_--count n_] [_--chars n_] [_--string chars_] [_--crypt_] [_options_]

# PARAMETERS

**--count** _N_
> 生成 N 个密码。

**--chars** _N_
> 密码长度。

**--minchars** _N_
> 最小长度。

**--maxchars** _N_
> 最大长度。

**--string** _CHARS_
> 要使用的字符集。

**--crypt**
> 输出经 DES 加密的密码。

**--crypt-md5**
> 输出经 MD5 加密的密码。

**--clearfrom** _FILE_
> 从文件读取明文。

**--cryptsalt** _N_
> crypt 使用的盐值。

**--randomseed** _N_
> 用 _N_ 作为随机数生成器的种子（用 **0** 表示真随机，固定值则可复现）。

**--rerandom** _N_
> 每生成 _N_ 个密码就重新设置一次随机数生成器的种子。

**--repeatpass** _N_
> 将每个生成的密码重复输出 _N_ 次（与 **--crypt** 搭配可将明文与哈希一一对应）。

**--nocrypt**
> 跳过加密哈希，仅输出明文。

**--verbose**, **--noverbose**
> 切换说明性输出。

# DESCRIPTION

**makepasswd** 生成适合用户账户使用的随机密码。它使用 /dev/urandom 作为随机源，产生适合加密用途的输出。

默认情况下，它使用字母和数字生成一个长度合理的单个密码。string 选项可以自定义字符集，以满足特定的密码策略。

crypt 系列选项会生成适用于 /etc/shadow 的密码哈希。MD5 crypt 生成的哈希以 $1$ 开头，与现代系统兼容。DES crypt 是遗留方案，且限制为 8 个字符。

配合 count 进行批量生成对创建多个账户很有用。结合适当的长度和字符要求，即可满足大多数密码策略。

在脚本中，密码每行输出一个。与 crypt 结合使用时，明文和哈希都会同时输出以便参考。

# CAVEATS

DES crypt 限制为 8 个字符——请改用 MD5。随机密码难以记忆。生成的密码应由用户自行修改。某些特殊字符可能引发 shell 问题。

# HISTORY

**makepasswd** 由 **Rob Browning** 于 **20 世纪 90 年代**为 **Debian** 编写。它为系统管理员提供了一个在创建账户时生成密码的简单工具。该软件包至今仍保留在 Debian 及其衍生发行版中。

# INSTALL

```dnf: sudo dnf install makepasswd```

```apk: sudo apk add makepasswd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pwgen](/man/pwgen)(1), [apg](/man/apg)(1), [openssl](/man/openssl)(1), [passwd](/man/passwd)(1)
