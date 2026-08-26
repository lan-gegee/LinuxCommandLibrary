# TAGLINE

向 APT 密钥环添加 GPG 密钥

# TLDR

从默认密钥服务器**按密钥 ID 添加**GPG 密钥

```sudo add-apt-key [KEY_ID]```

从指定的**密钥服务器添加**GPG 密钥

```sudo add-apt-key -k [keyserver.ubuntu.com] [KEY_ID]```

**添加**密钥并输出**详细**信息

```sudo add-apt-key -v [KEY_ID]```

# SYNOPSIS

**add-apt-key** [_options_] _keyid_

# DESCRIPTION

**add-apt-key** 从公共密钥服务器请求指定的 GPG 密钥并将其插入 APT 密钥环，使由该密钥签名的软件归档受信任。默认密钥服务器可在 /etc/default/add-apt-key 中配置。

# PARAMETERS

**-h**, **--help**
> 显示用法信息。

**-v**, **--verbose**
> 详细输出模式；在每条命令执行前先将其显示出来。

**-k**, **--keyserver** _name_
> 选择要使用的特定密钥服务器。

_keyid_
> 要添加的 GPG 密钥标识符。

# EXIT STATUS

**0** - 密钥添加成功。

**1** - 参数无效。

**2** - 无法获取 GPG 密钥 ID 或其格式有误。

**3** - 向 APT 密钥环插入密钥失败。

# CAVEATS

并非所有发行版都提供此工具。现代做法是把软件仓库密钥放到 /etc/apt/keyrings/ 中，并在 source list 文件里用 signed-by 选项直接引用。

# SEE ALSO

[apt-key](/man/apt-key)(8), [gpg](/man/gpg)(1), [apt](/man/apt)(8)
