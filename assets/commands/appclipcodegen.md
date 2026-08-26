# TAGLINE

生成并校验 Apple App Clip Codes

# TLDR

**生成** SVG 格式的 App Clip Code

```AppClipCodeGenerator generate --url [https://example.com] --type [cam] --foreground [FFFFFF] --background [000000] --output [output.svg]```

**生成**支持 NFC 的 App Clip Code

```AppClipCodeGenerator generate --url [https://example.com] --type [nfc] --foreground [FFFFFF] --background [000000] --output [output.svg]```

**校验颜色**并获得建议

```AppClipCodeGenerator suggest --foreground [FFFFFF] --background [000000]```

# SYNOPSIS

**AppClipCodeGenerator** \<command\> [_options_]

# PARAMETERS

**generate**
> 生成 App Clip Code SVG 文件

**suggest**
> 校验颜色组合并获得建议

**--url** _URL_
> 扫描 App Clip Code 时打开的 URL

**--type** _cam|nfc_
> 代码类型：**cam** 表示仅可通过相机扫描，**nfc** 表示支持 NFC 的代码

**--foreground** _RRGGBB_
> 前景色，十六进制值

**--background** _RRGGBB_
> 背景色，十六进制值

**--output** _path_
> 生成的 SVG 文件输出路径

# DESCRIPTION

**AppClipCodeGenerator** 是 Apple 官方用于创建和校验 App Clip Codes 的命令行工具。App Clip Code 是外观独特、可扫描的代码，可在 iOS 设备上启动 App Clip 体验——一种无需安装完整应用即可发现的轻量应用体验。

该工具生成 SVG 格式的 App Clip Code，包含两种类型：**cam** 类型可被设备相机扫描；**nfc** 类型还额外支持近场通信（NFC）触碰即开。**suggest** 命令用于校验前景色与背景色组合是否满足 Apple 的对比度和可读性要求。

App Clip Code 编码的 URL 通过 Apple App Store Connect 配置映射到已注册的 App Clip 体验。

# CAVEATS

仅在 **macOS** 上可用，属于 Apple 开发者工具的一部分。该工具必须从 Apple 的 App Clip 资源页面单独下载。生成的代码需要在 **App Store Connect** 中配置已注册的 App Clip 体验才能生效。颜色组合必须符合 Apple 的对比度要求——生成前请用 **suggest** 命令校验颜色。

# HISTORY

AppClipCodeGenerator 由 **Apple** 于 **iOS 14**（2020 年）随 **App Clips** 一同发布。App Clips 在 **WWDC 2020** 上亮相，旨在通过 Safari、地图、NFC 标签和二维码提供聚焦的应用体验。这款代码生成工具让开发者能够创建在外观上区别于标准二维码的专有 App Clip Code 格式。

# SEE ALSO

[xcodebuild](/man/xcodebuild)(1), [xcrun](/man/xcrun)(1)
