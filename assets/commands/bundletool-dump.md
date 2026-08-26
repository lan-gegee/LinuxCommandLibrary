# TAGLINE

检查 Android App Bundle 内容

# TLDR

**从 app bundle 中导出 AndroidManifest.xml**

```bundletool dump manifest --bundle=[app.aab]```

**使用 XPath 获取特定的清单值**

```bundletool dump manifest --bundle=[app.aab] --xpath=/manifest/@versionCode```

**导出 app bundle 中的所有资源**

```bundletool dump resources --bundle=[app.aab]```

**按 ID 导出特定资源**

```bundletool dump resources --bundle=[app.aab] --resource=[0x7f0e013a] --values```

**导出 bundle 配置**

```bundletool dump config --bundle=[app.aab]```

**导出签名信息**

```bundletool dump signatures --bundle=[app.aab]```

# SYNOPSIS

**bundletool** **dump** _subcommand_ **--bundle**=_path_ [_options_]

# SUBCOMMANDS

**manifest**
> 导出解析后的 AndroidManifest.xml 内容。

**resources**
> 导出应用资源的详细信息。

**config**
> 导出 bundle 配置（SDK 版本、ABI、屏幕密度）。

**signatures**
> 导出数字签名信息。

# PARAMETERS

**--bundle** _path_
> Android App Bundle（.aab）文件的路径。

**--xpath** _expression_
> 用于提取特定清单值的 XPath 表达式。

**--resource** _id_
> 要导出的具体资源 ID。

**--values**
> 在输出中包含资源值。

**--module** _name_
> 指定 bundle 中要导出的模块。

**--output-file** _path_
> 将输出写入文件而不是 stdout。

# DESCRIPTION

**bundletool dump** 分析 Android App Bundle（.aab）和 APK 文件的内部结构和元数据。它是 Google bundletool 的一部分，Android Studio 和 Google Play 就是用这个底层工具来构建和处理 App Bundle 的。

用例包括构建验证、签名证书的安全分析、资源管理检查以及调试清单问题。

# CAVEATS

需要 Java 运行时环境（JRE）11 或更高版本。Linux 系统通常不预装。

# INSTALL

```brew: brew install bundletool```

```nix: nix profile install nixpkgs#bundletool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bundletool](/man/bundletool)(1), [bundletool-validate](/man/bundletool-validate)(1), [apktool](/man/apktool)(1)
