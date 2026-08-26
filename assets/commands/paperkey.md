# TAGLINE

提取可打印的 GPG 密钥数据

# TLDR

**从 GPG 密钥中提取私钥**

```paperkey --secret-key [secret.gpg] --output [paperkey.txt]```

**从纸质备份恢复**

```paperkey --pubring [public.gpg] --secrets [paperkey.txt] --output [restored.gpg]```

**以 base16 输出**

```paperkey --secret-key [secret.gpg] --output-type base16```

# SYNOPSIS

**paperkey** [_options_]

# PARAMETERS

**--secret-key** _FILE_
> 私钥文件。

**--pubring** _FILE_
> 用于恢复的公钥环。

**--secrets** _FILE_
> 纸质备份文件。

**--output** _FILE_
> 输出文件。

**--output-type** _TYPE_
> 输出格式（raw、base16）。

# DESCRIPTION

**paperkey** 提取可打印的 GPG 密钥数据。用于创建纸质备份。

该工具支持密钥的离线存储。恢复时需要公钥。

# CAVEATS

恢复时需要公钥。请打印后妥善保管。

# HISTORY

paperkey 是为基于纸面的 **GPG 密钥**备份与恢复而开发的。

# INSTALL

```apt: sudo apt install paperkey```

```dnf: sudo dnf install paperkey```

```pacman: sudo pacman -S paperkey```

```zypper: sudo zypper install paperkey```

```brew: brew install paperkey```

```nix: nix profile install nixpkgs#paperkey```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gpg](/man/gpg)(1), [gpg2](/man/gpg2)(1)
