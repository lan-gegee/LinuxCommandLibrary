# TAGLINE

从 iCloud 照片下载照片和视频

# TLDR

**下载**到目录

```icloudpd --directory [~/Photos] --username [apple_id]```

仅下载**最近**的照片

```icloudpd --directory [~/Photos] --username [user] --recent [100]```

只**列出**而不下载

```icloudpd --directory [~/Photos] --username [user] --only-print-filenames```

# SYNOPSIS

**icloudpd** [*options*]

# DESCRIPTION

**icloudpd**（iCloud Photos Downloader）向 Apple iCloud 进行身份验证，并将照片图库下载到本地文件夹，支持最近项目数量、相册过滤以及跳过已存在文件等选项。可通过 PyPI 或 **icloud-photos-downloader/icloud_photos_downloader** 提供的 Docker 镜像安装。

# PARAMETERS

**--directory** *path*

> 目标文件夹。

**--username** *apple_id*

> Apple ID 电子邮箱。

**--recent** *n*

> 仅限于最近的 *n* 个资产。

**--until-found** *n*

> 连续遇到 *n* 个已存在的文件后停止。

需要时会出现 MFA/2FA 交互提示。线程数和实况照片（Live Photo）处理方式参见 **icloudpd --help**。

# CAVEATS

Apple 的身份验证和 MFA 流程经常变化，请保持工具更新。请尊重账户安全——优先使用官方文档推荐的应用专用处理方式。大型图库需要足够的磁盘空间和时间。

# INSTALL

```brew: brew install icloudpd```

```nix: nix profile install nixpkgs#icloudpd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rclone](/man/rclone)(1), [gphotos-uploader-cli](/man/gphotos-uploader-cli)(1)

# RESOURCES

```[Source code](https://github.com/icloud-photos-downloader/icloud_photos_downloader)```

<!-- verified: 2026-07-19 -->
