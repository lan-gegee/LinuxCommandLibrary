# TAGLINE

从模板创建 Vue.js 项目

# TLDR

从 webpack 模板**创建项目**

```vue init webpack [project-name]```

从 simple 模板（无构建步骤）**创建项目**

```vue init simple [project-name]```

**从本地模板目录创建**

```vue init [~/my-template] [project-name]```

**从 GitHub 仓库模板创建**

```vue init [username/repo] [project-name]```

**用克隆代替下载**模板

```vue init --clone [username/repo] [project-name]```

**使用缓存的模板**（离线模式）

```vue init --offline [webpack] [project-name]```

# SYNOPSIS

**vue** **init** [_options_] _template_ _project-name_

# PARAMETERS

_template_
> 模板名称。内置模板包括 webpack、webpack-simple、browserify、browserify-simple、pwa 和 simple。也可以是 GitHub 仓库（user/repo）或本地路径。

_project-name_
> 新项目目录的名称。

**--clone**
> 使用 git clone 而不是下载 zip 压缩包。

**--offline**
> 使用之前缓存的模板而不是重新下载。

# DESCRIPTION

**vue init** 从模板创建新的 Vue.js 项目。这是 **Vue CLI 2.x**（软件包：**vue-cli**）的遗留命令。对于 **Vue CLI 3+**（软件包：**@vue/cli**），请改用 **vue create**。

该命令对于托管在 GitHub 上或保存在本地的自定义项目模板仍然有用。要在 Vue CLI 3+ 中使用它，需安装 **@vue/cli-init** 桥接包。

# CAVEATS

这是 Vue CLI 2.x 的命令。Vue CLI 3+ 创建新项目使用 **vue create**。内置模板（webpack、browserify 等）已不再维护。要在 **@vue/cli** 3+ 中使用 **vue init**，需全局安装 **@vue/cli-init**。

# INSTALL

```nix: nix profile install nixpkgs#vue```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vue](/man/vue)(1)
