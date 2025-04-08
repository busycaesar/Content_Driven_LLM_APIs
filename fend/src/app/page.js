import Image from "next/image";
import logo from "../../public/logos.png";

export default function Home() {
  return (
    <>
      <h1 className="text-center md:text-[6em] text-[2.5em] font-bold my-2">
        Promptlicity
        <sup className="inline-block">
          <Image src={logo} alt="ShahTech Logo" className="md:w-26 w-16" />
        </sup>
      </h1>
      <h2 className="text-center md:text-[2.5em] text-[1.5em] font-bold my-2">
        AI-powered responses from your own content
      </h2>
      <p className="text-lg my-7">
        PromptlicityAI is a platform that enables users to store and manage
        custom content, which can then be used to generate knowledge-based
        responses through API calls. With PromptlicityAI, you can easily store
        content in a structured way and retrieve relevant knowledge chunks based
        on prompts—without needing to understand the underlying architecture of
        Retrieval-Augmented Generation (RAG) applications or how frameworks like
        work. PromptlicityAI simplifies the process of managing and querying
        knowledge content, enabling seamless AI integration without the
        complexity of underlying systems.
      </p>
      <h2 className="md:text-[2em] text-[1em] font-bold my-2">Features</h2>
      <ul>
        <li>
          <strong>Content Storage</strong>: Store and manage custom content with
          ease. API Access: Generate API keys to retrieve knowledge-based
          responses using the stored content.
        </li>
        <li>
          <strong>User-Friendly Interface</strong>: A simple dashboard where
          users can manage their content and API keys, making it easy to
          integrate and retrieve responses from stored knowledge.
        </li>
        <li>
          <strong>No Technical Overhead</strong>: Users don’t need to know the
          complex processes of how knowledge is stored, chunks are retrieved, or
          how to work with large language models (LLMs) for generating
          responses.
        </li>
        <li>
          <strong>Knowledge-Based Responses</strong>: Get relevant responses
          from your content based on the prompts you provide.
        </li>
      </ul>
    </>
  );
}
