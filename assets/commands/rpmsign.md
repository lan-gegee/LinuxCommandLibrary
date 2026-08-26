# TAGLINE

用 GPG 密钥为 RPM 软件包签名

# TLDR

**为 RPM 软件包签名**

```rpmsign --addsign [package.rpm]```

**使用指定密钥签名**

```rpmsign --addsign --key-id [KEYID] [package.rpm]```

**重新签名软件包**

```rpmsign --resign [package.rpm]```

**删除签名**

```rpmsign --delsign [package.rpm]```

**为多个软件包签名**

```rpmsign --addsign [*.rpm]```

# SYNOPSIS

**rpmsign** **--addsign**|**--resign** [_options_] _PACKAGE_FILE_...

**rpmsign** **--delsign** _PACKAGE_FILE_...

**rpmsign** **--delfilesign** _PACKAGE_FILE_...

# PARAMETERS

**--addsign**
> 为软件包添加签名。

**--resign**
> 替换现有的签名。

**--delsign**
> 删除所有 OpenPGP 签名。

**--delfilesign**
> 删除所有 IMA 和 fsverity 文件签名。

**--key-id** _KEYID_
> GPG 密钥 ID，覆盖 %_openpgp_sign_id 配置。

**--signfiles**
> 使用所配置的摘要算法和 RSA 密钥为软件包文件签名。

**--fskpath** _KEY_
> 文件签名密钥路径，与 --signfiles 配合使用。

**--signverity**
> 用 fsverity 签名为软件包文件签名。

**--certpath** _CERT_
> 与 --signverity 配合使用的证书。

**--rpmv3**
> 在 V4 软件包上添加 RPM V3 头部+有效负载签名，以兼容 rpm < 4.14。

**--rpmv4**
> 在 V6 软件包上添加 RPM V4 头部签名，以兼容 rpm 4.x。

**-D** _"MACRO EXPR"_
> 定义 RPM 宏。

# DESCRIPTION

**rpmsign** 为 RPM 软件包添加或管理 OpenPGP 签名。给软件包签名可以验证其真实性和完整性。它同时支持传统的整包签名和文件级的 IMA/fsverity 签名。

它是 RPM 包管理器的一部分。签名密钥通过 **%_openpgp_sign_id** 宏（或旧式的 **%_gpg_name**）来配置。

# EXAMPLES

```bash
# Sign package
rpmsign --addsign mypackage-1.0-1.x86_64.rpm

# Sign with specific key
rpmsign --addsign --key-id ABCD1234 package.rpm

# Re-sign (replace signature)
rpmsign --resign package.rpm

# Sign all RPMs
rpmsign --addsign *.rpm

# Define signing identity via macro
rpmsign -D "_gpg_name Your Name" --addsign package.rpm

# Delete file signatures
rpmsign --delfilesign package.rpm

# Verify signature
rpm -K package.rpm
```

# CONFIGURATION

**~/.rpmmacros**
> 用户级 RPM 宏文件；在其中设置 **%_openpgp_sign_id**（或旧式的 **%_gpg_name**）可指定默认的签名身份，设置 **%_gpg_path** 可指定 GnuPG 密钥环目录。

**/etc/rpm/macros**
> 系统级 RPM 宏覆盖文件，供所有用户共享签名相关的默认设置。

# CAVEATS

需要 GPG 密钥。需要密码短语（或 gpg-agent）。签名会被添加到头部中。

# HISTORY

rpmsign 是 **RPM** 包管理器的组成部分，最初由 **Red Hat** 开发，用于软件包身份认证。

# INSTALL

```apt: sudo apt install rpm```

```dnf: sudo dnf install rpm```

```apk: sudo apk add rpm```

```zypper: sudo zypper install rpm```

```brew: brew install rpm```

```nix: nix profile install nixpkgs#rpm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rpm](/man/rpm)(8), [rpmbuild](/man/rpmbuild)(8), [rpmkeys](/man/rpmkeys)(8), [gpg](/man/gpg)(1)
