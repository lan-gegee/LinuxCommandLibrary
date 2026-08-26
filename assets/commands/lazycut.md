# TAGLINE

基于终端的视频剪辑工具

# TLDR

在终端中交互式地**剪辑视频**文件

```lazycut [video.mp4]```

打开**指定视频**进行剪辑

```lazycut [path/to/file.mkv]```

# SYNOPSIS

**lazycut** _video-file_

# DESCRIPTION

**lazycut** 是一款基于终端的视频剪辑工具，它提供交互式 TUI 用于标记入点/出点并导出剪辑后的视频片段。它借助 **chafa** 直接在终端中渲染视频帧，并用 **FFmpeg** 处理剪切，从而无需离开命令行就能快速精确地修剪视频。

界面采用 vim 风格的按键绑定进行导航，跳转时支持重复计数（例如 **5l** 表示向前跳转 5 秒）。设置好入点和出点后，按 Enter 即可导出剪辑好的片段。

# KEYBOARD CONTROLS

**Space**
> 播放或暂停。

**h** / **l**
> 后退或前进 1 秒。

**H** / **L**
> 后退或前进 5 秒。

**i** / **o**
> 设置剪辑的入点或出点。

**Enter**
> 导出剪辑后的片段。

**?**
> 显示帮助菜单。

**q**
> 退出程序。

# CAVEATS

需要同时安装 **FFmpeg** 和 **chafa** 并保证它们位于 PATH 中。终端渲染质量取决于终端模拟器的能力和字体大小。标准 Linux 发行版软件源中没有收录此工具——必须通过 Homebrew 安装或从源码构建。

# HISTORY

**lazycut** 由 **Emin Ozata** 创建，最初以开源项目形式发布在 **GitHub** 上，采用 **MIT 许可证**。它完全用 **Go** 编写，在 Hacker News 上出现后开始受到关注。对于简单的剪辑任务而言，它是 GUI 视频编辑器的轻量替代品。

# INSTALL

```brew: brew install lazycut```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [chafa](/man/chafa)(1)
