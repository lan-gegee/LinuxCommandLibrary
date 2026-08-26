# TAGLINE

按照将要发布的样子创建软件包的 tarball

# TLDR

**打包当前软件包**

```npm pack```

**打包指定软件包**

```npm pack [package]```

**指定输出目录打包**

```npm pack --pack-destination [./dist]```

**试运行（列出内容）**

```npm pack --dry-run```

**以 JSON 格式输出**

```npm pack --json```

# SYNOPSIS

**npm pack** [_options_] [_packages_...]

# PARAMETERS

**--dry-run**
> 只显示内容而不实际打包。

**--json**
> 以 JSON 格式输出。

**--pack-destination** _dir_
> 输出目录。

**--workspace** _ws_
> 打包指定的工作区。

# DESCRIPTION

**npm pack** 按照将要发布的样子创建软件包的 tarball。适合用来测试发布的软件包里会包含哪些内容。

该 tarball 可以在本地安装，用于测试软件包。

# WORKFLOW

```bash
# Create tarball
npm pack
# Creates package-1.0.0.tgz

# Test installation
npm install ./package-1.0.0.tgz

# Check contents without creating file
npm pack --dry-run
```

# FILES INCLUDED

```
- Files in package.json "files"
- package.json
- README
- LICENSE
- CHANGELOG
Excluded by .npmignore
```

# CAVEATS

与 npm publish 不同。遵循 .npmignore 和 files 字段。适合发布前的测试。

# HISTORY

npm pack 的加入是为了让开发者在发布到 registry 之前测试软件包的内容。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-publish](/man/npm-publish)(1), [npm-install](/man/npm-install)(1)
