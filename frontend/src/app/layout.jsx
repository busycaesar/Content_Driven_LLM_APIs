import "./globals.css";
import NavBar from "@/components/common/nav-bar";

export const metadata = {
  title: "Promptlicity",
  description: "Official website of Promptlicity.",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.ico" />
      </head>
      <body>
        <NavBar />
        <div className="flex flex-col min-h-screen">
          <main className="flex-grow my-4 md:mx-12 mx-8">{children}</main>

          <footer className="bg-gray-900 text-white text-center p-4">
            &copy; 2025 ShahTech. All rights reserved.
          </footer>
        </div>
      </body>
    </html>
  );
}
