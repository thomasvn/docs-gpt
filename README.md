# LangChain - QA over Docs

```sh
jupyter lab
```

## Example

```json
{
    "question": "I've just installed my cloud billing integration, but I don't see any reconciled prices. Why?",
    "answer": "You may need to verify that the Helm values of `kubecostModel.etlCloudUsage` or `kubecostModel.etlCloudAsset` are not set to false. Cloud billing data may also lag by 24-48 hours.\n",
    "sources": "./data/docs/cloud-integration.md, ./data/docs/setup/frequently-asked-questions.md, ./data/docs/assets.md"
}
```

## Refs

- <https://docs.langchain.com/docs/use-cases/qa-docs>
- <https://python.langchain.com/en/latest/use_cases/question_answering.html>
- <https://python.langchain.com/en/latest/modules/indexes/getting_started.html>

<!-- 
TODO:
- Parameterize the query
- Save the database so we don't need to run the text loaders each time.
- Be capable of querying without the notebook.
- Indexed on Public Docs Repo and Private Support Repo
- Code inside embeddings?
- Chaining with the user conversation.

DONE:
- Manually put Kubecost docs into the data, and load it. Query the docs.
- Grab all documentation from the web.
-->