"use client";

import React from "react";
import { useContentListController } from "@/controller";

export default function Content() {
  const contents = useContentListController();

  return contents?.length > 0 ? (
    contents?.map((content) => <div>{content}</div>)
  ) : (
    <>No Content Stored.</>
  );
}
