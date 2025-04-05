import "@/styles/globals.css";
import Link from "next/link";
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  navigationMenuTriggerStyle,
} from "../components/ui/navigation-menu";

export default function App({ Component, pageProps }) {
  return (
    <>
      <div className="flex justify-between items-center bg-black p-4">
        <Link href="/" className="text-2xl text-white">
          Promplicity
        </Link>
        <NavigationMenu>
          <NavigationMenuList>
            <NavigationMenuItem>
              <Link href="/about" legacyBehavior passHref>
                <NavigationMenuLink className={navigationMenuTriggerStyle()}>
                  About
                </NavigationMenuLink>
              </Link>
            </NavigationMenuItem>
          </NavigationMenuList>
        </NavigationMenu>
      </div>
      <div className="flex flex-col min-h-screen">
        <main className="flex-grow my-4 md:mx-12 mx-8">
          <Component {...pageProps} />
        </main>

        <footer className="bg-gray-900 text-white text-center p-4">
          &copy; 2025 ShahTech. All rights reserved.
        </footer>
      </div>
    </>
  );
}
