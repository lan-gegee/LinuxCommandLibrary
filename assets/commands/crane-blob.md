# TAGLINE

从容器镜像中获取 blob

# TLDR

**获取镜像的某个 blob**

```crane blob [image]@[digest]```

**将 blob 保存到文件**

```crane blob [image]@[sha256:abc...] > [blob.tar.gz]```

# SYNOPSIS

**crane** **blob** [_options_] _image@digest_

# DESCRIPTION

**crane blob** 按摘要（digest）从容器镜像中检索特定的 blob。blob 通常是层或配置对象。

输出写入 stdout；可通过重定向保存到文件。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-manifest](/man/crane-manifest)(1)

# RESOURCES

```[Source code](https://github.com/google/go-containerregistry)```

```[Documentation](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_blob.md)```

<!-- verified: 2026-06-26 -->
