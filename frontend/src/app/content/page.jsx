"use client";

import React from "react";
import { useContentListController } from "@/controller";
import { Button } from "@/components/ui/button";

export default function Content() {
  const contents = useContentListController();

  return (
    <>
      <Button className="my-2">Add Content</Button>
      {contents?.length > 0 ? (
        contents?.map((content) => <div>{content}</div>)
      ) : (
        <>No Content Stored.</>
      )}
    </>
  );
}
