# TAGLINE

基于 EXIF 的照片、视频和音频整理器

# TLDR

**导入**文件到目标媒体库

```elodie.py import --destination=["/path/to/library"] ["/path/to/photos"]```

**试运行**导入（不做任何更改）

```elodie.py import --dry-run --destination=["/path/to/library"] ["/path/to/photos"]```

**在 EXIF 缺失位置信息时**导入并设置位置

```elodie.py import --destination=["/path/to/library"] --location=["Las Vegas, NV"] ["/path/to/photos"]```

**更新**位置 EXIF 并重新整理

```elodie.py update --location=["Las Vegas, NV"] [file.jpg]...```

**更新**拍摄时间

```elodie.py update --time=["2015-04-15"] [file.jpg]...```

**重新生成**校验和数据库

```elodie.py generate-db --source=["/path/to/library"]```

**校验**媒体库是否发生位腐坏（bit rot）

```elodie.py verify```

**运行**插件批量操作（试运行）

```elodie.py batch --dry-run```

# SYNOPSIS

**elodie.py** *command* [*options*] [*paths*...]

# DESCRIPTION

**Elodie** 是一个基于 EXIF 的个人照片、视频和音频整理助手。它读取元数据（通过 **ExifTool**），将媒体复制到结构化的媒体库中，可以更新位置/时间/标题/相册标签，并可在导入后选择性地把原文件移入回收站。

仓库中的主入口是 **elodie.py**（在克隆后执行 **pip install -r requirements.txt** 再运行）。PATH 中必须有 **ExifTool**（用 **exiftool -ver** 检查）；视频功能需要 ExifTool 10.20+，HEIC 需要 11.50+，地理位置到城市的转换需要 13.13+。

媒体库的布局和命名可通过 **~/.elodie/config.ini**（或 **ELODIE_APPLICATION_DIRECTORY**）配置。**~/.elodie/** 下的 **hash.json** 记录 SHA-256 签名，用于重复检测和 **verify**。

# PARAMETERS

**import** [*paths*...]
> 将媒体复制到必需的 **--destination** 中，读取 EXIF。选项包括 **--source**、**--file**、**--album-from-folder**、**--trash**、**--allow-duplicates**、**--location**、**--time**、**--exclude-regex**、**--debug**、**--dry-run**。

**update** *files*...
> 更新 EXIF 并重新整理。选项：**--album**、**--location**、**--time**、**--title**、**--debug**、**--dry-run**。

**generate-db**
> 从必需的 **--source** 重建 **hash.json**。

**batch**
> 为所有插件运行 **batch()**（**--debug**、**--dry-run**）。

**verify**
> 对照存储的校验和检查媒体库是否发生位腐坏。

完整选项说明请使用 elodie.py *command* **--help** 查看。

# CONFIGURATION

将 **config.ini** 放在 **~/.elodie/**（或 **ELODIE_APPLICATION_DIRECTORY** 之下）。其中的节可定义自定义文件夹/文件路径模板以及 **[Exclusions]** 模式。命令行的 **--exclude-regex** 也会在导入时跳过匹配的路径。提供 **--location** / **--time** 时会在导入时覆盖现有 EXIF；在数据缺失或确定有误时使用它们。

# CAVEATS

依赖系统上的 ExifTool；ExifTool 缺失或版本过旧会限制支持的格式和地理定位功能。MapQuest 集成已被弃用，推荐使用 ExifTool。批量导入前务必先用 **--dry-run**。默认导入方式是**复制**文件；**--trash** 会在成功后将源文件移走。

# SEE ALSO

[exiftool](/man/exiftool)(1), [exif](/man/exif)(1), [rsync](/man/rsync)(1)

# RESOURCES

```[Source code](https://github.com/jmathai/elodie)```

<!-- verified: 2026-07-19 -->
