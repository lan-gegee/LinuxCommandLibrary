# TAGLINE

从 PKGBUILD 文件创建 Arch Linux 软件包

# TLDR

**Build** 软件包

```makepkg```

Build 并**安装依赖**

```makepkg --syncdeps```

Build、安装依赖并**安装软件包**

```makepkg -si```

Build 时**跳过校验和**

```makepkg --skipchecksums```

构建后 **Clean**（清理）

```makepkg --clean```

**Verify**（校验）源文件校验和

```makepkg --verifysource```

Generate **.SRCINFO**

```makepkg --printsrcinfo > .SRCINFO```

只下载源码和**依赖**

```makepkg -so```

# SYNOPSIS

**makepkg** [_options_]

# DESCRIPTION

**makepkg** 从 PKGBUILD 文件创建 Arch Linux 软件包。它会下载源码、验证校验和、编译软件，并创建可供 pacman 安装的软件包。

# PARAMETERS

**-s, --syncdeps**
> 使用 pacman 安装缺失的依赖

**-i, --install**
> 构建后安装软件包

**-c, --clean**
> 构建后清理工作文件

**-f, --force**
> 覆盖已存在的软件包

**--skipchecksums**
> 跳过源文件校验和验证

**--verifysource**
> 验证源文件校验和

**--printsrcinfo**
> 将 .SRCINFO 打印到 stdout

**--nobuild**
> 只下载源码但不构建

**--noextract**
> 不解压源码

**-r, --rmdeps**
> 构建成功后移除已安装的依赖

**-g, --geninteg**
> 为源文件生成完整性检查

**-p** _buildscript_
> 读取指定的构建脚本而不是 PKGBUILD

**--nocheck**
> 不运行 PKGBUILD 中的 check() 函数

**--sign**
> 使用 gpg 对生成的软件包签名

**--holdver**
> 不更新 VCS 源

# CAVEATS

必须在包含 PKGBUILD 的目录中运行。切勿以 root 身份运行。安装依赖需要访问 pacman。

# INSTALL

```apt: sudo apt install makepkg```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```brew: brew install makepkg```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [yay](/man/yay)(1), [paru](/man/paru)(1)
