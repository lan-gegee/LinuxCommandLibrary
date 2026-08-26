# TAGLINE

对 Java 归档文件进行签名和验证

# TLDR

**对 JAR 文件签名**

```jarsigner -keystore [keystore.jks] [app.jar] [alias]```

**验证签名**

```jarsigner -verify [app.jar]```

**详细验证**

```jarsigner -verify -verbose -certs [app.jar]```

**对 APK 文件签名**

```jarsigner -keystore [keystore.jks] -signedjar [signed.apk] [unsigned.apk] [alias]```

**使用指定算法签名**

```jarsigner -sigalg SHA256withRSA -digestalg SHA-256 [app.jar] [alias]```

# SYNOPSIS

**jarsigner** [_options_] _jar-file_ _alias_

# DESCRIPTION

**jarsigner** 用于对 Java Archive（JAR）文件进行签名和验证。它添加数字签名以确保真实性和完整性，这是 Java applet、Android 应用和签名 JAR 所必需的。

该工具使用存储在 keystore 中的证书进行签名。验证过程会检查内容是否被修改过，并校验签名者的证书。

# PARAMETERS

**-keystore** _file_
> Keystore 位置。

**-storepass** _pass_
> Keystore 密码。

**-keypass** _pass_
> 密钥密码。

**-signedjar** _file_
> 输出的已签名 JAR 名称。

**-sigalg** _algo_
> 签名算法。

**-digestalg** _algo_
> 摘要算法。

**-verify**
> 验证签名。

**-verbose**
> 详细输出。

**-certs**
> 显示证书。

**-tsa** _url_
> 时间戳权威机构（TSA）URL。

# CAVEATS

弱算法已被弃用。Keystore 需妥善保护。若要长期有效建议加时间戳。Android 有特定要求。

# HISTORY

**jarsigner** 自 Java 早期起就是 **JDK** 的一部分。JAR 签名最初对浏览器中的 Java applet 很重要，后来对 Android 应用分发也很关键。该工具不断演进以支持更强的加密算法。

# SEE ALSO

[keytool](/man/keytool)(1), [jar](/man/jar)(1), [apksigner](/man/apksigner)(1), [openssl](/man/openssl)(1)
