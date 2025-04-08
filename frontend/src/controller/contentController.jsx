import React, { useState, useEffect } from "react";

export function useContentListController() {
  const [contents, setContents] = useState([]);

  useEffect(() => {
    // Get the list of contents.
    // Store the content.
    setContents(["content1", "content2"]);
  }, []);

  return contents;
}
