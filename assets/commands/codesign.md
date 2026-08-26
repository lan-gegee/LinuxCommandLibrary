# TAGLINE

macOS 代码签名与验证工具

# TLDR

**签署应用程序**

```codesign -s "[Developer ID]" [MyApp.app]```

**带时间戳签署**

```codesign -s "[Developer ID]" --timestamp [MyApp.app]```

**递归（深度）签署**

```codesign -s "[Developer ID]" --deep [MyApp.app]```

**强制重新签署**

```codesign -s "[Developer ID]" --force [MyApp.app]```

**验证签名**

```codesign -v [MyApp.app]```

**显示签名信息**

```codesign -d -v [MyApp.app]```

**移除签名**

```codesign --remove-signature [MyApp.app]```

# SYNOPSIS

**codesign** _operation_ [_options_] _path_...

# DESCRIPTION

**codesign** 在 macOS 上创建、验证和显示代码签名。代码签名是获得 Gatekeeper 批准、公证和分发应用所必需的。它对可执行文件、应用、框架、插件和其他代码进行加密签名，以验证其真实性和完整性。

该工具与 macOS 安全框架集成，强制要求代码来自可识别的开发者且未被篡改。签名需要 Keychain 中存有 Apple 签发的有效证书。来自 Apple 服务器的时间戳确保签名在证书过期后仍然有效。

深度签名会递归签署 bundle 内所有嵌套内容，这对于带有内嵌框架和插件的复杂应用是必要的。Entitlements 文件指定安全能力与权限。验证操作确认签名有效并满足指定的要求。

# OPERATIONS

**-s** _identity_, **--sign** _identity_
> 使用指定身份签署代码

**-v**, **--verify**
> 验证代码签名

**-d**, **--display**
> 显示签名信息

**--remove-signature**
> 移除现有签名

# PARAMETERS

**--force**, **-f**
> 替换现有签名

**--deep**
> 递归签署嵌套内容

**--timestamp**[=_url_]
> 从服务器请求时间戳

**--options** _flags_
> 设置代码签名选项（runtime 等）

**-a** _arch_, **--architecture** _arch_
> 为通用二进制文件指定架构

**--all-architectures**
> 验证所有架构

**--entitlements** _file_
> 从文件嵌入 entitlements

**-r** _requirement_
> 设置代码要求

**-i** _identifier_
> 设置 bundle 标识符

**--strict**
> 严格验证

# EXIT CODES

**0**: 成功

**1**: 签名/验证失败

**2**: 无效参数

**3**: 签名有效但要求未满足

# CAVEATS

选项顺序很重要（动词在前，名词在后）。使用 --force 替换签名。需要 Keychain 中有效的签名身份。

# SEE ALSO

[xcrun](/man/xcrun)(1), [xcodebuild](/man/xcodebuild)(1)
