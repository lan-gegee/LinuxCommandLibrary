# TAGLINE

安装软件包及其依赖

# TLDR

**安装所有依赖**

```npm install```

**安装指定软件包**

```npm install [package]```

**安装为开发依赖**

```npm install -D [package]```

**安装指定版本**

```npm install [package]@[version]```

**全局安装**

```npm install -g [package]```

**从 git 安装**

```npm install [git+https://github.com/user/repo.git]```

**全新安装（CI）**

```npm ci```

# SYNOPSIS

**npm install** [_options_] [_packages_...]

# PARAMETERS

**-D**, **--save-dev**
> 保存为 devDependency。

**-g**, **--global**
> 全局安装。

**-E**, **--save-exact**
> 保存精确版本。

**--no-save**
> 不更新 package.json。

**--legacy-peer-deps**
> 忽略 peer 依赖冲突。

**--force**
> 强制拉取软件包。

# DESCRIPTION

**npm install**（或 npm i）安装软件包及其依赖。不带参数时，会安装 package.json 中的全部内容；带软件包名时，则将其添加到项目中。

# VERSION RANGES

```bash
npm install lodash         # Latest
npm install lodash@4.17.0  # Exact
npm install lodash@^4.0.0  # Compatible
npm install lodash@~4.17.0 # Patch updates
```

# CAVEATS

在 CI/CD 中 npm ci 更快。peer 依赖在 npm 7 及以上版本可能引发问题。lock 文件应当提交到版本库。

# HISTORY

自 **Isaac Schlueter** 于 **2010 年**为 Node.js 软件包管理创建 npm 以来，npm install 就一直是 npm 的核心命令。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-ci](/man/npm-ci)(1), [npm-uninstall](/man/npm-uninstall)(1), [yarn](/man/yarn)(1)
