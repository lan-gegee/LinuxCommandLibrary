# TAGLINE

为 Android APK 文件签名和验证签名

# TLDR

为 APK **签名**

```apksigner sign --ks [keystore.jks] [app.apk]```

使用**指定密钥别名**签名

```apksigner sign --ks [keystore.jks] --ks-key-alias [alias] [app.apk]```

**验证** APK 签名

```apksigner verify [app.apk]```

带**详细信息**验证

```apksigner verify --verbose --print-certs [app.apk]```

使用 **PKCS #8 密钥和证书**签名（不通过 keystore）

```apksigner sign --key [key.pk8] --cert [cert.x509.pem] [app.apk]```

以**最低 SDK 版本**为目标签名

```apksigner sign --ks [keystore.jks] --min-sdk-version [21] [app.apk]```

# SYNOPSIS

**apksigner** **sign** [_options_] _apk_

**apksigner** **verify** [_options_] _apk_

**apksigner** **rotate** [_options_]

**apksigner** **lineage** [_options_]

# DESCRIPTION

**apksigner** 是 Android SDK 官方的 APK 签名工具。它支持多种签名方案（v1/JAR、v2、v3、v4），可以为 zipalign 对齐后的 APK 签名。

该工具确保 APK 满足 Android 的安装与更新签名要求，较新的方案提供更好的安全性和更快的验证速度。

# PARAMETERS

**sign**
> 为 APK 签名。

**verify**
> 验证 APK 签名。

**rotate**
> 轮换签名密钥，生成从旧密钥到新密钥的 lineage。

**lineage**
> 检查或更新签名证书 lineage。

**--ks** _file_
> Keystore 文件。对于不需要文件的 keystore 类型（如某些 PKCS #11），请使用 **NONE**。

**--ks-key-alias** _alias_
> Keystore 中的密钥别名。

**--ks-pass** _spec_
> Keystore 密码（pass:、env:、file: 或 stdin）。

**--key-pass** _spec_
> 密钥密码（输入格式与 --ks-pass 相同）。

**--key** _file_
> PKCS #8 私钥文件（--ks 的替代方式）。

**--cert** _file_
> X.509 证书链文件（与 --key 配合使用）。

**--out** _file_
> 已签名 APK 的输出路径。

**--min-sdk-version** _int_
> 要验证签名的最低 API 级别。默认取 manifest 的 minSdkVersion。

**--max-sdk-version** _int_
> 要验证签名的最高 API 级别。

**--v1-signing-enabled** _bool_
> 启用 JAR 签名（v1）。

**--v2-signing-enabled** _bool_
> 启用 APK Signature Scheme v2。

**--v3-signing-enabled** _bool_
> 启用 APK Signature Scheme v3。

**--v4-signing-enabled** _bool|only_
> 启用 APK Signature Scheme v4，会生成单独的 .idsig 文件。

**--verbose**, **-v**
> 详细输出。

**--print-certs**
> 打印证书详情（仅 verify 支持）。

# CAVEATS

APK 在用 v2+ 方案签名前必须先经过 zipalign。Android 11+ 不再建议仅用 v1 签名。密钥轮换需要 v3 签名。私钥安全至关重要。

# HISTORY

**apksigner** 随 Android SDK Build Tools 24.0.3（**2016 年**）与 APK Signature Scheme v2 一同推出，取代 jarsigner 成为推荐的签名工具。

# INSTALL

```nix: nix profile install nixpkgs#apksigner```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[zipalign](/man/zipalign)(1), [keytool](/man/keytool)(1), [jarsigner](/man/jarsigner)(1), [aapt](/man/aapt)(1)

# RESOURCES

```[Source code](https://android.googlesource.com/platform/tools/apksig/)```

```[Documentation](https://developer.android.com/tools/apksigner)```

<!-- verified: 2026-06-11 -->
