package com.linuxcommandlibrary.app.nav

import androidx.compose.runtime.Immutable
import com.linuxcommandlibrary.app.ui.composables.AppIcon
import kotlinx.collections.immutable.ImmutableList
import kotlinx.collections.immutable.persistentListOf

@Immutable
internal data class TopLevelDestination(
    val key: RouteKey,
    val label: String,
    val icon: AppIcon,
)

internal val TopLevelDestinations: ImmutableList<TopLevelDestination> = persistentListOf(
    TopLevelDestination(RouteKey.Basics, "基础", AppIcon.PUZZLE),
    TopLevelDestination(RouteKey.Tips, "技巧", AppIcon.IDEA),
    TopLevelDestination(RouteKey.Commands, "命令", AppIcon.SEARCH),
)
