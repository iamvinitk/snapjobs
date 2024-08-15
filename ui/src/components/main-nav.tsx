import { siteConfig } from "@/config/site";
import { cn } from "@/lib/utils";
// @ts-ignore
import { User } from "@firebase/auth";

export function MainNav() {
  const pathname = window.location.pathname
  return (
    <div className="mr-4 hidden md:flex">
      <a href="/" className="mr-6 flex items-center space-x-2">
        {/*<Icons.logo className="h-6 w-6" />*/}
        <span className="hidden font-bold sm:inline-block">{siteConfig.name}</span>
      </a>
      <nav className="flex items-center gap-6 text-sm">
        <a
          href={siteConfig.routes.search}
          className={cn("transition-colors hover:text-foreground/80", pathname === siteConfig.routes.search ? "text-foreground" : "text-foreground/60")}
        >
          Search
        </a>
        <a
          href={siteConfig.routes.applications}
          className={cn("transition-colors hover:text-foreground/80", pathname === siteConfig.routes.applications ? "text-foreground" : "text-foreground/60")}
        >
          Applications
        </a>
        <a
          href={siteConfig.routes.snapAI}
          className={cn("transition-colors hover:text-foreground/80", pathname === siteConfig.routes.snapAI ? "text-foreground" : "text-foreground/60")}
        >
          SnapAI
        </a>
      </nav>
      {/*  <Link*/}
      {/*    href="/docs/components"*/}
      {/*    className={cn(*/}
      {/*      "transition-colors hover:text-foreground/80",*/}
      {/*      pathname?.startsWith("/docs/components")*/}
      {/*        ? "text-foreground"*/}
      {/*        : "text-foreground/60",*/}
      {/*    )}*/}
      {/*  >*/}
      {/*    Components*/}
      {/*  </Link>*/}
      {/*  <Link*/}
      {/*    href="/themes"*/}
      {/*    className={cn(*/}
      {/*      "transition-colors hover:text-foreground/80",*/}
      {/*      pathname?.startsWith("/themes")*/}
      {/*        ? "text-foreground"*/}
      {/*        : "text-foreground/60",*/}
      {/*    )}*/}
      {/*  >*/}
      {/*    Themes*/}
      {/*  </Link>*/}
      {/*  <Link*/}
      {/*    href="/examples"*/}
      {/*    className={cn(*/}
      {/*      "transition-colors hover:text-foreground/80",*/}
      {/*      pathname?.startsWith("/examples")*/}
      {/*        ? "text-foreground"*/}
      {/*        : "text-foreground/60",*/}
      {/*    )}*/}
      {/*  >*/}
      {/*    Examples*/}
      {/*  </Link>*/}
      {/*  <Link*/}
      {/*    href={siteConfig.links.github}*/}
      {/*    className={cn(*/}
      {/*      "hidden text-foreground/60 transition-colors hover:text-foreground/80 lg:block",*/}
      {/*    )}*/}
      {/*  >*/}
      {/*    GitHub*/}
      {/*  </Link>*/}
      {/*</nav>*/}
    </div>
  );
}
