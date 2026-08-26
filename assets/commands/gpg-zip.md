# TAGLINE

将文件加密或签名到 GPG 归档中（已弃用）

# TLDR

**用对称加密加密目录**

```gpg-zip --symmetric --output [archive.gpg] [directory]```

**为指定接收者加密**

```gpg-zip --encrypt --output [archive.gpg] --gpg-args "-r [recipient]" [directory]```

**解密归档**

```gpg-zip --decrypt [archive.gpg]```

**列出归档内容**

```gpg-zip --list-archive [archive.gpg]```

**签名并加密**

```gpg-zip --encrypt --sign --output [archive.gpg] [directory]```

# SYNOPSIS

**gpg-zip** [_options_] [_files_]

# PARAMETERS

**-e**, **--encrypt**
> 加密数据。

**-d**, **--decrypt**
> 解密数据。

**-c**, **--symmetric**
> 使用口令进行对称加密。

**-s**, **--sign**
> 对数据进行签名。

**--list-archive**
> 列出归档内容。

**-o**, **--output** _file_
> 输出文件。

**--gpg-args** _args_
> 向 gpg 传递选项。

**--tar** _command_
> 使用替代的 tar 命令。

# DESCRIPTION

**gpg-zip** 使用 GnuPG 将文件加密或签名到一个归档中。它将 tar 归档与 GPG 加密结合在一起，采用与 PGP Zip 兼容的格式，同时支持对称（口令）和非对称（公钥）加密。

该工具已被弃用，请改用 **gpgtar**，后者提供相同的功能并与现代 GnuPG 套件集成得更好。

# CAVEATS

**gpg-zip** 已被弃用。请改用 **gpgtar**。

# INSTALL

```apt: sudo apt install gpg```

```apk: sudo apk add gpg```

```brew: brew install gpg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1), [tar](/man/tar)(1)
