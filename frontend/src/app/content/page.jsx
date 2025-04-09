"use client";

import React from "react";
import { useContentListController } from "@/controller";
import { Button, PageTitle } from "@/components/common";

export default function Content() {
  const contents = useContentListController();

  return (
    <>
      <Button href="/content/new">Add Content</Button>
      <PageTitle>Stored Content</PageTitle>
      {contents?.length > 0 ? (
        contents?.map((content) => <div>{content}</div>)
      ) : (
        <>No Content Stored.</>
      )}
    </>
  );
}
