# TAGLINE

输出 npm 安装可执行文件的文件夹

# TLDR

**显示本地 bin 目录**

```npm bin```

**显示全局 bin 目录**

```npm bin -g```

**将本地 bin 加入 PATH**

```export PATH="$(npm bin):$PATH"```

# SYNOPSIS

**npm bin** [_options_]

# PARAMETERS

**-g**, **--global**
> 显示全局 bin 目录。

# DESCRIPTION

**npm bin** 输出 npm 安装可执行文件的文件夹。本地安装时通常是 ./node_modules/.bin；全局安装时则取决于 npm prefix。

把本地 bin 加入 PATH 后即可运行本地安装的工具。

# EXAMPLE USAGE

```bash
# Show local bin
npm bin
# Output: /project/node_modules/.bin

# Show global bin
npm bin -g
# Output: /usr/local/bin

# Run local binary
$(npm bin)/eslint .

# Or add to PATH
export PATH="$(npm bin):$PATH"
eslint .
```

# ALTERNATIVES

```bash
# Use npx instead
npx eslint .

# Or npm exec
npm exec eslint .
```

# CAVEATS

本地 bin 随项目而变。全局路径因安装方式而异。运行可执行文件时 npx 通常更简单。

# HISTORY

npm bin 自早期版本起就是 npm 的一部分，帮助开发者定位并使用本地安装的可执行文件。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npx](/man/npx)(1), [npm-exec](/man/npm-exec)(1), [npm-prefix](/man/npm-prefix)(1)
