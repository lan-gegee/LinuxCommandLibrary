# TAGLINE

将 blob 内容提取到临时文件

# TLDR

**将 blob 解包到临时文件**

```git unpack-file [blob_hash]```

# SYNOPSIS

**git** **unpack-file** _blob_

# DESCRIPTION

**git unpack-file** 创建一个包含指定 blob 内容的临时文件，并打印该文件名。它是一个底层（plumbing）命令，用于在工作树之外访问 blob 内容；Git 在合并过程中内部会用到它，需要直接访问 blob 数据的脚本也会使用。

# CAVEATS

会在当前目录创建名为 **.merge_file_XXXXXX** 的文件。Git 不会自动删除它；调用者负责在用完后将其删除。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-cat-file](/man/git-cat-file)(1), [git-hash-object](/man/git-hash-object)(1)

# RESOURCES

```[Documentation](https://git-scm.com/docs/git-unpack-file)```

```[Source code](https://github.com/git/git)```

<!-- verified: 2026-07-17 -->
