# TAGLINE

管理 Nix store

# TLDR

**查询软件包的依赖**

```nix-store -q --references [/nix/store/...path]```

**查询反向依赖**

```nix-store -q --referrers [/nix/store/...path]```

**显示依赖树**

```nix-store -q --tree [/nix/store/...path]```

**执行垃圾回收**

```nix-store --gc```

**优化 store**

```nix-store --optimise```

**校验 store 完整性**

```nix-store --verify --check-contents```

# SYNOPSIS

**nix-store** _operation_ [_options_] [_paths_...]

# PARAMETERS

**-q**, **--query**
> 查询模式。

**--gc**
> 执行垃圾回收。

**--optimise**
> 对 store 进行去重。

**--verify**
> 校验 store 完整性。

**--references**
> 显示依赖项。

**--referrers**
> 显示反向依赖。

**--tree**
> 显示依赖树。

**--delete**
> 删除路径。

# DESCRIPTION

**nix-store** 管理 Nix store（/nix/store）。它负责垃圾回收、优化、查询以及各种 store 维护操作。

Nix store 把所有软件包及其依赖保存为不可变的路径。

# STORE LAYOUT

```
/nix/store/
├── hash-name/           # Package paths
├── hash-name.drv        # Derivations
└── .links/              # Hard link pool
```

# CAVEATS

不要手动修改 /nix/store。垃圾回收只会移除无引用的路径。优化操作利用硬链接实现。

# HISTORY

nix-store 是一款核心 **Nix** 工具，自项目诞生之初就负责提供对 Nix store 的底层访问。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix-env](/man/nix-env)(1), [nix-build](/man/nix-build)(1), [nix-collect-garbage](/man/nix-collect-garbage)(1)
