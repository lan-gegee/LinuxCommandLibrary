# TAGLINE

为新软件包设置默认作者的配置

# TLDR

**设置作者姓名**

```npm config set init-author-name "[Your Name]"```

**设置作者邮箱**

```npm config set init-author-email "[email@example.com]"```

**设置作者 URL**

```npm config set init-author-url "[https://example.com]"```

**查看作者配置**

```npm config get init-author-name```

# SYNOPSIS

**npm** **config** **set** **init-author-**_field_ _value_

# PARAMETERS

**init-author-name**
> 软件包作者姓名。

**init-author-email**
> 软件包作者邮箱。

**init-author-url**
> 软件包作者 URL。

**init-license**
> 新软件包的默认 SPDX 许可证 ID（默认：`ISC`）。

**init-version**
> 新软件包的默认 semver 版本（默认：`1.0.0`）。

# DESCRIPTION

**npm-author** 是一个配置概念而非独立的子命令：它指的是 **npm init**（以及 **npm create**）在填充新 `package.json` 的 `author` 字段时读取的 `init-author-*` 配置项。

用 **npm config set** 设置一次这些值——通常写在用户级的 `~/.npmrc` 中——之后初始化新软件包时就无需重复输入。也可以通过项目本地的 `.npmrc` 按项目单独设置。

这些配置项默认未设置；若为空，`npm init` 会以交互方式提示输入。

# CAVEATS

属于 npm config 子命令。仅影响 npm init。可全局或按项目设置。

# HISTORY

作者配置是 **npm** 用于创建 package.json 的 init 默认值体系的一部分。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-config](/man/npm-config)(1), [npm-init](/man/npm-init)(1)
