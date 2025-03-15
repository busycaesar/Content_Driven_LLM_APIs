# APIs

## User

- POST `/api/user/register`: Register a new user.
- POST `/api/user/validate`: Validate an existing user.
- PATCH `/api/user/password`: Update a password of an existing user.
- GET `/api/user`: Get user information.
- DELETE `/api/user`: Delete an existing user.

## Content

- POST `/api/content`: Store a new content in vector database.
- GET `/api/content`: Get all the stored content by the user.
- GET `/api/content/:contentId`: Get a specific stored content.
- PUT `/api/content/:contentId`: Update a specific stored content.
- DELETE `/api/content/:contentId`: Delete a specific stored content.

## Prompt Template

- PUT `/api/prompt_template/:contentId`: Update stored prompt template for the specific content.
- GET `/api/prompt_template/:contentId`: Get stored prompt template for the specific content.

## LLM

- GET `/api/llm`: Get the list of available LLMs.

## Content Model

- PUT `/api/content_model/:contentId`: Add a specific model for the content.
- GET `/api/content_model/:contentId`: Get the model stored for the content.

## Conversation

- POST `/api/conversation`: Generates the response to the prompt.
- GET `/api/conversation`: Get the conversation history.
