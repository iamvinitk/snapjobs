import './App.css'
import {ThemeProvider} from "@/components/theme-provider.tsx";
import {SiteHeader} from "@/components/site-header.tsx";

function App() {

  return (
    <ThemeProvider attribute="class" defaultTheme="system" enableSystem disableTransitionOnChange>
          <div vaul-drawer-wrapper="">
            <div className="relative flex h-screen flex-col bg-background">
              <SiteHeader />
              <main className="flex-1"></main>
              {/*<SiteFooter />*/}
            </div>
          </div>
          {/*<TailwindIndicator />*/}
          {/*<ThemeSwitcher />*/}
          {/*<Analytics />*/}
          {/*<NewYorkToaster />*/}
          {/*<DefaultToaster />*/}
          {/*<NewYorkSonner />*/}
        </ThemeProvider>
  )
}

export default App
