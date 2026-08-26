# TAGLINE

移除文件元数据以保护隐私

# TLDR

**移除文件中的元数据**

```mat2 [file.jpg]```

**检查元数据**（不修改文件）

```mat2 --show [file.pdf]```

**原地移除元数据**

```mat2 --inplace [file.docx]```

**处理目录中的所有文件**

```mat2 [*.jpg]```

**轻量清理**（更快，但不够彻底）

```mat2 --lightweight [video.mp4]```

**列出支持的格式**

```mat2 --list```

**检查依赖**

```mat2 --check-dependencies```

# SYNOPSIS

**mat2** [_-s_] [_--inplace_] [_-L_] [_options_] _files_

# PARAMETERS

**-s**, **--show**
> 列出 mat2 可检测到的有害元数据，但不移除它们。

**--inplace**
> 原地清理文件，不创建备份。

**-L**, **--lightweight**
> 移除部分元数据，以牺牲彻底性换取不修改文件数据的保证。

**-l**, **--list**
> 列出所有支持的文件格式。

**--check-dependencies**
> 检查 mat2 是否具备所需的全部依赖。

**--no-sandbox**
> 禁用 bubblewrap 的沙盒机制。

**--unknown-members** _POLICY_
> 处理归档类文件中未知成员的策略（abort、omit、keep）。

**-V**, **--verbose**
> 显示更详细的状态信息。

**-v**, **--version**
> 显示版本号并退出。

**-h**, **--help**
> 显示帮助信息并退出。

# DESCRIPTION

**mat2**（Metadata Anonymisation Toolkit 2）通过移除文件元数据来保护隐私。它会清除图片、文档、音频和视频中的身份识别信息。

图片可能包含 EXIF 数据，其中有相机型号、GPS 坐标、时间戳和所用软件。文档会嵌入作者姓名、修订历史和编辑时间。音频文件包含艺术家、编码软件和录制细节。

默认情况下，mat2 会创建清理后的副本，在文件名与扩展名之间插入 `.cleaned`（例如 `file.cleaned.jpg`）。inplace 模式直接修改原文件。show 选项只显示元数据而不做修改。

支持的格式包括 JPEG、PNG、PDF、DOCX、ODT、MP3、MP4、FLAC 等。归档格式（ZIP、TAR）会被递归处理。

对于视频等完整处理较慢的格式，轻量模式可以提供更快的清理速度，代价是元数据移除不够彻底。

# CAVEATS

某些元数据不经重新编码无法移除（如视频）。非常彻底的清理可能改变文件特征。某些特定格式的元数据可能残留。并非支持所有格式。

# HISTORY

**mat2** 是 **Tails** 项目创建的原始 MAT（Metadata Anonymisation Toolkit）的继任者。由 **Julien Voisin** 于 **2018 年**重写，改进了格式支持和可靠性。它被记者、活动人士和注重隐私的用户广泛使用。

# INSTALL

```dnf: sudo dnf install mat2```

```pacman: sudo pacman -S mat2```

```brew: brew install mat2```

```nix: nix profile install nixpkgs#mat2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[exiftool](/man/exiftool)(1), [exiv2](/man/exiv2)(1), [pdfinfo](/man/pdfinfo)(1), [ffprobe](/man/ffprobe)(1)
