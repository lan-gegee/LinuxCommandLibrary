# TAGLINE

将二进制文件编码为 ASCII 文本

# TLDR

**编码二进制文件**以便传输

```uuencode [file] [encoded_name] > [output.txt]```

改用 base64 **进行编码**而非 UU 编码

```uuencode -m [file] [encoded_name]```

**从 stdin 编码**

```cat [file] | uuencode [encoded_name]```

**编码并用邮件发送**文件

```uuencode [file] [file] | mail -s "Subject" [user@example.com]```

先压缩再**编码**以便传输

```gzip -c [file] | uuencode [file.gz]```

# SYNOPSIS

**uuencode** [_-m_] [_file_] _name_

# PARAMETERS

**-m**
> 使用 base64 编码代替传统的 UU 编码。

_file_
> 待编码的输入文件（省略时读取 stdin）。

_name_
> 存入编码输出中的名称，供 uudecode 解码时使用。

# DESCRIPTION

**uuencode** 把二进制文件编码成 ASCII 文本，以便经由只支持文本的通道传输，例如电子邮件或较老的网络协议。编码输出包含文件权限和名称信息，供 uudecode 重建文件。

默认情况下，uuencode 采用传统的 UU 编码（Unix-to-Unix encoding）。**-m** 选项则启用 base64 编码，这是现代系统中更为通用的方案。UU 编码会使文件体积增大约 37%，base64 约增大 35%。

输出格式由三部分组成：带有文件权限和名称的头行、若干编码数据行，以及一行终止标记。

# CAVEATS

就电子邮件而言，uuencode 已基本被 MIME base64 编码取代。现代系统通常直接使用 **base64** 命令。编码和解码时务必采用相同的编码方法。

# HISTORY

uuencode 由贝尔实验室开发，于 1980 年代初随 **BSD 4.0** 首次发布。它的出现是为了解决二进制文件无法在 UUCP（Unix-to-Unix Copy Protocol）网络上传送的问题——这类网络只能处理 7 位 ASCII。"uu" 前缀正是 "Unix-to-Unix" 的缩写。虽然在邮件领域已被 MIME 大面积取代，它在简单的二进制转文本任务中依然有用武之地。

# INSTALL

```apt: sudo apt install sharutils```

```dnf: sudo dnf install sharutils```

```pacman: sudo pacman -S sharutils```

```apk: sudo apk add sharutils```

```zypper: sudo zypper install sharutils```

```nix: nix profile install nixpkgs#sharutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uudecode](/man/uudecode)(1), [base64](/man/base64)(1), [mail](/man/mail)(1)
