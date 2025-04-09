import React from "react";
import { Button as _Button } from "../ui/button";
import Link from "next/link";

export default function Button({ children, className, href }) {
  const button = (
    <_Button href={href} className={`my-5 ${className}`}>
      {children}
    </_Button>
  );

  return href ? <Link href={href}>{button}</Link> : button;
}
