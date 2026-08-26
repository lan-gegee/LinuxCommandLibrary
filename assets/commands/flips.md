# TAGLINE

IPS 与 BPS 补丁的创建与应用

# TLDR

**创建 IPS 补丁**

```flips --create [original.rom] [modified.rom] [patch.ips]```

**应用 IPS 补丁**

```flips --apply [patch.ips] [input.rom] [output.rom]```

**创建 BPS 补丁**

```flips --create --bps [original] [modified] [patch.bps]```

**应用 BPS 补丁**

```flips --apply [patch.bps] [input] [output]```

# SYNOPSIS

**flips** [_options_] [_files_...]

# PARAMETERS

**--create**
> 创建补丁。

**--apply**
> 应用补丁。

**--bps**
> 使用 BPS 格式而非 IPS。

**--exact**
> 创建精确 BPS 补丁（较慢，但保证输出尽可能小）。

**--ips**
> 明确使用 IPS 格式。

# DESCRIPTION

**Flips**（Floating IPS）是一款针对二进制文件的补丁创建与应用工具，常用于 ROM 改造和游戏修改社区。它同时支持传统的 IPS（International Patching System）格式和现代的 BPS（Binary Patching System）格式。

IPS 格式自 1990 年代以来一直是 ROM 补丁的标准，但存在一些局限：16 MB 的文件大小上限以及缺乏错误检测。BPS 解决了这些问题：支持任意大小的文件、内置用于校验的 CRC32 校验和，以及更好的压缩效果从而得到更小的补丁文件。

Flips 通过比较原始文件和修改后的文件来创建补丁，然后应用这些补丁即可复现修改。BPS 格式包含元数据和验证机制，确保补丁正确应用，防止将补丁应用到错误的源文件上导致损坏。

# INSTALL

```pacman: sudo pacman -S flips```

```nix: nix profile install nixpkgs#flips```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bsdiff](/man/bsdiff)(1), [xdelta](/man/xdelta)(1)
