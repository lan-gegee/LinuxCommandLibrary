# TAGLINE

简单的 OpenGL 渲染测试

# TLDR

**运行 OpenGL 演示**

```glxdemo```

# SYNOPSIS

**glxdemo**

# DESCRIPTION

**glxdemo** 是一个简单的 OpenGL 演示程序，展示如何使用 GLX 函数创建运行在 X server 之上的 OpenGL 程序。它会打开一个窗口并渲染一个基础 3D 场景，以验证系统上的 OpenGL 渲染是否正常工作。

这个程序最有价值的用法是研究它的源代码。如果它能成功运行，说明 OpenGL 加速已正确配置。

# CAVEATS

需要 X11 和 OpenGL。属于 mesa-utils（或 mesa-demos）的一部分。仅作基础功能测试；不接受任何命令行选项。

# HISTORY

glxdemo 是 **Mesa demos** 的一部分，后者为 Linux/Unix 系统上的 OpenGL 渲染测试提供了多个简单程序。

# INSTALL

```apt: sudo apt install mesa-utils```

```dnf: sudo dnf install mesa-demos```

```pacman: sudo pacman -S mesa-utils```

```apk: sudo apk add mesa-demos```

```nix: nix profile install nixpkgs#mesa-demos```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[glxinfo](/man/glxinfo)(1), [glxgears](/man/glxgears)(1)
