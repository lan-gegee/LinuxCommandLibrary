# TAGLINE

管理 RPM 软件包签名密钥

# TLDR

**列出**所有已导入的 RPM 密钥

```sudo rpmkeys --list```

**导入**来自仓库的 RPM 密钥

```sudo rpmkeys --import [path/to/rpm_key]```

按键 ID **删除**先前导入的 RPM 密钥

```sudo rpmkeys --delete [5a278d9c-5bbc73cb]```

# SYNOPSIS

**rpmkeys** {**--import**|**--delete**|**--list**|**--checksig**} [_options_] [_keyfile_|_package_]

# PARAMETERS

**--import**
> 从文件导入公钥

**--delete**
> 按密钥 ID 删除已导入的密钥

**--list**
> 列出所有已导入的 RPM 密钥及其密钥 ID

**--checksig, -K**
> 校验软件包签名

**-v, --verbose**
> 提供更详细的输出

# DESCRIPTION

**rpmkeys** 管理用于校验 RPM 软件包签名的 GPG 密钥。在添加 RPM 软件仓库时，还应一并导入其对应的签名密钥，以启用签名校验并确保软件包来源可信。

密钥保存在 RPM 数据库中，并在软件包安装过程中自动用于验证软件包未被篡改。**--list** 选项会显示删除密钥所需的密钥 ID。

# CAVEATS

导入或删除密钥需要 root 权限。密钥 ID 是 16 个字符的十六进制字符串。删除某仓库的密钥会导致来自该仓库的软件包签名校验失败。

# INSTALL

```apt: sudo apt install rpm```

```dnf: sudo dnf install rpm```

```apk: sudo apk add rpm```

```zypper: sudo zypper install rpm```

```brew: brew install rpm```

```nix: nix profile install nixpkgs#rpm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rpm](/man/rpm)(8), [rpm2cpio](/man/rpm2cpio)(8), [gpg](/man/gpg)(1)
