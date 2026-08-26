# TAGLINE

与 Sigstore 透明日志交互

# TLDR

**上传条目**

```rekor-cli upload --artifact [file] --signature [file.sig] --public-key [key.pub]```

**按工件搜索**

```rekor-cli search --artifact [file]```

**按电子邮件搜索**

```rekor-cli search --email [user@example.com]```

**按 UUID 获取条目**

```rekor-cli get --uuid [entry-uuid]```

**按日志索引获取条目**

```rekor-cli get --log-index [12345]```

**验证条目**

```rekor-cli verify --artifact [file] --signature [file.sig]```

**显示日志信息**

```rekor-cli loginfo```

# SYNOPSIS

**rekor-cli** _command_ [_--artifact file_] [_--signature file_] [_options_]

# PARAMETERS

**upload**
> 向日志添加条目。

**search**
> 搜索条目。

**get**
> 获取条目。

**verify**
> 验证工件。

**loginfo**
> 日志信息。

**--artifact** _FILE_
> 工件文件。

**--signature** _FILE_
> 签名文件。

**--public-key** _FILE_
> 公钥文件。

**--uuid** _UUID_
> 条目 UUID。

**--rekor_server** _URL_
> Rekor 服务器 URL。

# DESCRIPTION

**rekor-cli** 与 Rekor 透明日志交互。Rekor 提供防篡改的审计追踪。

upload 将已签名的工件添加到日志。条目一经记录便不可更改。

search 按工件、电子邮件或哈希查找条目，可证明签名的创建时间。

verify 将工件与日志进行核对，确认签名的有效性和时间。

loginfo 显示树大小和根哈希，可用于验证日志完整性。

# CONFIGURATION

**REKOR_REKOR_SERVER**
> 设置默认 Rekor 服务器 URL 的环境变量，覆盖内置的公共实例 rekor.sigstore.dev。

# CAVEATS

需要能访问 Rekor 服务器的网络。条目是公开的。密钥管理需另行处理。

# HISTORY

**Rekor** 是 **Sigstore** 项目的组成部分，由 **Google**、**Red Hat** 等发起。它为软件供应链安全提供透明日志。

# INSTALL

```apt: sudo apt install rekor```

```pacman: sudo pacman -S rekor```

```apk: sudo apk add rekor```

```zypper: sudo zypper install rekor```

```brew: brew install rekor-cli```

```nix: nix profile install nixpkgs#rekor-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cosign](/man/cosign)(1), [fulcio](/man/fulcio)(1)
