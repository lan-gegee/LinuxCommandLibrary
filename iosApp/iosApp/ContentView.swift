import SwiftUI

/// Native 3-tab SwiftUI shell. Tab selection is driven by AppRouter so deep links
/// can switch tabs programmatically.
struct ContentView: View {
    @EnvironmentObject private var router: AppRouter

    var body: some View {
        TabView(selection: $router.selectedTab) {
            BasicCategoriesView()
                .tag(AppRouter.Tab.basics)
                .tabItem {
                    Label("基础", systemImage: "book.fill")
                }

            TipsView()
                .tag(AppRouter.Tab.tips)
                .tabItem {
                    Label("技巧", systemImage: "lightbulb.fill")
                }

            CommandsTabView()
                .tag(AppRouter.Tab.commands)
                .tabItem {
                    Label("命令", systemImage: "terminal")
                }
        }
        .tint(.brandRed)
    }
}
