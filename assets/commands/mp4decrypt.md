# TAGLINE

解密被加密的 MP4 文件

# TLDR

使用轨道 ID 和密钥**解密** MP4 文件

```mp4decrypt --key [track_id]:[hex_key] [input.mp4] [output.mp4]```

对 MPEG-CENC 内容使用 **KID**（Key ID）和密钥**解密**

```mp4decrypt --key [hex_kid]:[hex_key] [input.mp4] [output.mp4]```

为独立的音频和视频轨道使用**多个密钥****解密**

```mp4decrypt --key 1:[hex_key1] --key 2:[hex_key2] [input.mp4] [output.mp4]```

配合单独的 init 文件**解密**分片 MP4 段

```mp4decrypt --fragments-info [init.mp4] --key 1:[hex_key] [segment.m4s] [output.m4s]```

**解密**时显示**进度**

```mp4decrypt --show-progress --key 1:[hex_key] [input.mp4] [output.mp4]```

# SYNOPSIS

**mp4decrypt** [_options_] _input_ _output_

# PARAMETERS

**--key** _\<id\>_:_\<key\>_
> 指定解密密钥。_id_ 可以是轨道 ID（十进制）或 128 位 KID（十六进制）。_key_ 是十六进制表示的 128 位解密密钥。可为不同轨道多次指定。

**--fragments-info** _\<filename\>_
> 使用来自另一个文件的轨道信息解密分片。用于分片式 MP4 工作流（DASH/HLS 分段）。

**--show-progress**
> 解密过程中显示进度详情

# DESCRIPTION

**mp4decrypt** 用于解密采用内容保护方案加密的 MP4 文件。它是 **Bento4** SDK 的一部分——这是一个跨平台的 C++ 工具包，用于处理 ISO-MP4 文件、MPEG-DASH、HLS 和 CMAF。它是 **mp4encrypt** 的解密对应工具。

该工具从输入文件的元数据自动检测加密方案。支持的方案包括 **MPEG-CENC**（AES-CTR）、**MPEG-CBCS**（AES-CBC 子采样模式）、**PIFF**（Microsoft PlayReady）、**OMA-PDCF**、**Marlin IPMP** 和 **ISMACRYP**。这些涵盖了业界常用的 DRM 系统：Widevine、PlayReady、FairPlay 和 Marlin。

对于 **OMA DCF** 文件，轨道索引请使用 **1**。对于 **Marlin IPMP/ACGK** 加密，轨道 ID 请使用 **0**。KID（十六进制 Key ID）仅适用于 **MPEG-CENC** 系列加密。

# CAVEATS

你必须自行提供解密密钥；mp4decrypt 不会获取、推导或破解密钥。解密分片式 MP4 分段时，若省略 **--fragments-info**，可能产生 0 字节的输出文件，某些情况下工具还可能静默生成实际上并未解密的输出。在若干失败场景下（密钥错误、Key ID 格式错误），mp4decrypt 可能不报错就生成输出文件。开源版本采用 **GPLv2** 许可证并有 copyleft 要求；商业使用需要向 Axiomatic Systems 单独获取许可。

# HISTORY

**mp4decrypt** 是 **Axiomatic Systems, LLC** 的 **Gilles Boccon-Gibod** 所创建的 **Bento4** 工具集的一部分，其开发可追溯到 **2002 年**。该工具集于 **2005 年**前后首次在 SourceForge 上公开发布，此后持续扩展以支持现代加密方案（MPEG-CENC、CBCS）和自适应串流格式（DASH、HLS、CMAF）。它已被 **Dolby Laboratories** 和 **XBMC/Kodi** fork。

# INSTALL

```apk: sudo apk add bento4```

```brew: brew install bento4```

```nix: nix profile install nixpkgs#bento4```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [ffprobe](/man/ffprobe)(1)
