# TAGLINE

将 GEM IMG 格式转换为 PBM

# TLDR

**将 GEM IMG 转换为 PBM**

```gemtopbm [input.img] > [output.pbm]```

# SYNOPSIS

**gemtopbm** [_input_]

# DESCRIPTION

**gemtopbm** 是一个格式转换实用程序，用于将 GEM IMG 格式图像转换为 PBM（Portable Bitmap）格式。GEM IMG 是 Digital Research 的 GEM（Graphics Environment Manager）操作系统和桌面环境所使用的原生位图图像格式，流行于 20 世纪 80 年代和 90 年代初，尤其是在 Atari ST 计算机上。

该工具是 Netpbm 图像转换实用程序套件的一部分，可将遗留的 GEM 图像融入现代工作流程。转换为简单可移植的 PBM 格式后，GEM 图像就可以用其他 Netpbm 工具进一步处理或转换成当代格式。

这个转换器主要用于数字保存、复古计算爱好者，以及所有处理 GEM 时代历史计算机图形的人。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pbmtogem](/man/pbmtogem)(1), [gemtopnm](/man/gemtopnm)(1)

# RESOURCES

```[Homepage](https://netpbm.sourceforge.net/)```

```[Documentation](https://netpbm.sourceforge.net/doc/gemtopnm.html)```

<!-- verified: 2026-07-15 -->
