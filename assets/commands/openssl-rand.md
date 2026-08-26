# TAGLINE

生成伪随机字节

# TLDR

以十六进制**生成 32 个随机字节**

```openssl rand -hex [32]```

以 Base64 **生成 24 个随机字节**

```openssl rand -base64 [24]```

将 **256 个随机字节写入**文件

```openssl rand -out [path/to/file] [256]```

**生成随机密码**（16 字节，Base64 编码）

```openssl rand -base64 [16]```

# SYNOPSIS

**openssl** **rand** [**-help**] [**-out** _file_] [**-base64**] [**-hex**] [**-engine** _id_] [**-rand** _files_] [**-writerand** _file_] [**-provider** _name_] [**-provider-path** _path_] [**-propquery** _propq_] _num_

# PARAMETERS

**-help**
> 打印用法信息后退出。

**-out** _file_
> 将输出写入 _file_ 而不是标准输出。

**-base64**
> 使用 Base64 对输出进行编码。

**-hex**
> 以十六进制字符串显示输出。

**-engine** _id_
> 指定用于随机生成的引擎（在 OpenSSL 3.0 中已弃用）。

**-rand** _files_
> 指定额外的随机数据源文件。

**-writerand** _file_
> 退出时将随机状态写入 _file_。

**-provider** _name_
> 指定用于随机生成的提供程序。

**-provider-path** _path_
> 搜索提供程序的路径。

**-propquery** _propq_
> 用于选择提供程序的属性查询。

**_num_**
> 要生成的随机字节数（必需）。

# DESCRIPTION

**openssl rand** 使用密码学安全的伪随机数生成器（CSPRNG）生成指定数量的伪随机字节。它在内部调用 **RAND_bytes(3)**，只要从操作系统的熵源正确播种，即可提供 **256 位安全强度**。

输出可以写成原始二进制、Base64 编码或十六进制形式。常见用途包括生成随机密码、加密密钥、初始化向量以及用于密码学操作的 nonce。

# CAVEATS

如果 CSPRNG 无法从操作系统的熵源正确播种，该命令会以非零退出码失败。使用 **-base64** 时，由于 Base64 编码的膨胀（约 4/3 的比例外加换行符），实际输出会大于 _num_ 字节。**-engine** 选项自 OpenSSL 3.0 起已弃用，由基于提供程序的架构取代。

# HISTORY

**openssl rand** 至少自 **0.9.x 版本**（约 **2000 年**）起就是 OpenSSL 的一部分。**-engine** 选项在 **OpenSSL 3.0**（于 **2021 年**发布）中被弃用，由基于提供程序的架构取代。OpenSSL 本身始于 **1998 年**，是 SSLeay 的一个分支。

# INSTALL

```apt: sudo apt install openssl```

```dnf: sudo dnf install openssl```

```pacman: sudo pacman -S openssl```

```apk: sudo apk add openssl```

```zypper: sudo zypper install openssl```

```brew: brew install openssl```

```nix: nix profile install nixpkgs#openssl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1), [openssl-dgst](/man/openssl-dgst)(1)
