# TAGLINE

从应用商店下载 APK

# TLDR

从默认来源（APKPure）**下载** APK

```apkeep -a [com.example.app] .```

下载**特定版本**

```apkeep -a [com.example.app]@[version] .```

使用账号邮箱和 AAS token 从 **Google Play** 下载

```apkeep -a [com.example.app] -d google-play -e [user@gmail.com] -t [aas_token] .```

从 **F-Droid** 下载

```apkeep -a [com.example.app] -d f-droid .```

列出可用**版本**

```apkeep -a [com.example.app] -l```

批量下载 **CSV 文件**中列出的多个应用

```apkeep -c [apps.csv] .```

# SYNOPSIS

**apkeep** <**-a** _app_id[@version]_ | **-c** _csv_> [_options_] _OUTPATH_

# DESCRIPTION

**apkeep** 可从多个 Android 应用来源下载 APK 文件。它能够获取应用的当前版本或特定的历史版本，适用于安全研究、应用存档，或在没有设备的情况下获取应用。

默认从 APKPure 下载，无需任何凭据。从 Google Play 下载需要账号邮箱和 AAS token。可以用 **-a** 逐个指定应用，也可以用 **-c** 从 CSV 文件批量获取。

# PARAMETERS

**-a, --app** _app_id[@version]_
> 应用 ID，可选附加 @version（例如 com.instagram.android）。

**-c, --csv** _file_
> 列出待批量下载应用 ID 的 CSV 文件。

**-f, --field** _n_
> 包含应用 ID 的 CSV 字段（列）。默认是 **1**。

**-v, --version-field** _n_
> 包含版本号的 CSV 字段。

**-d, --download-source** _source_
> 下载来源：**apk-pure**（默认）、**google-play**、**f-droid**、**huawei-app-gallery**。

**-l, --list-versions**
> 列出应用的可用版本而不是下载。

**-e, --email** _email_
> Google 账号邮箱地址（google-play 必需）。

**-t, --aas-token** _token_
> Google AAS token（google-play 必需）。

**-o, --options** _opts_
> 以逗号分隔的下载源额外选项（例如 arch=arm64-v8a）。

**-r, --parallel** _n_
> 同时运行的并行 APK 抓取数量。默认为 **4**。

**-s, --sleep-duration** _ms_
> 每次下载请求前的等待时长（毫秒）。默认为 **0**。

# CAVEATS

从 Google Play 下载需要有效的账号邮箱和 AAS token；获取方法见项目文档。服务器可能对过量下载进行限速或封锁，请用 **-s** 进行节流。下载的 APK 仍受其原始许可证约束。

# HISTORY

**apkeep** 由 EFF 威胁实验室开发，首个版本发布于 **2021 年**，以 Rust 编写，为存档和安全研究提供访问多个 Android 应用来源的命令行途径。

# INSTALL

```aur: yay -S apkeep```

```brew: brew install apkeep```

```nix: nix profile install nixpkgs#apkeep```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adb](/man/adb)(1), [apktool](/man/apktool)(1), [aapt](/man/aapt)(1)

# RESOURCES

```[Source code](https://github.com/EFForg/apkeep)```

```[Homepage](https://www.eff.org/pages/apkeep)```

<!-- verified: 2026-06-11 -->
