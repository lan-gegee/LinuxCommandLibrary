# TAGLINE

替换镜像的基础层

# TLDR

**将镜像变基到新的基础镜像**

```crane rebase [image:tag] --old_base [old:base] --new_base [new:base] -t [rebased:tag]```

**针对特定平台进行变基**

```crane rebase [image:tag] --old_base [old:base] --new_base [new:base] --platform [linux/amd64]```

# SYNOPSIS

**crane** **rebase** [_options_] _image_

# PARAMETERS

**--old_base** _image_
> 要移除的旧基础镜像。

**--new_base** _image_
> 要插入的新基础镜像。

**-t**, **--tag** _tag_
> 应用于变基后镜像的标签。

**--platform** _platform_
> 以 `os/arch[/variant][:osversion]` 形式指定的平台（例如 `linux/amd64`）。默认为全部。

**--allow-nondistributable-artifacts**
> 允许推送不可分发（foreign）的层。

**--insecure**
> 允许在不使用 TLS 的情况下获取镜像引用。

# DESCRIPTION

**crane rebase** 用另一个基础镜像的层替换镜像的基础层。这适用于不重新构建就更新基础镜像的场景，例如当基础层发现漏洞而需要快速修补大量镜像时。

只有在层栈中"基础"层与"应用"层之间遵循关于基础层产出约定的边界处进行变基才是安全的。

# CAVEATS

要求旧的基础层与镜像中的层完全匹配。如果镜像构建时对基础层做过修改，则可能无法工作。建议先将变基后的镜像打上不同的标签，执行可信度检查后再重新打标签。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-mutate](/man/crane-mutate)(1), [crane-cp](/man/crane-cp)(1)
