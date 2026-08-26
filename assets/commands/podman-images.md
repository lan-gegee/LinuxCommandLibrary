# TAGLINE

列出本地存储的容器镜像

# TLDR

**列出所有镜像**

```podman images```

**显示摘要列出**

```podman images --digests```

**按引用过滤镜像**

```podman images --filter reference=[nginx*]```

**仅显示镜像 ID**

```podman images -q```

**显示所有镜像**包括中间层

```podman images -a```

**自定义输出格式**

```podman images --format "{{.Repository}}:{{.Tag}} {{.Size}}"```

**列出悬空**（无标签）镜像

```podman images --filter dangling=true```

# SYNOPSIS

**podman images** [_options_] [_repository_[:_tag_]]

# PARAMETERS

**-a**, **--all**
> 显示所有镜像，包括中间镜像层。

**--digests**
> 显示镜像摘要。

**-f**, **--filter** _filter_
> 根据条件过滤输出（key=value 或 key!=value）。

**--format** _format_
> 使用 Go 模板或 'json' 更改输出格式。

**--history**
> 显示镜像名称的历史（在镜像被重新打标签或取消标签时有用）。

**-n**, **--noheading**
> 输出中省略表头。

**--no-trunc**
> 不截断输出（显示完整的镜像 ID）。

**-q**, **--quiet**
> 仅显示镜像 ID。

**--sort** _field_
> 排序依据：created、id、repository、size 或 tag（默认：created）。

# DESCRIPTION

**podman images** 列出本地存储的容器镜像。它会显示每个镜像的仓库、标签、镜像 ID、创建日期和大小。

# EXAMPLES

```bash
# List all images
podman images

# With full IDs
podman images --no-trunc

# Filter dangling images
podman images --filter dangling=true

# Custom format
podman images --format "{{.Repository}}:{{.Tag}} {{.Size}}"

# Filter by label
podman images --filter label=maintainer=me

# Sort by size
podman images --sort size
```

# FILTERS

```
dangling=true        - Untagged images (<none> tag)
reference=name:tag   - Match image reference pattern
before=image         - Created before specified image
since=image          - Created after specified image
label=key=value      - Has label (also supports label!=key)
id=image_id          - Match image ID
containers=true      - Images with running containers
intermediate=true    - Intermediate build layers
readonly=true        - Read-only images
```

# CAVEATS

显示的大小可能在镜像之间共享。使用 --all 可查看中间层。

# HISTORY

podman images 是 **Red Hat** 的 **Podman** 的一部分，提供与 Docker 兼容的镜像列表功能。

# INSTALL

```apt: sudo apt install podman```

```dnf: sudo dnf install podman```

```pacman: sudo pacman -S podman```

```apk: sudo apk add podman```

```zypper: sudo zypper install podman```

```brew: brew install podman```

```nix: nix profile install nixpkgs#podman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman-pull](/man/podman-pull)(1), [podman-rmi](/man/podman-rmi)(1), [podman-image](/man/podman-image)(1), [podman-build](/man/podman-build)(1), [podman-ps](/man/podman-ps)(1), [docker-images](/man/docker-images)(1)
