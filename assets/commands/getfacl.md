# TAGLINE

文件访问控制列表查看器

# TLDR

**显示** ACL

```getfacl path/to/file```

以**数字** ID 显示

```getfacl -n path/to/file```

**表格**输出

```getfacl -t path/to/file```

# SYNOPSIS

**getfacl** [_OPTIONS_] _files_...

# DESCRIPTION

**getfacl** 显示文件的访问控制列表（ACL）。ACL 提供比传统 Unix 权限更细粒度的访问控制，允许在所有者/组/其他之外为特定用户和组设置权限。

# PARAMETERS

**-n, --numeric**
> 以数字形式显示用户和组 ID

**-t, --tabular**
> 使用表格输出格式

**-a, --access**
> 显示访问 ACL

**-d, --default**
> 显示默认 ACL

**-R, --recursive**
> 递归进入目录

**-p, --absolute-names**
> 不去除开头的斜杠

# CAVEATS

文件系统必须支持 ACL（挂载时使用 acl 选项）。默认 ACL 仅适用于目录，并影响其中新建的文件。修改 ACL 请使用 setfacl。

# HISTORY

**getfacl** 是 **acl** 软件包的一部分，在 Linux 上提供 POSIX ACL 支持。

# INSTALL

```apt: sudo apt install acl```

```dnf: sudo dnf install acl```

```pacman: sudo pacman -S acl```

```apk: sudo apk add acl```

```zypper: sudo zypper install acl```

```brew: brew install acl```

```nix: nix profile install nixpkgs#acl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[setfacl](/man/setfacl)(1), [chmod](/man/chmod)(1)

# RESOURCES

```[Homepage](https://savannah.nongnu.org/projects/acl/)```

```[Documentation](https://manpages.debian.org/getfacl)```

<!-- verified: 2026-07-15 -->
