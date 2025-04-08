import { ContentModel } from "@/model";

export default class ContentService {
  constructor(userId, contentId = null) {
    if (!userId) throw new Error("User Id not received.");

    this.userId = userId;
    this.contentId = contentId;
    this.contents = [];
  }

  #verifyContentId() {
    if (!this.contentId) throw new Error("Content Id not received.");
  }

  getAll() {
    this.#verifyContentId();

    // Get the list of all the content of the user.
    const contents = ["all", "the", "content"];

    // Store the content into the model.
    contents.forEach((content) => {
      this.contents.push(new ContentModel(1, content));
    });

    // Return all the contents.
    return contents;
  }
}
