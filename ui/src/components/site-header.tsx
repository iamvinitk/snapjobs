import { siteConfig } from "@/config/site";

import { MainNav } from "@/components/main-nav";
import { MobileNav } from "@/components/mobile-nav";
import { ModeToggle } from "@/components/mode-toggle";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/shad-components/ui/dropdown-menu";
import { Button } from "@/shad-components/ui/button";
import { Avatar, AvatarFallback, AvatarImage } from "@/shad-components/ui/avatar";
import React, {useEffect, useState} from "react";
import { User } from "@firebase/auth";

export function SiteHeader() {
  const [user, setUser] = useState<User | null>(null);
  const [fallbackText, setFallbackText] = useState<string>("L");

  useEffect(() => {
    const user = JSON.parse(localStorage.getItem("user") as string) as User;
    if (user) {
      setUser(user);
      // Extract the first letter of the first and last name
      const firstLetter = user?.displayName?.charAt(0);
      const lastLetter = user?.displayName?.split(" ")[1]?.charAt(0);
      setFallbackText(`${firstLetter}${lastLetter}`);
    }
  }, []);

  const handleLogout = (e: React.MouseEvent) => {
    console.log(typeof e, e)
    e.preventDefault();
    console.log("logout");
    localStorage.clear();
    setUser(null);
    window.location.href = siteConfig.routes.login;
  };

  return (
    <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-14 max-w-screen-2xl items-center">
        <MainNav />
        <MobileNav />
        <div className="flex flex-1 items-center justify-between space-x-2 md:justify-end">
          {/*<div className="w-full flex-1 md:w-auto md:flex-none">/!*<CommandMenu />*!/</div>*/}
          <nav className="flex items-center">
            <ModeToggle />
            <div className="ml-2">
              <DropdownMenu>
                <DropdownMenuTrigger asChild>
                  <Button variant="ghost" className="relative h-8 w-8 rounded-full">
                    <Avatar className="h-8 w-8">
                      <AvatarImage src={user?.photoURL as string} alt={user ? (user.displayName as string) : "Login"} />
                      <AvatarFallback>{fallbackText}</AvatarFallback>
                    </Avatar>
                  </Button>
                </DropdownMenuTrigger>
                <DropdownMenuContent className="w-56" align="end" forceMount>
                  {user ? (
                    <>
                      <DropdownMenuLabel className="font-normal">
                        <div className="flex flex-col space-y-1">
                          <p className="text-sm font-medium leading-none">{user?.displayName}</p>
                          <p className="text-xs leading-none text-muted-foreground">{user?.email}</p>
                        </div>
                      </DropdownMenuLabel>
                      <DropdownMenuSeparator />
                    </>
                  ) : null}
                  <DropdownMenuItem onClick={handleLogout}>
                    Log out
                  </DropdownMenuItem>
                </DropdownMenuContent>
              </DropdownMenu>
            </div>
          </nav>
        </div>
      </div>
    </header>
  );
}
