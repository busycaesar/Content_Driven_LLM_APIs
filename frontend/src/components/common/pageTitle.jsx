import React from "react";

export default function PageTitle({ children, className }) {
  return <h1 className={`text-3xl font-bold my-5 ${className}`}>{children}</h1>;
}
