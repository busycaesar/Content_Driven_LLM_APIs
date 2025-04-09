import React from "react";
import { Textarea } from "@/components/ui/textarea";
import { Button, PageTitle } from "@/components/common";

export default function newContent() {
  return (
    <>
      <PageTitle>New Content</PageTitle>
      <Button href="/content">Back</Button>
      <Textarea />
      <Button>Store Content</Button>
    </>
  );
}
