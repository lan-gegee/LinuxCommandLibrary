# TAGLINE

导出扁平化的镜像文件系统

# TLDR

**将镜像文件系统导出**为 tar 包

```crane export [image] [output.tar]```

**导出到 stdout**

```crane export [image] - | tar -tvf -```

# SYNOPSIS

**crane** **export** [_options_] _image_ _output_

# DESCRIPTION

**crane export** 将容器镜像的文件系统导出为 tar 包。它会把所有层压平为单个归档，代表最终的文件系统状态。

将 **-** 用作输出目标即可写入 stdout。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-pull](/man/crane-pull)(1)

# RESOURCES

```[Source code](https://github.com/google/go-containerregistry)```

```[Documentation](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_export.md)```

<!-- verified: 2026-06-26 -->
