# TAGLINE

Portable Anymap 图像格式家族

# TLDR

**查看 PNM 信息**

```pnmfile [image.pnm]```

**转换为其他格式**

```pnmtopng [image.pnm] > [image.png]```

**从其他格式转换**

```pngtopnm [image.png] > [image.pnm]```

# SYNOPSIS

用于处理 PNM 图像的各种 **pnm*** 工具。

# PARAMETERS

PNM 格式包括：
- PBM（位图）
- PGM（灰度）
- PPM（彩色）

属于 Netpbm 工具集。

# DESCRIPTION

**PNM**（Portable Anymap）是 Netpbm 图像格式家族的统称：PBM（位图、黑白）、PGM（灰度图、灰度）和 PPM（像素图、彩色）。这些格式使用简单、人类可读的文件头，其后是以 ASCII 或二进制编码存储的像素数据。

PNM 在 Netpbm 工具集中扮演中间格式的角色：图像先被转换为 PNM，用各种 pnm* 工具处理后，再转换为目标输出格式。PNM 的简单性使它很容易通过编程生成和解析。

# CAVEATS

PNM 文件不做压缩，与 PNG 或 JPEG 等格式相比体积可能很大。“Netpbm 格式”这一更宽泛的说法还包含 PAM。没有注册官方 MIME 类型；惯例上使用 image/x-portable-anymap。

# HISTORY

PNM 作为 **Netpbm** 项目的一部分诞生，最初源自 Jef Poskanzer 的 **Pbmplus** 工具集（1988 年）。Netpbm 至今仍作为开源软件包持续维护，服务于便携的图像处理。

# SEE ALSO

[pbm](/man/pbm)(5), [pgm](/man/pgm)(5), [ppm](/man/ppm)(5), [netpbm](/man/netpbm)(1)
