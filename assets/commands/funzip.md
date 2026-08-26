# TAGLINE

从管道中解压 ZIP 或 gzip 归档的第一个成员

# TLDR

**通过 stdin 从 ZIP 归档中提取第一个文件**

```cat [file.zip] | funzip > [output]```

**通过 stdin 从 gzip 文件中提取**

```cat [file.gz] | funzip > [output]```

**下载并解压一步完成**

```curl -s [url/file.zip] | funzip > [output]```

**直接从文件参数提取**

```funzip [file.zip] > [output]```

**解压受密码保护的 ZIP 归档**

```funzip -[password] [file.zip] > [output]```

**借助二级归档工具处理 tar.zip 归档**

```cat [archive.tar.zip] | funzip | tar xf -```

# SYNOPSIS

**funzip** [**-**_password_] [_input_[.zip|.gz]]

# DESCRIPTION

**funzip** 作为过滤器，用于从 ZIP 归档或 gzip 文件中提取第一个成员。不带文件参数时，它从标准输入读取并写入标准输出；给定文件参数时，则改为从该文件读取。它也能处理 gzip 压缩文件。

它最适合在不生成中间文件的情况下从管道中提取单文件归档，或者与 **tar**(1) 等二级归档工具配合进行磁带备份。

# PARAMETERS

**-**_password_
> 加密 ZIP 归档的解密密码。在命令行上传递密码不安全，因为可能会通过 ps(1) 被他人看到。

# CAVEATS

只能提取 ZIP 归档的第一个成员。多文件归档请改用 **unzip**。当第一个成员是目录时，funzip 只会创建该目录然后退出。

# INSTALL

```apt: sudo apt install unzip```

```dnf: sudo dnf install unzip```

```pacman: sudo pacman -S unzip```

```apk: sudo apk add unzip```

```zypper: sudo zypper install unzip```

```brew: brew install unzip```

```nix: nix profile install nixpkgs#unzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gzip](/man/gzip)(1), [unzip](/man/unzip)(1), [unzipsfx](/man/unzipsfx)(1), [zip](/man/zip)(1), [zipinfo](/man/zipinfo)(1)
