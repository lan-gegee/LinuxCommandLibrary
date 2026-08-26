# TAGLINE

扫描 APK 中的硬编码机密和密钥

# TLDR

**扫描** APK 中的硬编码机密

```apkleaks -f [app.apk]```

以 **JSON 输出**扫描

```apkleaks -f [app.apk] -o [results.json]```

使用**自定义模式**扫描

```apkleaks -f [app.apk] -p [patterns.json]```

**详细**输出

```apkleaks -f [app.apk] -v```

# SYNOPSIS

**apkleaks** -f _apk_file_ [_-o output_] [_-p patterns_] [_options_]

# DESCRIPTION

**apkleaks** 扫描 Android APK 文件中的硬编码机密、API 密钥和敏感信息。它会反编译 APK，使用正则表达式模式搜索代码和资源，并报告潜在的安全问题。

该工具有助于识别凭据、私钥、带 token 的 URL 等敏感数据的意外泄露——这些往往是开发者无意间打包进应用的。

# PARAMETERS

**-f** _file_
> 要分析的 APK 文件

**-o** _file_
> 结果的输出文件

**-p** _file_
> 自定义模式文件（JSON）

**-a** _args_
> 传递给 jadx 反编译器的附加参数。

**--json**
> 以 JSON 格式输出结果。

**-v**, **--verbose**
> 详细输出，包括匹配行的行号。

**--disassemble**
> 反汇编字节码（较慢，可能发现更多机密）。

# DETECTED PATTERNS

- API 密钥（AWS、Google、Facebook 等）
- 私钥和证书
- URL 中的 token 和机密
- 硬编码密码
- 数据库凭据
- 自定义正则表达式模式

# CAVEATS

可能产生需要人工核实的误报。只能检测基于字符串的机密；加密或混淆的数据无法找到。受到高度保护的 APK 可能反编译失败。

# HISTORY

**apkleaks** 为 Android 安全评估而创建，将人工代码审查可能遗漏的机密泄露识别过程自动化。

# INSTALL

```brew: brew install apkleaks```

```nix: nix profile install nixpkgs#apkleaks```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apktool](/man/apktool)(1), [jadx](/man/jadx)(1), [androguard](/man/androguard)(1)
