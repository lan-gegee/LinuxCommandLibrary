# TAGLINE

先运行 npm ci 再运行 npm test

# TLDR

**全新安装并测试**

```npm install-ci-test```

**简写形式**

```npm cit```

**另一个别名**

```npm sit```

**跳过生命周期脚本的执行**

```npm install-ci-test --ignore-scripts```

# SYNOPSIS

**npm install-ci-test**

# DESCRIPTION

**npm install-ci-test** 是一个组合命令，先运行 **npm ci** 再运行 **npm test**。它面向持续集成流水线：先保证从 **package-lock.json** 进行干净、可重现的安装，然后立即执行项目的测试套件。

别名：**cit**、**clean-install-test**、**sit**。

# CAVEATS

与 **npm ci** 一样，该命令要求已存在 **package-lock.json** 或 **npm-shrinkwrap.json**，并且会在安装前删除现有的 **node_modules** 目录。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-ci](/man/npm-ci)(1), [npm-test](/man/npm-test)(1)
