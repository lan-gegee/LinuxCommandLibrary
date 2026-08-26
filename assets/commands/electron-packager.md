# TAGLINE

打包 Electron 应用以便分发

# TLDR

**为当前平台打包**

```electron-packager [.] [app_name]```

**为特定平台打包**

```electron-packager [.] [app_name] --platform=[darwin] --arch=[x64]```

**为所有平台打包**

```electron-packager [.] [app_name] --all```

**指定图标**

```electron-packager [.] [app_name] --icon=[icon.icns]```

**指定输出目录**

```electron-packager [.] [app_name] --out=[dist]```

**覆盖已有构建产物**

```electron-packager [.] [app_name] --overwrite```

# SYNOPSIS

**electron-packager** _sourcedir_ _appname_ [_options_]

# PARAMETERS

**--platform** _platform_
> 目标平台（darwin、linux、win32、mas）。

**--arch** _arch_
> 目标架构（x64、arm64、ia32）。

**--all**
> 为所有平台构建。

**--icon** _path_
> 应用图标。

**--out** _directory_
> 输出目录。

**--overwrite**
> 覆盖已有的输出。

**--asar**
> 打包为 ASAR 归档。

**--prune**
> 移除 devDependencies。

# DESCRIPTION

**electron-packager** 将 Electron 应用打包以便分发。它从源代码创建 macOS、Windows 和 Linux 的独立可执行文件。

# INSTALL

```pacman: sudo pacman -S electron```

```nix: nix profile install nixpkgs#electron```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[electron](/man/electron)(1)
