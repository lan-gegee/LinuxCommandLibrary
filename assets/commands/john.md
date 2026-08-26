# TAGLINE

John the Ripper，密码安全审计工具

# TLDR

**破解密码文件**

```john [hashes.txt]```

**显示已破解的密码**

```john --show [hashes.txt]```

**使用指定的字典文件**

```john --wordlist=[wordlist.txt] [hashes.txt]```

**指定哈希格式**

```john --format=[md5crypt] [hashes.txt]```

**增量模式**

```john --incremental [hashes.txt]```

**恢复破解会话**

```john --restore```

# SYNOPSIS

**john** [_options_] [_password_files_]

# PARAMETERS

_PASSWORD_FILES_
> 包含哈希的文件。

**--show**
> 显示已破解的密码。

**--wordlist** _FILE_
> 使用字典攻击。

**--format** _FORMAT_
> 哈希格式（md5crypt、sha256 等）。

**--incremental**
> 暴力破解模式。

**--restore**
> 恢复上一次会话。

**--help**
> 显示帮助信息。

# DESCRIPTION

**john** 即 John the Ripper，是一款密码安全审计工具。它通过各种破解方法检测弱密码。

该工具支持众多哈希格式和攻击模式，常用于安全测试和密码审计。

# CAVEATS

仅限授权用途。会大量占用 CPU/GPU 资源。Jumbo 版本支持更多哈希格式。

# HISTORY

John the Ripper 由 **Solar Designer** 于 1996 年创建，现由 **Openwall** 维护，是一款开源密码审计工具。

# INSTALL

```apt: sudo apt install john```

```dnf: sudo dnf install john```

```pacman: sudo pacman -S john```

```apk: sudo apk add john```

```zypper: sudo zypper install john```

```brew: brew install john```

```nix: nix profile install nixpkgs#john```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hashcat](/man/hashcat)(1), [unshadow](/man/unshadow)(1), [zip2john](/man/zip2john)(1)
